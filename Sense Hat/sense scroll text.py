#python to random generate hat colours
#and scroll text in any colour and background


from sense_emu import SenseHat
from time import sleep
import random

sense = SenseHat()
t = 0
while t < 20 :
    r = (random.randrange(1,255))
    g = (random.randrange(1,255))
    b = (random.randrange(1,255))
    sense.clear((r,g,b))
    sleep(.3)
    t = t + 1
    
# python to scroll message
sense.show_letter("T",back_colour=(255, 0, 0),text_colour=(0, 255, 0))
sense.show_message("TEDDY IS AMAZING AT PROGRAMMING.",back_colour=(0, 0, 0),text_colour=(255, 255, 255))

