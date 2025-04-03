# Show clock time and date on sense hat
# Ted Hensman @ Galaxysoft (C) 2025


# IMPORT the required libraries (sense_hat, time) 
from sense_hat import SenseHat
from time import sleep
from time import gmtime, strftime
from datetime import date
import datetime

# CREATE a sense object
sense = SenseHat()

#get current date and time
x = datetime.datetime.now()

#convert date and time to string for sense hat to scroll
dateTimeStr = str(x)
#dateTimeStr = dateTimeStr[:10]  will determine how many charachters to display

#format string to day/month/year a=day string d=day m=month y=year /or in capitals ADMY
dateTimeStr = strftime("%a %d %m")  

#scroll time on sense hat
while True:
        sense.show_message(dateTimeStr, scroll_speed = 0.1, text_colour=(255, 255, 255), back_colour=(0,0,255))
        sense.show_message(strftime('%H:%M', gmtime()), scroll_speed= 0.1, text_colour=(255, 255, 255), back_colour=(0,0,255))
    