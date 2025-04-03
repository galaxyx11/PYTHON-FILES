# simple ball and bat

from sense_emu import SenseHat
from time import sleep
from random import randint
import struct
import sys

sense = SenseHat()
sense.clear()

bc = (255,0,0) # ball colour red
bat = (0,255,0) #bat colour green
tc = (0,0,0)   # back colour blank
bpx = 7  # bat x pos
bpy = 2	 # bat y pos

while True:

# new_ball position (y = random column)
    y = randint(0,7)

# set ball position and update (x = row)
    for x in range (0,8):
        sense.set_pixel(y,x,bc)
        sleep(0.1)
        sense.set_pixel(y,x,tc)
    
# set bat position and update
        sense.set_pixel(bpy,bpx,bat)
        sense.set_pixel(bpy+1,bpx,bat)
        sense.set_pixel(bpy+2,bpx,bat)
        sleep(0.1)
           
        if bpy <=0:
            bpy = bpy =+1
        if bpy >=7:
            bpy = bpy =-1
        else:
            bpy == bpy +1
            
        sense.set_pixel(bpy,bpx,tc)
        sense.set_pixel(bpy+1,bpx,tc)
        sense.set_pixel(bpy+2,bpx,tc)


    

    
    
    