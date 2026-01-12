import xml.etree.ElementTree as ET

asciiTable = {
    "": "\u2800",
    "1": "\u2801",
    "2": "\u2802",
    "12": "\u2803",
    "3": "\u2804",
    "13": "\u2805",
    "23": "\u2806",
    "123": "\u2807",
    "4": "\u2808",
    "14": "\u2809",
    "24": "\u280a",
    "124": "\u280b",
    "34": "\u280c",
    "134": "\u280d",
    "234": "\u280e",
    "1234": "\u280f",
    "5": "\u2810",
    "15": "\u2811",
    "25": "\u2812",
    "125": "\u2813",
    "35": "\u2814",
    "135": "\u2815",
    "235": "\u2816",
    "1235": "\u2817",
    "45": "\u2818",
    "145": "\u2819",
    "245": "\u281a",
    "1245": "\u281b",
    "345": "\u281c",
    "1345": "\u281d",
    "2345": "\u281e",
    "12345": "\u281f",
    "6": "\u2820",
    "16": "\u2821",
    "26": "\u2822",
    "126": "\u2823",
    "36": "\u2824",
    "136": "\u2825",
    "236": "\u2826",
    "1236": "\u2827",
    "46": "\u2828",
    "146": "\u2829",
    "246": "\u282a",
    "1246": "\u282b",
    "346": "\u282c",
    "1346": "\u282d",
    "2346": "\u282e",
    "12346": "\u282f",
    "56": "\u2830",
    "156": "\u2831",
    "256": "\u2832",
    "1256": "\u2833",
    "356": "\u2834",
    "1356": "\u2835",
    "2356": "\u2836",
    "12356": "\u2837",
    "456": "\u2838",
    "1456": "\u2839",
    "2456": "\u283a",
    "12456": "\u283b",
    "3456": "\u283c",
    "13456": "\u283d",
    "23456": "\u283e",
    "123456": "\u283f",
}

charTable = {
    "": " ",
    "1": "a",
    "2": "1",
    "12": "b",
    "3": "'",
    "13": "k",
    "23": "2",
    "123": "l",
    "4": "@",
    "14": "c",
    "24": "i",
    "124": "f",
    "34": "/",
    "134": "m",
    "234": "s",
    "1234": "p",
    "5": "\"",
    "15": "e",
    "25": "3",
    "125": "h",
    "35": "9",
    "135": "o",
    "235": "6",
    "1235": "r",
    "45": "^",
    "145": "d",
    "245": "j",
    "1245": "g",
    "345": ">",
    "1345": "n",
    "2345": "t",
    "12345": "q",
    "6": ",",
    "16": "*",
    "26": "5",
    "126": "<",
    "36": "-",
    "136": "u",
    "236": "8",
    "1236": "v",
    "46": ".",
    "146": "%",
    "246": "[",
    "1246": "$",
    "346": "+",
    "1346": "x",
    "2346": "!",
    "12346": "&",
    "56": ";",
    "156": ":",
    "256": "4",
    "1256": "\\",
    "356": "0",
    "1356": "z",
    "2356": "7",
    "12356": "(",
    "456": "_",
    "1456": "?",
    "2456": "w",
    "12456": "]",
    "3456": "#",
    "13456": "y",
    "23456": ")",
    "123456": "=",
}

numbers = {
    0: "245",
    1: "1",
    2: "12",
    3: "14",
    4: "145",
    5: "15",
    6: "124",
    7: "1245",
    8: "125",
    9: "24"
}

dict = {
    "a": "1",
    "b": "12",
    "c": "14",
    "d": "145",
    "e": "15",
    "f": "124",
    "g": "1245",
    "h": "125",
    "i": "24",
    "j": "245",
    "k": "13",
    "l": "123",
    "m": "134",
    "n": "1345",
    "o": "135",
    "p": "1234",
    "q": "12345",
    "r": "1235",
    "s": "234",
    "t": "2345",
    "u": "136",
    "v": "1236",
    "w": "2456",
    "x": "1346",
    "y": "13456",
    "z": "1356",
}

punc = {
    ",": "2",
    ";": "23",
    ":": "25",
    ".": "256",
    "?": "236",
    "!": "235",
}

symbols = {
    "number": "3456",
    "sharp": "146",
    "flat": "126",
    "natural": "16",
    "db": "126 13",  # double bar
    "sdb": "126 13 3",  # sectional double bar
    "er": "1346",  # eighth rest
    "qr": "1236",  # quarter rest
    "hr": "136",  # half rest
    "wr": "134",  # whole rest
    "dot": "3"
}

