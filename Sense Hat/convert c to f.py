# python to get temp and display in farenheit and centigrade
# (c) Ted Hensman 2025

from sense_hat import SenseHat
from time import sleep
sense = SenseHat()

while True:
    temp = round (sense.get_temperature())
    print("Temperature: %s C" % temp)
    fheit = round (temp * 1.8 + 32)
    print("Temperature: %s F" % fheit)
    sense.show_message("Temperture is %s Degree's C" % temp , text_colour=[255, 255, 255])
    sleep(2)
    sense.show_message("Temperture is %s Degree's F" % fheit , text_colour=[255, 255, 255])