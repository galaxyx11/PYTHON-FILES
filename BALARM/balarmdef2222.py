# Burgular alarm with camera / pir sensor and lcd screen
# when motion detected take a picture sound alarm and log to
# a file with time and date. echo details to lcd screen
# tedh @galaxysoft.co.uk (C) 2025

import time, libcamera
from time import sleep
from picamera2 import Picamera2, Preview
from picamera2.encoders import H264Encoder
from gpiozero import MotionSensor,LED,Buzzer
from datetime import datetime
import os
import drivers



# setup gpio pins  / lcd on 12c
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

display = drivers.Lcd() #setup lcd drivers


def myclear(): # Function to clear terminal screen
    for i in range (1,40):
        print("\n")


####### create camera config for still picture ########
def takepic():
	picam = Picamera2() # set camera as picam
	picam.set_logging(picam.INFO) # log pic info. ie debug\info\warn\error\fatal
	config = picam.create_preview_configuration(main={"size": (800, 600)}) #pic size
	config["transform"] = libcamera.Transform(hflip=0, vflip=1) # h and v flip 0 or 1
	picam.configure(config)
	# start a preview
	picam.start_preview(Preview.QTGL,x=1000, y=200, width=800, height=600) # preview window placement with gui
	# take a picture using the current config
	picam.start()
	sleep(2)
	picam.capture_file("test-python2.jpg")
	picam.close()


##### create config for video #######
def takevid():
	picam = Picamera2() # set camera as picam
	video_config = picam.create_video_configuration()
	video_config["transform"] = libcamera.Transform(hflip=0, vflip=1) # h and v flip 0 or 1
	picam.configure(video_config)
	encoder = H264Encoder(10000000)
	# record using current config
	picam.start_preview(True,x=1000, y=200, width=800, height=600)
	picam.start_recording(encoder, 'tedstest.h264')
	sleep(8)
	picam.stop_preview()
	picam.stop_recording()
	picam.close()
	
	########### get pir detection ############
def run_detector():
	
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
		print("       ",dt)
		buzzer.on()
		red.on()
		takepic()
		sleep(1)
		buzzer.off()
		takevid()
		sleep(1)
		myclear()
	
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
		print("\033[H")
		mypicfile = open("pirlog.txt", "r")
		picdata = mypicfile.read()
		#print(picdata)   
		mypicfile.close()
		print(redb,"    WARNING MOTION DETECTED       ",whitblac,whitblac,"\n")
		print("       ",line_count,"LINES IN LOG FILE") # get num of lines in log
		print(" SIZE OF LOG FILE IS --- " , os.path.getsize("pirlog.txt"),"Bytes\n") # get size of log
		print(redb,"    WARNING MOTION DETECTED       ",whitblac,whitblac,"\n")

        
        
def load_lcd():
	# Remember 1602 sentences 16 characters 2004 20 charachters long!
      dt = datetime.now().replace(microsecond=0)
      display.lcd_clear()
      display.lcd_display_string("  MOTION  DETECTED", 1)  # Write line of text to first line of display
      display.lcd_display_string("  DETAILS  LOGGED", 2)  # Write line of text to second line of display
      display.lcd_display_string("  PICTURE   TAKEN",3) # 3rd line for lcd 2004      
      display.lcd_display_string(str(dt),4) # 4th line 
      sleep (8)
      display.lcd_clear()  


# Main Loop

while True:
	run_detector()
	load_lcd()

	

	


