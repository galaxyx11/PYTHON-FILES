
from sense_emu import SenseHat
from time import sleep
import random
sense = SenseHat()

e = (0,0,0)
r = (255,0,0)
sense.clear(e)

a = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,r,e,e,e,e,e,e,
r,e,r,e,e,e,e,e,
r,r,r,e,e,e,e,e,
r,e,r,e,e,e,e,e
]

b = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
r,e,e,e,e,e,e,e,
r,r,r,e,e,e,e,e,
r,e,r,e,e,e,e,e,
r,r,r,e,e,e,e,e
]

c = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,r,r,e,e,e,e,e,
r,e,e,e,e,e,e,e,
r,e,e,e,e,e,e,e,
e,r,r,e,e,e,e,e
]

for x in range(8):
    for t in range(5):
        sense.set_pixel(x,t,r)
sleep(1)
