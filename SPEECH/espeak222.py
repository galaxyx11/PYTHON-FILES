# LDR Light Sensors (GPIO Zero) galaxysoft.co.uk (C) 2025
# Light rework as SightSensor no longer works
# use with light detecting diode and laser when beam is 
# broken detection warning given
# speech from espeak library # sudo apt install espeak

# Import Libraries
from gpiozero import LightSensor, OutputDevice, InputDevice
from time import sleep
import os

# A variable with the LDR reading pin number
pinldr=27

blue = "\033[1;37;44m" # ansi blue
black = "\033[1;37;40m" # ansi black
red = "\033[1;37;41m" # ansi red

def readldr():
    ldrcount = 0
    
    pir = OutputDevice(pin=27, active_high=True, initial_value=False)
    # Drive output low to discharge the capacitor
    sleep(0.2)

    # Set to input device
    pir.close()
    pir = InputDevice(pin=27, pull_up=None, active_state=True)

    # Count how long it takes for the input pin to recharge
    while not pir.is_active:
        ldrcount += 1

    pir.close()
    return ldrcount

while True:
	print("LDR READING IS",readldr())
	if readldr() <=25:
		print(blue," IT'S LIGHT ",black,"\n")
	else:
		print(red," IT'S DARK ",black,"\n")
		os.system("espeak -a200 -ven -s170 -p50 'warning intruder detected' ")
		# espeak parameters a/volume v/english s/speed p/pitch

sleep(1)  # Wait for a second
