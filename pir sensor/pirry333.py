# MOVEMENT DETECTOR USING PIR SENSOR

from time import sleep
from gpiozero import MotionSensor,LED,Buzzer
from datetime import datetime
import os

# setup gpio pins
pir = MotionSensor(25)
buzzer = Buzzer(17)
red = LED(18)
blue = LED(24)

# define ansi colours
yellb = ("\033[48;5;220m")
redb = ("\033[48;5;161m")
blackt =("\033[38;5;16m")
bluet = ("\033[38;5;21m")
whitblac = ("\033[1;37;40m")


def myclear(): # Function to clear terminal screen
    for i in range (1,40):
        print("\n")
      

while True:
	myclear()
	print("\033[H")
	print ("\033[?25l") # hide cursor
	# print ("\033[?25h") # bring cursor back
	
	
	# wait for detection
	print (yellb,bluet,"  WAITING FOR SENSOR DETECTION   ",whitblac, "\n")
	blue.on()
	red.off()
	pir.wait_for_motion()
	blue.off()
	currentstate = pir.motion_detected
	
	# if motion detected
	myclear()
	print("\033[H")
	dt = datetime.now().replace(microsecond=0)
	print(redb,"    WARNING MOTION DETECTED       ",whitblac,whitblac,"\n")
	print("       ",dt)
	buzzer.on()
	red.on()
	sleep(1)
	buzzer.off()
	
	# Log details of times and date to a file
	date1 = str(datetime.now().date())
	time1 = str(datetime.now().time())
	mypicfile = open("pirlog.txt", "a") # Append log to existing file
	mypicfile.write("PIR SENSOR WARNING LOGGED AT " + date1 + "  " + time1 + "\n")
	mypicfile.close()

	# Count number of lines in log file
	with open("pirlog.txt") as f:
		line_count = 0
		for line in f:
			line_count += 1
        
	# Echo log file data to screen
	mypicfile = open("pirlog.txt", "r")
	picdata = mypicfile.read()
	#print(picdata)   
	mypicfile.close()
	print("       ",line_count,"LINES IN LOG FILE") 
	print(" SIZE OF LOG FILE IS --- " , os.path.getsize("pirlog.txt"),"Bytes\n")
	print(redb,"    WARNING MOTION DETECTED       ",whitblac,whitblac,"\n")
	sleep(8)

