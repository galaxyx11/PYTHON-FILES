from time import gmtime, strftime
from random import randint
from sense_emu import SenseHat
sense = SenseHat()
sense.clear()
def hilo(a, b, c):
    if c < b: b, c = c, b
    if b < a: a, b = b, a
    if c < b: b, c = c, b
    return a + c
def complement(r, g, b):
    k = hilo(r, g, b)
    return tuple(k - u for u in (r, g, b))
while True:
    r=randint(0, 255)
    g=randint(0, 255)
    b=randint(0, 255)
    while True:
        x, y, z = sense.get_accelerometer_raw().values()
        x = abs(x)
        y = abs(y)
        z = abs(z)
        sense.show_message(strftime('%H:%M', gmtime()), scroll_speed= 0.1, text_colour=[255, 255, 255], back_colour=(0,0,0))
        if x > 2 or y > 2 or z > 2 :
            break
    else:
         continue