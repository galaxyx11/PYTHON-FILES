# MOVEMENT DETECTOR USING PIR SENSOR

from time import sleep
from gpiozero import MotionSensor,LED,Buzzer
from datetime import datetime

pir = MotionSensor(17)
buzzer = Buzzer(22)
red = LED(18)
blue = LED(24)

# define ansi colours
yellb = ("\033[48;5;220m")
redb = ("\033[48;5;161m")
greyb = ("\033[48;5;246m")
greenb =("\033[48;5;190m")
violetb =("\033[48;5;165m")
blackt =("\033[38;5;16m")
bluet = ("\033[38;5;21m")
whitblac = ("\033[1;37;40m")
blacwhit = ("\033[1;30;47m")

while True:
	# wait for detection
	print (yellb,bluet," WAITING FOR SENSOR DETECTION  \n")
	blue.on()
	pir.wait_for_motion()
	blue.off()
	currentstate = pir.motion_detected
	
	# if motion detected
	print(redb,whitblac,"    WARNING MOTION DETECTED AT   ",datetime.now().time(),whitblac,"\n")
	buzzer.on()
	red.on()
	sleep(1)
	buzzer.off()
	red.off()
	sleep(2)