notes = {
    0: "145",
    2: "15",
    4: "124",
    5: "1245",
    7: "125",
    9: "24",
    11: "245",
}

lengths = {
    "eighth": "",
    "quarter": "6",
    "half": "3",
    "whole": "36"
}

octaves = {
    0: "4 4",
    1: "4",
    2: "45",
    3: "456",
    4: "5",
    5: "46",
    6: "56",
    7: "6",
    8: "6 6"
}

noteShift = {
    "C": 0,
    "D": 2,
    "E": 4,
    "F": 5,
    "G": 7,
    "A": 9,
    "B": 11
}

flatKeys = [
    {"type": "flat", "note": 10},
    {"type": "flat", "note": 3},
    {"type": "flat", "note": 8},
    {"type": "flat", "note": 1},
    {"type": "flat", "note": 6},
    {"type": "flat", "note": 11},
    {"type": "flat", "note": 4}
]

sharpKeys = [
    {"type": "sharp", "note": 6},
    {"type": "sharp", "note": 1},
    {"type": "sharp", "note": 8},
    {"type": "sharp", "note": 3},
    {"type": "sharp", "note": 10},
    {"type": "sharp", "note": 5},
    {"type": "sharp", "note": 0}
]

def shiftDown(code):
    newCode = ""
    for c in code:
        newCode += str(int(c) + 1)
    return newCode


def printBraille(s):
    isNumber = False
    isSpace = False
    for c in s:
        if c in dict:
            if isNumber and not isSpace:
                print(asciiTable["56"], end="")
            print(asciiTable[dict[c]], end="")
            isNumber = False
            isSpace = False
        elif c in punc:
            print(asciiTable[punc[c]], end="")
        elif c.isdigit() and int(c) in numbers:
            if not isNumber:
                print(asciiTable[symbols["number"]], end="")
            print(asciiTable[numbers[int(c)]], end="")
            isNumber = True
            isSpace = False
        elif c == " ":
            print(c, end="")
            isNumber = False
            isSpace = True
    print()


def printMult(s):
    arr = s.split()
    for c in arr:
        print(asciiTable[c], end="")


def makeNote(name, length):
    nameArr = list(notes[name]) + list(lengths[length])
    nameArr.sort()
    return "".join(nameArr)


def printSymbol(dict, value):
    printMult(dict[value])


def printNumber(num):
    printSymbol(symbols, "number")
    for c in num:
        printSymbol(numbers, int(c))


def printNote(note, length, key):
    for k in key:
        if (note + 8) % 12 == k["note"]:
            if k["type"] == "flat":
                note += 1
            elif k["type"] == "sharp":
                note -= 1
    print(asciiTable[makeNote((note + 8) % 12, length)], end="")


class Song:
    def __init__(self, key, time, measures):
        self.key = key
        self.time = time
        self.measures = measures
        self.measureSize = 8

    def addMeasure(self, measure):
        self.measures.append(measure)

    def print(self):
        for k in self.key:
            printSymbol(symbols, k["type"])
        printSymbol(symbols, "number")
        printSymbol(numbers, self.time[0])
        print(asciiTable[shiftDown(numbers[self.time[1]])], end="")
        print()
        i = 0
        lastNote = -1
        for m in self.measures:
            lastNote = m.print(i % self.measureSize == 0, lastNote, self.key)
            if not i % self.measureSize == self.measureSize - 1 and not i == len(self.measures) - 1:
                print("   ", end="")
            elif i % self.measureSize == self.measureSize - 1 and not i == len(self.measures) - 1:
                print()
            i += 1

        printSymbol(symbols, "db")
        print()


