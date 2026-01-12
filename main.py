# Taken from Partitura Repository Starter code
#
#import partitura as pt
import xml.etree.ElementTree as ET

tree = ET.parse('Dotted_test.musicxml')
root = tree.getroot()

for child in root.findall("./part/measure"):
    print(child.tag, child.attrib["number"])
    for c in child.findall("./note"):
        print(c.findall("./type")[0].text, c.findall("./pitch/step")[0].text)
        if c.findall("./accidental"):
            print(c.findall("./accidental")[0].text)
    if child.findall("./barline"):
        print("barline")

#from map import Song
#from map import Measure

#Example = "Example_score.musicxml"
#score = pt.load_score(Example)

#part = score.parts[0]
#print(part.pretty())

#note_array = part.note_array()

#print(note_array)

#pt.render(part)
