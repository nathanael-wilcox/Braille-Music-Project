import cadquery as cq

th = 1.2
padding = 0.5
dia = 1.6
a = 2.5
l = 6.0
e = 10
dr = 0.8
dh = 0.6
r = 0.6
pad = 4

dotValues = [(-a, -a/2), (0, -a/2), (a, -a/2),
             (-a, a/2), (0, a/2), (a, a/2)]
chars = ["126", "126", "3456", "14", "256"]
points = []

plate = (cq.Workplane("XY")
         .box(2 * a + dia + pad, len(chars) * a + (len(chars) - 1) * (l - a) + dia + pad, th)
         .edges("|Z")
         .fillet(r)
         )

for i in range(0, len(chars)):
    for c in chars[i]:
        dv = list(dotValues[int(c)-1])
        dv[1] += i*l
        points.append(tuple(dv))

result = (cq.Workplane("XY")
          .pushPoints(points)
          .sphere(dr)
          .translate((0, (-l * (len(chars) - 1))/2, th/2 - (dr - dh)))
          .split(True, False)
          .union(plate)
          )

cq.exporters.export(result, "result.stl")
