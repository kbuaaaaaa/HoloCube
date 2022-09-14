from __future__ import absolute_import, division, print_function, unicode_literals

from math import sin, cos, radians
from time import time
import random

import demo
import pi3d
import json

DISPLAY = pi3d.Display.create(w=1024, h=768, background=(0.0, 0.0, 0.0, 1.0))

CAMERA = pi3d.Camera()
shade = pi3d.Shader('uv_flat')
earthTex = [pi3d.Texture('earth.png')]
earth = pi3d.Sphere()
starsimg = pi3d.Texture('textures/stars2.jpg')
myplane = pi3d.Plane(w=50, h=50, name="stars", z=30)
flatsh = pi3d.Shader("uv_flat")


empty = pi3d.Triangle(corners=((-0.01, 10.0), (0.0, 0.01), (0.01, 0.0)), z=10.0)
earth.positionY(3.0)
empty.add_child(earth)

keys = pi3d.Keyboard()
mouse = pi3d.Mouse(restrict=False)
mouse.start()

views = ((0.0, 0.0), 
         (-90.0, 90.0), 
         (90.0, -90), 
         (180.0, 180.0))
         
while DISPLAY.loop_running():
  
  mx, my = mouse.position()

  rot = - mx * 0.1
  tilt = my * 0.1

  earth.rotateToY(rot)
  earth.rotateToX(tilt)

  for v in views:
    empty.rotateToY(v[0])
    empty.rotateToZ(v[1])
    empty.draw(shade,earthTex)

  if keys.read() == 27:
    break

