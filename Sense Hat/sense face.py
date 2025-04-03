# random pixel colour sense hat prog

from sense_emu import SenseHat
from time import sleep
from random import randint

sense = SenseHat()
sense.clear()


while True:
    
#eye right
    x = randint(5,7)
    y = randint(0,2)
    c1 = randint(0,255)
    c2 = randint(0,255)
    c3 = randint(0,255)
    sense.set_pixel(x,y,c1,c2,c3)

# eye left  
    x = randint(0,2)
    y = randint(0,2)
    c1 = randint(0,255)
    c2 = randint(0,255)
    c3 = randint(0,255)
    sense.set_pixel(x,y,c1,c2,c3)
    
# nose
    c1 = randint(0,255)
    c2 = randint(0,255)
    c3 = randint(0,255)
    sense.set_pixel(3,4,c1,c2,c3)
    sense.set_pixel(4,4,c1,c2,c3)    
    
# mouth
    c1 = randint(0,255)
    c2 = randint(0,255)
    c3 = randint(0,255)
    sense.set_pixel(2,7,c1,c2,c3)
    sense.set_pixel(3,7,c1,c2,c3)
    sense.set_pixel(4,7,c1,c2,c3)
    sense.set_pixel(5,7,c1,c2,c3)
    sense.set_pixel(1,6,c1,c2,c3)
    sense.set_pixel(6,6,c1,c2,c3)
    
# eye centre off
    sense.set_pixel(1,1,0,0,0)
    sense.set_pixel(6,1,0,0,0)
    sleep(0.2)
    
    
    
    