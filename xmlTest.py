import xml.etree.ElementTree as ET

tree = ET.parse('test1.musicxml')
root = tree.getroot()

for child in root.findall("./part/measure"):
    print(child.tag, child.attrib["number"])
    for c in child.findall("./note"):
        print(c.findall("./type")[0].text, c.findall("./pitch/step")[0].text)
        if c.findall("./accidental"):
            print(c.findall("./accidental")[0].text)
    if child.findall("./barline"):
        print("barline")