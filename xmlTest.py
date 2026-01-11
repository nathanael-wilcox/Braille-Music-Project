import xml.etree.ElementTree as ET

tree = ET.parse('test1.musicxml')
root = tree.getroot()

print(root)