# Program to take video and pics with picamera2
# and output details on 2004 lcd (C)Galaxysoft 2025

from time import sleep
import os
from datetime import datetime
from picamera2 import Picamera2 ,Preview
import drivers # lcd drivers folder/needs to be in same directory

def clearme(): # Function to clear terminal screen
    for cle in range (1,20):
        print("\n")
    
# Initilize camera
picam2 = Picamera2()
camera_config = picam2.create_preview_configuration()
picam2.configure(camera_config)
picam2.start_preview(Preview.QTGL)

# Take a picture
picam2.start_and_capture_file("/home/galaxy/Desktop/test.jpg")
sleep(2)

# Take a 5 second video
picam2.start_and_record_video("/home/galaxy/Desktop/test.mp4", duration=5)
picam2.stop_preview()       #stop and close preview window
#picam2.start_preview(True) #start and open preview window
sleep(2)

# Display details on 2004/1602 lcd / 2 or 4 lines remember!!
display = drivers.Lcd()
display.lcd_clear()
display.lcd_display_string("JPEG PIC  TAKEN ", 1) # Write to lcd line1
display.lcd_display_string("MP4 VIDEO TAKEN ", 2) # Write to lcd line2
display.lcd_display_string("DATE " + str(datetime.now().date()), 3) # Write date to line 3
display.lcd_display_string("TIME " + str(datetime.now().time()), 4)# Write time to line 4  
sleep(10)
display.lcd_clear()

# Log details of times and date to a file
clearme()
date1 = str(datetime.now().date())
time1 = str(datetime.now().time())
mypicfile = open("picslog.txt", "a") # Append log to existing file
mypicfile.write("JPEG & MP4 LOGGED AT " + date1 + "  " + time1 + "\n")
mypicfile.close()

# Count number of lines in log file
with open("picslog.txt") as f:
    line_count = 0
    for line in f:
        line_count += 1
        
# Echo log file data to screen
mypicfile = open("picslog.txt", "r")
picdata = mypicfile.read()
print(picdata)   
mypicfile.close()

# Print Time & date & Length/Size of log details to screen
print("\033[0;37;44m") # White on blue background see textcol.py?
print ("\n" "   CAMERA DATA LOGGED AT" + "\n" + date1 + "   " + time1)
sleep(2)
print("\n Number of Lines in Log File = " , line_count) # Get num of lines and byte size of file
print(" Size of Log File is --- " , os.path.getsize("picslog.txt"),"Bytes")
sleep(5)

# Close Program and echo Goodbye on lcd and terminal
display.lcd_display_string("NEXT PIC IN 15 MINS", 1)
display.lcd_display_string("*** CLEANING UP ***", 3)
display.lcd_display_string("***** GOODBYE *****", 4)
print("\n" + "       NEXT SEQUENCE OF PICS IN 15 MINUTES" + "\n")
print("******************* GOODBYE ******************")
sleep(10)
display.lcd_clear()
quit()


