import xml.etree.ElementTree as ET


def handleXML(input: str | None):
    output: str = ""
    if type(input) == str:
        output = input
    return output


def parseFile(file: str):
    tree = ET.parse(file)
    root = tree.getroot()

    for child in root.findall("./part/measure"):  # For each measure in XML
        print(type(child))
        print(child.tag)
        # for c in child:
        #     print(c.tag, c.attrib)
        # for c in child.findall("./note"):  # For each note
        #     if c.findall("./pitch"):  # If note is a note
        #         # Find absolute pitch value from octave and note name
        #         print(handleXML(c.findall("./pitch/step")[0].text), handleXML(c.findall("./pitch/octave")
        #               [0].text))
        #         if c.findall("./accidental"):  # Check for accidental
        #             print(handleXML(c.findall("./accidental")[0].text))
        #         if c.findall("./pitch/alter"):  # Check for pitch shift
        #             print(handleXML(c.findall("./pitch/alter")[0].text))
        #         length: str = handleXML(c.findall("./type")[0].text)
        #         if c.findall("./dot"):  # Check for dotted note
        #             length = "dotted " + length
        #         print(length)
        #     elif c.findall("./rest"):  # If note is a rest
        #         print(handleXML(c.findall("./type")[0].text))

    print(root.find("./part/measure"))

parseFile("test12.musicxml")
