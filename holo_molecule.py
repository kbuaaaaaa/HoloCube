from __future__ import absolute_import, division, print_function, unicode_literals
from math import sin, cos, radians
from time import time
import random
import demo
import pi3d
import json

DISPLAY = pi3d.Display.create(w=800, h=480, background=(0.0, 0.0, 0.0, 1.0))

CAMERA = pi3d.Camera()

scaleDownFactor = 6
scaleDownFactorAtom = 5

with open('models/Structure3D_CID_16500.json','r') as f:
  json_data = json.load(f)['PC_Compounds'][0]
element = json_data['atoms']['element']
x = json_data['coords'][0]['conformers'][0]['x']
y = json_data['coords'][0]['conformers'][0]['y']
z = json_data['coords'][0]['conformers'][0]['z']
n = len(element)
atoms = {1:['hydrogen', 0.5/scaleDownFactorAtom, (1.0, 0.0, 0.0)],
         6:['carbon', 0.8/scaleDownFactorAtom, (0.1, 0.1, 0.1)],
         7:['nitrogen', 0.9/scaleDownFactorAtom, (0.1, 0.9, 1.0)],
         8:['oxygen', 0.9/scaleDownFactorAtom, (1.0, 1.0, 1.0)],
         15:['phosphorus', 1.5/scaleDownFactorAtom, (1.0, 0.0, 1.0)]}

shape1 = pi3d.Sphere(radius=atoms[6][1], y=2.5)

empty = pi3d.Triangle(corners=((-0.01, 10.0), (0.0, 0.01), (0.01, 0.0)), z=10.0)

elem = {}

for e in atoms:
  if e != 6: 
    shape1 = pi3d.Sphere(radius=atoms[e][1])
    elem[e] = pi3d.MergeShape()
    
    for i in range(n):
      if element[i] == e:
        elem[e].add(shape1, x[i]/scaleDownFactor, y[i]/scaleDownFactor, z[i]/scaleDownFactor)
    elem[e].set_material(atoms[e][2])
    elem[e].positionY(2.0)
    empty.add_child(elem[e])

keys = pi3d.Keyboard()
mouse = pi3d.Mouse(restrict=False)
mouse.start()

views = ((0.0, 0.0), 
         (-90.0, 90.0), 
         (90.0, -90), 
         (180.0, 180.0))
         
while DISPLAY.loop_running():
  
  mx, my = mouse.position()

  rot = - mx * 0.2
  tilt = my * 0.2
  
  for e in atoms:
    if e != 6:
		elem[e].rotateToY(rot)
		elem[e].rotateToX(tilt)
  
  for v in views:
    empty.rotateToY(v[0])
    empty.rotateToZ(v[1])
    empty.draw()

  if keys.read() == 27:
    break
