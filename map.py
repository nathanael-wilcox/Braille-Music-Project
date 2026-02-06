import xml.etree.ElementTree as ET
import cadquery as cq

ascii = ["\u2800", "\u2801", "\u2802", "\u2803", "\u2804", "\u2805", "\u2806", "\u2807", "\u2808", "\u2809", "\u280a", "\u280b", "\u280c", "\u280d", "\u280e", "\u280f", "\u2810", "\u2811", "\u2812", "\u2813", "\u2814", "\u2815", "\u2816", "\u2817", "\u2818", "\u2819", "\u281a", "\u281b", "\u281c", "\u281d", "\u281e", "\u281f",
         "\u2820", "\u2821", "\u2822", "\u2823", "\u2824", "\u2825", "\u2826", "\u2827", "\u2828", "\u2829", "\u282a", "\u282b", "\u282c", "\u282d", "\u282e", "\u282f", "\u2830", "\u2831", "\u2832", "\u2833", "\u2834", "\u2835", "\u2836", "\u2837", "\u2838", "\u2839", "\u283a", "\u283b", "\u283c", "\u283d", "\u283e", "\u283f"]
dots = ["", "1", "2", "12", "3", "13", "23", "123", "4", "14", "24", "124", "34", "134", "234", "1234", "5", "15", "25", "125", "35", "135", "235", "1235", "45", "145", "245", "1245", "345", "1345", "2345", "12345", "6", "16",
        "26", "126", "36", "136", "236", "1236", "46", "146", "246", "1246", "346", "1346", "2346", "12346", "56", "156", "256", "1256", "356", "1356", "2356", "12356", "456", "1456", "2456", "12456", "3456", "13456", "23456", "123456"]
chars = [" ", "a", "1", "b", "'", "k", "2", "l", "@", "c", "i", "f", "/", "m", "s", "p", "\"", "e", "3", "h", "9", "o", "6", "r", "^", "d", "j", "g", ">", "n", "t", "q",
         ",", "*", "5", "<", "-", "u", "8", "v", ".", "%", "[", "$", "+", "x", "!", "&", ";", ":", "4", "\\", "0", "z", "7", "(", "_", "?", "w", "]", "#", "y", ")", "="]
numbers = {0: "245", 1: "1", 2: "12", 3: "14", 4: "145",
           5: "15", 6: "124", 7: "1245", 8: "125", 9: "24"}
symbols = {"number": "3456", "sharp": "146", "flat": "126", "natural": "16", "db": "126 13", "dp": "345 145", "tdp": "345 256", "common": "46 14", "slur": "14", "repeat": "2356", "startSlur": "56 12",
           "sdb": "126 13 3", "er": "1346", "qr": "1236", "hr": "136", "wr": "134", "dot": "3", "cp": "345 14", "tcp": "345 25", "cut": "456 14", "tie": "4 14", "mr": "134", "endSlur": "45 23"}
notes = {0: "145", 2: "15", 4: "124",
         5: "1245", 7: "125", 9: "24", 11: "245", }
lengths = {"128th": "", "64th": "6", "32nd": "3", "16th": "36",
           "eighth": "", "quarter": "6", "half": "3", "whole": "36"}
octaves = {0: "4 4", 1: "4", 2: "45", 3: "456",
           4: "5", 5: "46", 6: "56", 7: "6", 8: "6 6"}
noteShift = {"C": 0, "D": 2, "E": 4, "F": 5, "G": 7, "A": 9, "B": 11}
flatKeys = [{"type": "flat", "note": 10}, {"type": "flat", "note": 3}, {"type": "flat", "note": 8}, {
    "type": "flat", "note": 1}, {"type": "flat", "note": 6}, {"type": "flat", "note": 11}, {"type": "flat", "note": 4}]
sharpKeys = [{"type": "sharp", "note": 6}, {"type": "sharp", "note": 1}, {"type": "sharp", "note": 8}, {
    "type": "sharp", "note": 3}, {"type": "sharp", "note": 10}, {"type": "sharp", "note": 5}, {"type": "sharp", "note": 0}]
abbreviations = {"ritardando": "rit'", "crescendo": "cr'",
                 "cresc'": "cr'", "decrescendo": "decr'", "decresc'": "decr'"}
dynamics = ["pppppp", "ppppp", "pppp", "ppp", "pp", "p", "mp", "mf", "f", "ff", "fff", "ffff", "fffff", "ffffff",
            "fp", "pf", "sf", "sfz", "sff", "sffz", "sfff", "sfffz", "sfp", "sfpp", "rfz", "rf", "fz", "m", "r", "z", "s", "n"]
