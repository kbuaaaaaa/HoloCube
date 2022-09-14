#!/usr/bin/env python
import skywriter
import signal
import autopy
import uinput
import time
some_value = 0

mouse = uinput.Device([uinput.REL_X, uinput.REL_Y, uinput.BTN_LEFT])
x = 0
y = 0
@skywriter.move()
def move(x, y, z):
  x = (x) * 8
  y = (y) * 8

  x = int(x)
  y = int(y)

  mouse.emit(uinput.REL_X, x)
  mouse.emit(uinput.REL_Y, y)
  time.sleep(0.01)

signal.pause()