class Measure:
    def __init__(self, number, data):
        self.number = number
        self.data = data

    def addNote(self, note):
        self.data.append(note)

    def print(self, printMeasure, lastNote, key):
        if printMeasure:
            printNumber(self.number)
            print("   ", end="")
        for d in self.data:
            length = d["length"]
            if d["type"] == "rest":
                if len(length.split()) == 1:
                    printSymbol(symbols, length[0] + "r")
                elif length.split()[0] == "dotted":
                    printSymbol(symbols, length.split()[1][0] + "r")
                    printSymbol(symbols, "dot")
            if (d["type"] == "note"):
                note = d["note"]
                if lastNote < 0 or abs(note - lastNote) > 8:
                    printSymbol(octaves, (note + 8) // 12)
                elif abs(note - lastNote) > 4:
                    if not (note + 8) // 12 == (lastNote + 8) // 12:
                        printSymbol(octaves, (note + 8) // 12)

                if not d["sign"] == "none":
                    if d["sign"] == "natural":
                        key = [k for k in key if k.get("note") != d["note"]]
                        printSymbol(symbols, d["sign"])
                    else:
                        key.append(
                            {"type": d["sign"], "note": (d["note"] + 8) % 12})
                        printSymbol(symbols, d["sign"])

                if len(length.split()) == 1:
                    printNote(note, length, key)
                elif length.split()[0] == "dotted":
                    printNote(note, length.split()[1], key)
                    printSymbol(symbols, "dot")

                lastNote = note
        return lastNote


m1 = Measure("1", [{"type": "rest", "length": "half"}, {
             "type": "note", "length": "quarter", "note": 30, "sign": "none"}])
m2 = Measure("2", [{"type": "note", "length": "half", "note": 38, "sign": "none"}, {
    "type": "note", "length": "quarter", "note": 35, "sign": "none"}])
m3 = Measure("3", [{"type": "note", "length": "dotted quarter", "note": 35, "sign": "none"}, {
    "type": "note", "length": "eighth", "note": 34, "sign": "sharp"}, {
    "type": "note", "length": "quarter", "note": 35, "sign": "none"},])
m4 = Measure("4", [{"type": "note", "length": "half", "note": 37, "sign": "none"}, {
    "type": "note", "length": "quarter", "note": 34, "sign": "sharp"}])
m5 = Measure("5", [{"type": "note", "length": "half", "note": 30, "sign": "none"}, {
    "type": "rest", "length": "quarter"}])

song = Song([{"type": "flat", "note": 10}, {
            "type": "flat", "note": 3}], [3, 4], [m1, m2, m3, m4, m5])
song.print()


# m21 = Measure("1", [
#     {"type": "note", "length": "half", "note": 52, "sign": "none"},
# ])
# m22 = Measure("2", [
#     {"type": "note", "length": "quarter", "note": 51, "sign": "natural"},
#     {"type": "note", "length": "quarter", "note": 50, "sign": "flat"},
# ])
# m23 = Measure("3", [
#     {"type": "note", "length": "half", "note": 49, "sign": "none"},
# ])
# m24 = Measure("4", [
#     {"type": "note", "length": "eighth", "note": 40, "sign": "none"},
#     {"type": "note", "length": "eighth", "note": 45, "sign": "none"},
#     {"type": "note", "length": "eighth", "note": 49, "sign": "none"},
#     {"type": "note", "length": "eighth", "note": 52, "sign": "none"}
# ])
# m25 = Measure("5", [
#     {"type": "note", "length": "half", "note": 52, "sign": "none"},
# ])
# m26 = Measure("6", [
#     {"type": "note", "length": "quarter", "note": 51, "sign": "natural"},
#     {"type": "note", "length": "quarter", "note": 52, "sign": "none"},
# ])
# m27 = Measure("7", [
#     {"type": "note", "length": "half", "note": 54, "sign": "none"},
# ])
# m28 = Measure("8", [
#     {"type": "note", "length": "half", "note": 49, "sign": "none"},
# ])

# song2 = Song([{"type": "flat", "note": 10}], [2, 4], [
#              m21, m22, m23, m24, m25, m26, m27, m28])
# song2.print()


tree = ET.parse('test2.musicxml')
root = tree.getroot()

firstMeasure = root.findall("./part/measure/attributes")[0]
beat = int(firstMeasure.findall("./time/beats")[0].text)
beatType = int(firstMeasure.findall("./time/beat-type")[0].text)
accidentals = int(firstMeasure.findall("./key/fifths")[0].text)

key = []

if accidentals > 0:
    i = 0
    while i < abs(accidentals):
        key.append(sharpKeys[i])
        i += 1
elif accidentals < 0:
    i = 0
    while i < abs(accidentals):
        key.append(flatKeys[i])
        i += 1

song = Song(key, [beat, beatType], [])

for child in root.findall("./part/measure"):
    m = Measure(child.attrib["number"], [])
    for c in child.findall("./note"):
        if c.findall("./pitch"):
            pitch = int(c.findall("./pitch/octave")[0].text) * 12 - 8 + noteShift[c.findall("./pitch/step")[0].text]
            sign = "none"
            if c.findall("./accidental"):
                sign = c.findall("./accidental")[0].text
            if c.findall("./pitch/alter"):
                pitch += int(c.findall("./pitch/alter")[0].text)
            length = c.findall("./type")[0].text
            if c.findall("./dot"):
                length = "dotted " + length
            note = {"type": "note", "length": length, "note": pitch, "sign": sign}
            m.addNote(note)
        elif c.findall("./rest"):
            note = {"type": "rest", "length": c.findall("./type")[0].text}
            m.addNote(note)
    song.addMeasure(m)

song.print()