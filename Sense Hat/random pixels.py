# Move random pixels on sense hat
# Random colours and placement

from sense_emu import SenseHat
from time import sleep
from random import randint
sense = SenseHat()

while True:
    x = randint(0,7)
    y = randint(0,7)
    c1 = randint(0,255)
    c2 = randint(0,255)
    c3 = randint(0,255)
    sense.set_pixel(x,y,c1,c2,c3)
