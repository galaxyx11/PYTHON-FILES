# Show random 6 sided dice on sense hat

# IMPORT the required libraries (sense_hat, time ,random)
from random import randint
from sense_emu import SenseHat

# CREATE a sense object
sense = SenseHat()

# Set up the colours
f = (255, 0, 0) # foreground text
b = (0, 0, 255) # background text

 
while True :
    input("                   PRESS ENTER KEY TO ROLL DICE   Cntr/c TO QUIT")
    roll = randint(1,6)
    sense.show_letter(str(roll),f,b) #string,fg,bg colours
    
       