# Run from venv
# example...  source dht11/env/bin/activate

import time
import adafruit_dht
import board

# define screen colours
red = "\033[1;37;41m"
white = "\033[1;37;40m"
green = "\033[1;37;42m"
blue = "\033[1;37;44m"

def myclear(): #clear screen
	for i in range (1,30):
		print("\n")


myclear()
dht_device = adafruit_dht.DHT11(board.D17) # set gpio pin ie 17

while True:
    try:
        temperature_c = int(dht_device.temperature) # get temp in farenheit
        temperature_f = int(temperature_c * (9 / 5) + 32) # convert to centigrade

        humidity = int(dht_device.humidity) # get humidity

        print(red,"Temp cent ",temperature_c,green," Temp Farh ",temperature_f,blue," Humidity ",humidity,white)
    except RuntimeError as err: # catch errors
        print(err.args[0])

    time.sleep(2.0) # pause 2 seconds



