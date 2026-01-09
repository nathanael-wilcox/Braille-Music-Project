# Taken from Partitura Repository Starter code
#
import partitura as pt

Example = "FriendInMe.mid"
score = pt.load_score(Example)

part = score.parts[0]
print(part.pretty())

pt.render(part)

