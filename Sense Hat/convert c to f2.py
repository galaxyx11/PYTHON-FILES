# python to get temp and display in farenheit and centigrade
# (c) Ted Hensman 2025

from sense_hat import SenseHat
from time import sleep
sense = SenseHat()

while True:
    cent = round (sense.get_temperature()) #get temp in C
    fheit = round (cent * 1.8 + 32)        #convert cent to fheit F
    press = round(sense.get_pressure())   #get pressure in millibars
    humid = round(sense.get_humidity())   #get humidity in percentage
    speed = 0.06                          #set text scroll speed
    
    sense.show_message("Temperture is  %sC" % cent ,speed, text_colour=[255, 0, 0])
    sleep(2)
    sense.show_message("Temperture is  %sF" % fheit ,speed, text_colour=[255, 0, 255])
    sleep(2)
    sense.show_message("Pressure is %s Mbars" % press ,speed, text_colour=[0, 0, 255])
    sleep(2)
    sense.show_message("Humidity is %s Percent" % humid ,speed, text_colour=[0, 255, 0])
    sleep(2)