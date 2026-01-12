import xml.etree.ElementTree as ET

ascii = ["\u2800", "\u2801", "\u2802", "\u2803", "\u2804", "\u2805", "\u2806", "\u2807", "\u2808", "\u2809", "\u280a", "\u280b", "\u280c", "\u280d", "\u280e", "\u280f", "\u2810", "\u2811", "\u2812", "\u2813", "\u2814", "\u2815", "\u2816", "\u2817", "\u2818", "\u2819", "\u281a", "\u281b", "\u281c", "\u281d", "\u281e", "\u281f",
         "\u2820", "\u2821", "\u2822", "\u2823", "\u2824", "\u2825", "\u2826", "\u2827", "\u2828", "\u2829", "\u282a", "\u282b", "\u282c", "\u282d", "\u282e", "\u282f", "\u2830", "\u2831", "\u2832", "\u2833", "\u2834", "\u2835", "\u2836", "\u2837", "\u2838", "\u2839", "\u283a", "\u283b", "\u283c", "\u283d", "\u283e", "\u283f"]
dots = ["", "1", "2", "12", "3", "13", "23", "123", "4", "14", "24", "124", "34", "134", "234", "1234", "5", "15", "25", "125", "35", "135", "235", "1235", "45", "145", "245", "1245", "345", "1345", "2345", "12345", "6", "16",
        "26", "126", "36", "136", "236", "1236", "46", "146", "246", "1246", "346", "1346", "2346", "12346", "56", "156", "256", "1256", "356", "1356", "2356", "12356", "456", "1456", "2456", "12456", "3456", "13456", "23456", "123456"]
chars = [" ", "a", "1", "b", "'", "k", "2", "l", "@", "c", "i", "f", "/", "m", "s", "p", "\"", "e", "3", "h", "9", "o", "6", "r", "^", "d", "j", "g", ">", "n", "t", "q",
         ",", "*", "5", "<", "-", "u", "8", "v", ".", "%", "[", "$", "+", "x", "!", "&", ";", ":", "4", "\\", "0", "z", "7", "(", "_", "?", "w", "]", "#", "y", ")", "="]
numbers = {0: "245", 1: "1", 2: "12", 3: "14", 4: "145",
           5: "15", 6: "124", 7: "1245", 8: "125", 9: "24"}
symbols = {"number": "3456", "sharp": "146", "flat": "126", "natural": "16", "db": "126 13",
           "sdb": "126 13 3", "er": "1346", "qr": "1236", "hr": "136", "wr": "134", "dot": "3"}
notes = {0: "145", 2: "15", 4: "124",
         5: "1245", 7: "125", 9: "24", 11: "245", }
lengths = {"eighth": "", "quarter": "6", "half": "3", "whole": "36"}
octaves = {0: "4 4", 1: "4", 2: "45", 3: "456",
           4: "5", 5: "46", 6: "56", 7: "6", 8: "6 6"}
noteShift = {"C": 0, "D": 2, "E": 4, "F": 5, "G": 7, "A": 9, "B": 11}
flatKeys = [{"type": "flat", "note": 10}, {"type": "flat", "note": 3}, {"type": "flat", "note": 8}, {
    "type": "flat", "note": 1}, {"type": "flat", "note": 6}, {"type": "flat", "note": 11}, {"type": "flat", "note": 4}]
sharpKeys = [{"type": "sharp", "note": 6}, {"type": "sharp", "note": 1}, {"type": "sharp", "note": 8}, {
    "type": "sharp", "note": 3}, {"type": "sharp", "note": 10}, {"type": "sharp", "note": 5}, {"type": "sharp", "note": 0}]


class Key:
    def __init__(self, type: str, note: int):
        self.type = type
        self.note = note


# Example data - {"length": "half"}
class Rest:
    def __init__(self, length: str):
        self.type = "rest"
        self.length = length


# Example data - {"length": "dotted quarter", "note": 35, "sign": "none"},
#                {"length": "eighth", "note": 41, "sign": "flat"}
class Note:
    def __init__(self, length: str, note: int, sign: str):
        self.type = "note"
        self.length = length
        self.note = note
        self.sign = sign


