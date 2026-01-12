# Taken from Partitura Repository Starter code
#
import partitura as pt

from map import Song
from map import Measure

Example = "Example_score.musicxml"
score = pt.load_score(Example)

part = score.parts[0]
print(part.pretty())

note_array = part.note_array()

print(note_array)
