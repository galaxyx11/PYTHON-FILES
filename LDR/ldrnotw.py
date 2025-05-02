# CamJam EduKit 2 - Sensors (GPIO Zero)
# Worksheet 4 - Light rework as lightsensor no longer works

# Import Libraries
from gpiozero import LightSensor, OutputDevice, InputDevice
from time import sleep

# A variable with the LDR reading pin number
pinldr=27

def readldr():
    ldrcount = 0
    
    pir = OutputDevice(pin=27, active_high=True, initial_value=False)
    # Drive output low to discharge the capacitor
    sleep(0.1)

    # Set to input device
    pir.close()
    pir = InputDevice(pin=27, pull_up=None, active_state=True)

    # Count how long it takes for the input pin to recharge
    while not pir.is_active:
        ldrcount += 1

    pir.close()
    return ldrcount

while True:
	print("LDR READING IS ",readldr())
	if readldr() == 0:
		print("IT'S LIGHT")
	else:
		print("IT'S DARK")
    
sleep(1)  # Wait for a second