class Measure:
    def __init__(self, number: int, data: list[Rest | Note]):
        self.number = number
        self.data = data

    def addNote(self, note: Rest | Note):
        self.data.append(note)

    def print(self, printNumber: bool, lastNote: int, key: list[Key]):
        str = ""
        if printNumber:  # Prints the measure number if needed
            str += getChar(symbols["number"]) + \
                getChar(numbers[self.number]) + "  "
        for d in self.data:  # For each item in the measure
            length = d.length
            type = d.type
            if isinstance(d, Rest):
                if len(length.split()) == 1:  # If length is just one word
                    str += getChar(symbols[length[0] + "r"])
                elif length.split()[0] == "dotted":  # If length has dotted in front
                    str += getChar(symbols[length.split()[1][0] + "r"])
                    str += getChar(symbols["dot"])
            if isinstance(d, Note):
                note = d.note
                sign = d.sign
                # If there is no last note or the last note was more than
                # 8 half-steps away, print an octave marker
                if lastNote < 0 or abs(note - lastNote) > 8:
                    str += getChar(octaves[(note + 8) // 12])
                # Else if the note is within 4 half-steps of the last note
                # and is on a new octave print octave marker
                elif abs(note - lastNote) > 4:
                    if not (note + 8) // 12 == (lastNote + 8) // 12:
                        str += getChar(octaves[(note + 8) // 12])

                # Check for accidentals
                if not sign == "none":
                    if sign == "natural":
                        # If note is natural, check for that note in the key signature and remove it
                        key = [k for k in key if k.note != note]
                        str += getChar(symbols[sign])
                    else:
                        # Append the new accidental to the key signature
                        key.append(Key(sign, (note + 8) % 12))
                        str += getChar(symbols[sign])

                if len(length.split()) == 1:
                    str += makeNote(note, length, key)
                elif length.split()[0] == "dotted":
                    str += makeNote(note, length.split()[1], key)
                    str += getChar(symbols["dot"])

                lastNote = note
        return [lastNote, str]


# Example time - [3, 4]
class Song:
    def __init__(self, key: list[Key], time: list[int], measures: list[Measure]):
        self.key = key
        self.time = time
        self.measures = measures
        self.measureSize = 8  # Determines how many measures are on a line

    def addMeasure(self, measure: Measure):
        self.measures.append(measure)

    def write(self, file: str):
        res = ""
        for k in self.key:  # Print every flat or sharp in the key signature
            res += getChar(symbols[k.type])
        # Print number sign and time signature
        res += getChar(symbols["number"])
        res += getChar(numbers[self.time[0]])
        res += getChar(shiftDown(numbers[self.time[1]]))
        res += "\n"

        i = 0
        lastNote = -1
        for m in self.measures:  # For each measure, print and check for new line
            mData = m.print(i % self.measureSize == 0, lastNote, self.key)
            lastNote = mData[0]
            res += mData[1]
            if not i % self.measureSize == self.measureSize - 1 and not i == len(self.measures) - 1:
                res += "  "
            elif i % self.measureSize == self.measureSize - 1 and not i == len(self.measures) - 1:
                res += "\n"
                lastNote = -1
            i += 1

        res += getChar(symbols["db"])  # Print double bar line
        res += "\n"
        with open(file, "w") as f:
            f.write(res)


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

    firstMeasure = root.findall("./part/measure/attributes")[0]

    beat = int(handleXML(firstMeasure.findall("./time/beats")[0].text))
    beatType = int(handleXML(firstMeasure.findall(
        "./time/beat-type")[0].text))
    accidentals = int(handleXML(firstMeasure.findall("./key/fifths")[0].text))

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

    song = Song(key, [beat, beatType], [])

    for child in root.findall("./part/measure"):  # For each measure in XML
        m = Measure(int(child.attrib["number"]), [])
        for c in child.findall("./note"):  # For each note
            if c.findall("./pitch"):  # If note is a note
                # Find absolute pitch value from octave and note name
                pitch: int = int(handleXML(c.findall("./pitch/octave")[0].text)) * 12 - 8 \
                    + noteShift[handleXML(c.findall("./pitch/step")[0].text)]
                sign: str = "none"
                if c.findall("./accidental"):  # Check for accidental
                    sign = handleXML(c.findall("./accidental")[0].text)
                if c.findall("./pitch/alter"):  # Check for pitch shift
                    pitch += int(handleXML(c.findall("./pitch/alter")[0].text))
                length: str = handleXML(c.findall("./type")[0].text)
                if c.findall("./dot"):  # Check for dotted note
                    length = "dotted " + length
                note = Note(length, pitch, sign)
                m.addNote(note)
            elif c.findall("./rest"):  # If note is a rest
                note = Rest(handleXML(c.findall("./type")[0].text))
                m.addNote(note)
        song.addMeasure(m)

    return song


song = parseFile('test1.musicxml')
song.write("song.brf")

# >allegretto,
