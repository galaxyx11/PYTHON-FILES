from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

w = (255, 250, 250)
b = (255, 0, 0)
e = (0, 0, 0)

image = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
w,w,w,e,e,w,w,w,
w,w,b,e,e,w,w,b,
w,w,w,e,e,w,w,w,
e,e,e,e,e,e,e,e,
e,e,w,w,w,w,e,e,
e,e,e,w,w,e,e,e
]

sense.set_pixels(image)

# flip the orintation of the matrix either h horizontal or v vertical
while True:
    sleep(1)
    sense.flip_h()