punctuation = {",": "2", ";": "23", "'": "3", ":": "25", "-": "36", ".": "256", "_": "6",
               "!": "235", "oq": "236", "?": "236", "cq": "356", "(": "2356", ")": "2356", "/": "34"}

LINE_WIDTH = 36


class Key:
    def __init__(self, type: str, note: int):
        self.type = type
        self.note = note


class Text:
    def __init__(self, text: str):
        self.text = text


# Example data - {"length": "half"}
class Rest:
    def __init__(self, length: str):
        self.length = length


# Example data - {"length": "dotted quarter", "note": 35, "sign": "none"},
#                {"length": "eighth", "note": 41, "sign": "flat"}
class Note:
    def __init__(self, length: str, note: int, sign: str, tie: bool, slur: str):
        self.length = length
        self.note = note
        self.sign = sign
        self.tie = tie
        self.slur = slur


class Measure:
    def __init__(self, number: int, data: list[Rest | Note | Text]):
        self.number = number
        self.data = data
        self.lyrics = ""
        self.length = 0

    def addText(self, text: Text):
        self.data.append(text)

    def addNote(self, note: Rest | Note | Text):
        self.data.append(note)

    def addLyrics(self, lyrics: str):
        self.lyrics = lyrics

    def print(self, printNumber: bool, lastNote: int, key: list[Key]):
        str = ""
        firstNote = True
        trimmedStr = ""
        if printNumber:  # Prints the measure number if needed
            str += getChar(symbols["number"]) + \
                getChar(numbers[self.number]) + " "
        for d in self.data:  # For each item in the measure
            if isinstance(d, Rest):
                length = d.length
                if len(length.split()) == 1:  # If length is just one word
                    str += getChar(symbols[length[0] + "r"])
                    trimmedStr += getChar(symbols[length[0] + "r"])
                elif length.split()[0] == "dotted":  # If length has dotted in front
                    str += getChar(symbols[length.split()[1]
                                   [0] + "r"]) + getChar(symbols["dot"])
                    trimmedStr += getChar(symbols[length.split()
                                          [1][0] + "r"]) + getChar(symbols["dot"])
            elif isinstance(d, Text):
                if len(d.text.split()) == 1:
                    str += ">" + d.text
                    if d.text in dynamics:
                        trimmedStr += ">" + d.text
                else:
                    if lastNote > 0:
                        str += " >" + d.text + "> "
                    else:
                        str += ">" + d.text + "> "
                lastNote = -1
            elif isinstance(d, Note):
                length = d.length
                note = d.note
                sign = d.sign
                tie = d.tie
                slur = d.slur

                # Print start of slur character
                if slur == "start":
                    str += getChar(symbols["startSlur"])
                    trimmedStr += getChar(symbols["startSlur"])
                # Print slur character
                elif slur == "slur":
                    str += getChar(symbols["slur"])
                    trimmedStr += getChar(symbols["slur"])

                # If there is no last note or the last note was more than
                # 7 half-steps away, print an octave marker
                if abs(note - lastNote) > 7:
                    if not firstNote:
                        trimmedStr += getChar(octaves[(note + 8) // 12])
                    str += getChar(octaves[(note + 8) // 12])
                # Else if the note is within 4 half-steps of the last note
                # and is on a new octave print octave marker
                elif abs(note - lastNote) > 4:
                    if not (note + 8) // 12 == (lastNote + 8) // 12:
                        if not firstNote:
                            trimmedStr += getChar(octaves[(note + 8) // 12])
                        str += getChar(octaves[(note + 8) // 12])

                # Check for accidentals
                if not sign == "none":
                    if sign == "natural":
                        # If note is natural, check for that note in the key signature and remove it
                        key = [k for k in key if k.note != note]
                        str += getChar(symbols[sign])
                        trimmedStr += getChar(symbols[sign])
                    else:
                        # Append the new accidental to the key signature
                        key.append(Key(sign, (note + 8) % 12))
                        str += getChar(symbols[sign])
                        trimmedStr += getChar(symbols[sign])

                if len(length.split()) == 1:
                    str += makeNote(note, length, key)
                    trimmedStr += makeNote(note, length, key)
                elif length.split()[0] == "dotted":
                    str += makeNote(note, length.split()
                                    [1], key) + getChar(symbols["dot"])
                    trimmedStr += makeNote(note, length.split()
                                           [1], key) + getChar(symbols["dot"])

                # Print end of slur character
                if slur == "end":
                    str += getChar(symbols["endSlur"])
                    trimmedStr += getChar(symbols["endSlur"])

                # Print tie character
                if tie:
                    str += getChar(symbols["tie"])
                    trimmedStr += getChar(symbols["tie"])

                lastNote = note
                firstNote = False
        self.length = len(str)
        return [lastNote, str, trimmedStr]


# Example time - [3, 4]
class Song:
    def __init__(self, key: list[Key], beatName: str, time: list[int], text: str, measures: list[Measure]):
        self.key = key
        self.beatName = beatName
        self.time = time
        self.text = text
        self.measures = measures
        self.measureSize = 16  # Determines how many measures are on a line

    def addMeasure(self, measure: Measure):
        self.measures.append(measure)

    def write(self, file: str):
        res = ""
        if self.text:
            res += self.text + " "
        for k in self.key:  # Print every flat or sharp in the key signature
            res += getChar(symbols[k.type])
        # Print number sign and time signature
        if len(self.beatName):
            res += getChar(symbols[self.beatName])
        else:
            res += getChar(symbols["number"])
            res += getChar(numbers[self.time[0]])
            res += getChar(shiftDown(numbers[self.time[1]]))

        i = ((LINE_WIDTH - len(res)) // 2) + 3
        if self.text:
            while i > 0:
                res = " " + res
                i -= 1
        else:
            res = "  " + res
        res += "\n"

        i = 0
        lastNote = -1
        runningLength = 0
        lyricLength = 0
        lastMeasure = ""
        lyrics = ""
        for m in self.measures:  # For each measure, print and check for new line
            mData = m.print(i % self.measureSize == 0, lastNote, self.key)
            hasLyrics = False
            if m.lyrics != "":
                hasLyrics = True

            lastNote = mData[0]
            thisMeasure = mData[2]
            if thisMeasure == lastMeasure or (len(lastMeasure) > 0 and lastMeasure[0] == ">" and thisMeasure == lastMeasure[2:]):
                runningLength += 1
                if runningLength > LINE_WIDTH or (hasLyrics and lyricLength > LINE_WIDTH):
                    res += "\n  "
                    runningLength = 1
                    newLyrics = m.lyrics
                    newLyrics = "".join(
                        ["_" + ch if ch.isupper() else ch for ch in newLyrics])
                    newLyrics = "".join(
                        [getChar(punctuation[ch]) if ch in punctuation else ch for ch in newLyrics])
                    newLyrics = newLyrics.lower()
                    lyrics += newLyrics
                    lyrics += "\n"
                    lyricLength = 0
                if res.split()[-1][0:2] == getChar(symbols["repeat"]) + getChar(symbols["number"]):
                    # Get number of repeated measures and add 1
                    res = res[0:-2] + getChar(numbers[list(numbers.keys())[list(numbers.values()).index(
                        getDots(res.split(" ")[-2][2:]))] + 1])
                    lastNote = -1
                elif res.split()[-2] == getChar(symbols["repeat"]) and res.split()[-1] == getChar(symbols["repeat"]):
                    res = res[:-4] + getChar(symbols["repeat"]) + getChar(
                        symbols["number"]) + getChar(numbers[3])
                    runningLength -= 3
                    lastNote = -1
                else:
                    res += getChar(symbols["repeat"])
            else:
                runningLength += m.length
                newLyrics = m.lyrics
                newLyrics = "".join(
                    ["_" + ch if ch.isupper() else ch for ch in newLyrics])
                newLyrics = "".join(
                    [getChar(punctuation[ch]) if ch in punctuation else ch for ch in newLyrics])
                newLyrics = newLyrics.lower()
                lyricLength += len(newLyrics)
                if runningLength > LINE_WIDTH or (hasLyrics and lyricLength > LINE_WIDTH):
                    mData = m.print(i % self.measureSize == 0, -1, self.key)
                    mData[1] = "  " + mData[1]
                    res += "\n"
                    runningLength = m.length
                    lyrics += "\n"
                    lyricLength = len(newLyrics)
                lyrics += newLyrics
                res += mData[1]
            lastMeasure = mData[2]
            if not i % self.measureSize == self.measureSize - 1 and not i == len(self.measures) - 1:
                res += " "
            elif i % self.measureSize == self.measureSize - 1 and not i == len(self.measures) - 1:
                res += "\n"
                lastNote = -1
            i += 1

        res += getChar(symbols["db"])  # Print double bar line

        if lyrics.strip() == "":
            with open(file, "w") as f:
                f.write(res)
        else:
            with open(file, "w") as f:
                lyricLines = lyrics.split("\n")
                noteLines = res.split("\n")
                f.write(noteLines[0] + "\n")
                for x, line in enumerate(noteLines):
                    if x > 0:
                        f.write(
                            lyricLines[x - 1] + "\n  " + line.strip() + "\n")


def shiftDown(code: str):  # Shifts a dot code down by one
    newCode = ""
    for c in code:
        newCode += str(int(c) + 1)
    return newCode


def getChar(code: str):  # Returns the character value of the provided dot code(s)
    arr = code.split()
    str = ""
    for c in arr:
        str += chars[dots.index(c)]
    return str


def getDots(char: str):  # Returns the dot code of the provided character code
    return dots[chars.index(char)]


def getAscii(code: str):  # Returns the braille ascii character for the provided dot code(s)
    arr = code.split()
    str = ""
    for c in arr:
        str += ascii[dots.index(c)]
    return str


# Combines note dot code with length code and checks for accidentals
def makeNote(note: int, length: str, key: list[Key]):
    for k in key:
        if (note + 8) % 12 == k.note:
            if k.type == "flat":
                note += 1
            elif k.type == "sharp":
                note -= 1
    chars = list(notes[(note + 8) % 12]) + list(lengths[length])
    chars.sort()
    return getChar("".join(chars))


def handleXML(input: str | None):
    output: str = ""
    if type(input) == str:
        output = input
    return output


# Parsing the MusicXML file
def parseFile(file: str):
    tree = ET.parse(file)
    root = tree.getroot()

    firstMeasure = root.find("./part/measure")

    if firstMeasure is None:
        raise Exception("Provided file has no measures")

    beat = int(handleXML(firstMeasure.findall(
        "./attributes/time/beats")[0].text))
    beatType = int(handleXML(firstMeasure.findall(
        "./attributes/time/beat-type")[0].text))
    beatName = ""
    time = firstMeasure.find("./attributes/time")
    if time is not None and len(time.attrib) > 0 and time.attrib["symbol"] is not None:
        beatName = time.attrib["symbol"]
    accidentals = int(handleXML(firstMeasure.findall(
        "./attributes/key/fifths")[0].text))
    text = ""
    direction = firstMeasure.find("./direction")
    if direction is not None and direction.find("./direction-type/words") is not None and \
            direction.find("./direction-type/words").text.replace(".", "'") not in abbreviations:  # type:ignore
        text = "," + \
            handleXML(firstMeasure.findall(
                "./direction/direction-type/words")[0].text).lower() + "4"
        el = root.find("./part/measure/direction")
        if el is not None:
            firstMeasure.remove(el)

    # Add accidentals to key signature
    key = []
    if accidentals > 0:
        i = 0
        while i < abs(accidentals):
            key.append(Key(sharpKeys[i]["type"], sharpKeys[i]["note"]))
            i += 1
    elif accidentals < 0:
        i = 0
        while i < abs(accidentals):
            key.append(Key(flatKeys[i]["type"], flatKeys[i]["note"]))
            i += 1

    song = Song(key, beatName, [beat, beatType], text, [])
    lastCresc = ""

    notes = list(root.findall("./part/measure/note"))
    slur = 0
    longSlur = False

    lyrics = ""

    for child in root.findall("./part/measure"):  # For each measure in XML
        m = Measure(int(child.attrib["number"]), [])
        childList = list(child)
        for c in child:
            lastChild = True if childList.index(
                c) == len(childList) - 1 else False
            if c.tag == "direction":
                tag = c.find("./direction-type/words")
                if tag is not None and tag.text:
                    tag = tag.text.lower().replace(".", "'")
                    if tag in abbreviations:
                        m.addText(Text(abbreviations[tag]))
                    else:
                        m.addText(Text(tag))
                tag = c.find("./direction-type/dynamics")
                if tag is not None and tag[0] is not None:
                    m.addText(Text(tag[0].tag))
                tag = c.find("./direction-type/wedge")
                if tag is not None and tag.attrib["type"] is not None:
                    if tag.attrib["type"] == "crescendo":
                        lastCresc = "14"
                        m.addText(Text(getChar(lastCresc)))
                    elif tag.attrib["type"] == "diminuendo":
                        lastCresc = "145"
                        m.addText(Text(getChar(lastCresc)))
                    elif tag.attrib["type"] == "stop":
                        if lastChild or childList[childList.index(c) + 1].tag == "barline":
                            m.addText(Text(getChar(shiftDown(lastCresc))))
                        else:
                            m.addText(
                                Text(getChar(shiftDown(lastCresc)) + "'"))
                        lastCresc = ""
            elif c.tag == "note":
                if slur > 0:
                    slur -= 1
                if c.findall("./pitch"):  # If note is a note
                    # Find absolute pitch value from octave and note name
                    pitch: int = int(handleXML(c.findall("./pitch/octave")[0].text)) * 12 - 8 \
                        + noteShift[handleXML(c.findall("./pitch/step")[0].text)]
                    sign: str = "none"
                    tie = False
                    slurValue = ""
                    if not longSlur and slur > 0:
                        slurValue = "slur"
                    if c.find("./notations/tied") is not None and \
                            handleXML(c.findall("./notations/tied")[0].attrib["type"]) == "start":  # Check for tie
                        tie = True
                    if c.find("./notations/slur") is not None and \
                            handleXML(c.findall("./notations/slur")[0].attrib["type"]) == "start":  # Check for slur start
                        currentNote = notes.index(c)
                        slurValue = "start"
                        for i in range(len(notes) - currentNote - 1):
                            if notes[i + currentNote + 1].find("./notations/slur") is not None:
                                longSlur = True
                                if i <= 2:
                                    longSlur = False
                                    slurValue = ""
                                slur = i + 2
                                break
                    if slur == 1 and longSlur:
                        slurValue = "end"
                        longSlur = False
                    if c.find("./accidental") is not None:  # Check for accidental
                        sign = handleXML(c.findall("./accidental")[0].text)
                    if c.find("./pitch/alter") is not None:  # Check for pitch shift
                        pitch += int(handleXML(c.findall("./pitch/alter")
                                     [0].text))
                    length: str = handleXML(c.findall("./type")[0].text)
                    if c.find("./dot") is not None:  # Check for dotted note
                        length = "dotted " + length
                    note = Note(length, pitch, sign, tie, slurValue)
                    m.addNote(note)

                    if c.find("./lyric/text") is not None and c.find("./lyric/syllabic") is not None:
                        lyrics += c.find("./lyric/text").text  # type:ignore
                        val = c.find("./lyric/syllabic")
                        if val is not None and (val.text == "single" or val.text == "end"):
                            lyrics += " "
                elif c.findall("./rest"):  # If note is a rest
                    if len(c.findall("./type")) > 0:
                        note = Rest(handleXML(c.findall("./type")[0].text))
                    else:
                        note = Rest("measure")
                    m.addNote(note)
        m.addLyrics(lyrics)
        song.addMeasure(m)
        lyrics = ""

    return song


def makeStl(file: str, stl: str):
    with open(file, "r") as f:
        th = 1.2
        dia = 1.6
        a = 2.5
        l = 6.0
        e = 10
        dr = 0.8
        dh = 0.6
        r = 0.6
        pad = 8
        dotValues = [(-a, -a/2), (0, -a/2), (a, -a/2),
                     (-a, a/2), (0, a/2), (a, a/2)]
        points = []

        width = 0
        # width = LINE_WIDTH
        height = 0

        for i, line in enumerate(f):
            line = line.rstrip()
            height += 1
            curWidth = 0
            for j, char in enumerate(line):
                curWidth += 1
                charDots = getDots(char)
                for d in charDots:
                    dv = list(dotValues[int(d)-1])
                    dv[0] += i*e
                    dv[1] += j*l
                    points.append(tuple(dv))
            if curWidth > width:
                width = curWidth

        plate = (cq.Workplane("XY")
                 .box(height * 2 * a + (height - 1) * (e - 2 * a) + dia + pad, width * a + (width - 1) * (l - a) + dia + pad, th)
                 .edges("|Z")
                 .fillet(r)
                 )

        result = (cq.Workplane("XY")
                  .pushPoints(points)
                  .sphere(dr)
                  .translate((-e * (height - 1)/2, -l * (width - 1)/2, th/2 - (dr - dh)))
                  .split(True, False)
                  .union(plate)
                  )

        cq.exporters.export(result, stl)


song = parseFile("lyrics.musicxml")
song.write("song.brf")

makeStl("song.brf", "res.stl")
