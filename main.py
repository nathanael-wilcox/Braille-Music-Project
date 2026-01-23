# Taken from Partitura Repository Starter code
#
#import partitura as pt
import xml.etree.ElementTree as ET
from map import sharpKeys, flatKeys, noteShift, Song, Measure

# tree = ET.parse('Dotted_test.musicxml')
# root = tree.getroot()

# firstMeasure = root.findall("./part/measure/attributes")[0]
# beat = int(firstMeasure.findall("./time/beats")[0].text)
# beatType = int(firstMeasure.findall("./time/beat-type")[0].text)
# accidentals = int(firstMeasure.findall("./key/fifths")[0].text)

# key = []

# if accidentals > 0:
#     i = 0
#     while i < abs(accidentals):
#         key.append(sharpKeys[i])
#         i += 1
# elif accidentals < 0:
#     i = 0
#     while i < abs(accidentals):
#         key.append(flatKeys[i])
#         i += 1

# song = Song(key, [beat, beatType], [])

# for child in root.findall("./part/measure"):
#     m = Measure(child.attrib["number"], [])
#     for c in child.findall("./note"):
#         if c.findall("./pitch"):
#             pitch = int(c.findall("./pitch/octave")[0].text) * 12 - 8 + noteShift[c.findall("./pitch/step")[0].text]
#             sign = "none"
#             if c.findall("./accidental"):
#                 sign = c.findall("./accidental")[0].text
#             if c.findall("./pitch/alter"):
#                 pitch += int(c.findall("./pitch/alter")[0].text)
#             length = c.findall("./type")[0].text
#             if c.findall("./dot"):
#                 length = "dotted " + length
#             note = {"type": "note", "length": length, "note": pitch, "sign": sign}
#             m.addNote(note)
#         elif c.findall("./rest"):
#             note = {"type": "rest", "length": c.findall("./type")[0].text}
#             m.addNote(note)
#     song.addMeasure(m)

# song.print()

#from map import Song
#from map import Measure

#Example = "Example_score.musicxml"
#score = pt.load_score(Example)

#part = score.parts[0]
#print(part.pretty())

#note_array = part.note_array()

#print(note_array)

#pt.render(part)
