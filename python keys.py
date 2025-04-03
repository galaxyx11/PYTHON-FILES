# demo-keyboard.py

import struct
import sys
from datetime import datetime

def GetKeyboardEventFile(tokenToLookFor):
	# Any exception raised here will be processed by the calling function.
	section = ""
	line = ""
	eventName = ""

	fp = open ("/proc/bus/input/devices", "r")
	done = False
	while False == done:
		line = fp.readline()
		if line:
			#print (line.strip())
			if "" == line.strip():
				#print ("\nFound Section:\n" + section)
				if -1 != section.find(tokenToLookFor) and -1 == section.lower().find("mouse"):
					# It is entirely possible there to be multiple devices
					# listed as a keyboard. In this case, I will look for 
					# the word "mouse" and exclude anything that contains
					# that. This section may need to be suited to taste
					print ("Found [" + tokenToLookFor + "] in:\n" + section)
					# Get the last part of the "Handlers" line:
					lines = section.split('\n')
					for sectionLine in lines:
						# The strip() method is needed because there may be trailing spaces
						# at the end of this line. This will confuse the split() method.
						if -1 != sectionLine.strip().find("Handlers=") and "" == eventName:
							print ("Found Handlers line: [" + sectionLine + "]")
							sectionLineParts = sectionLine.strip().split(' ')
							eventName = sectionLineParts[-1]
							print ("Found eventName [" + eventName + "]")
							done = True
				section = ""
			else:
				section = section + line
		else:
			done = True
	fp.close()

	if "" == eventName:
		raise Exception("No event name was found for the token [" + tokenToLookFor + "]")

	return "/dev/input/" + eventName

def main(argv):
	# Need to add code which figures out the name of this file from 
	# /proc/bus/input/devices - Look for EV=120013
	# Per Linux docs, 120013 is a hex number indicating which types of events
	# this device supports, and this number happens to include the keyboard
	# event.

	keyboardEventFile = ""
	try:
		keyboardEventFile = GetKeyboardEventFile("EV=120013");
	except Exception as err:
		print ("Couldn't get the keyboard event file due to error [" + str(err) + "]")

	if "" != keyboardEventFile:
		try:
			k = open (keyboardEventFile, "rb");
			# The struct format reads (small L) (small L) (capital H) (capital H) (capital I)
			# Per Python, the structure format codes are as follows:
			# (small L) l - long
			# (capital H) H - unsigned short
			# (capital I) I - unsigned int
			structFormat="llHHI"
			eventSize = struct.calcsize(structFormat)

			event = k.read(eventSize)
			goingOn = True
			while goingOn and event:
				(seconds, microseconds, eventType, eventCode, value) = struct.unpack(structFormat, event)

				# Per Linux docs at https://www.kernel.org/doc/html/v4.15/input/event-codes.html
				# Constants defined in /usr/include/linux/input-event-codes.h 
				# EV_KEY (1) constant indicates a keyboard event. Values are:
				# 1 - the key is depressed.
				# 0 - the key is released.
				# 2 - the key is repeated.

				# The code corresponds to which key is being pressed/released.

				# Event codes EV_SYN (0) and EV_MSC (4) appear but are not used, although EV_MSC may 
				# appear when a state changes.

				unixTimeStamp = float(str(seconds) + "." + str(microseconds)) 
				utsDateTimeObj = datetime.fromtimestamp(unixTimeStamp)
				friendlyDTS = utsDateTimeObj.strftime("%B %d, %Y - %H:%M:%S.%f")

				if 1 == eventType:
					# It is necessary to flush the print statement or else holding multiple keys down
					# is likely to block *output*
					print ("Event Size [" + str(eventSize) + "] Type [" + str(eventType) + "], code [" +
					str (eventCode) + "], value [" + str(value) + "] at [" + friendlyDTS + "]", flush=True)
				if 1 == eventCode:
					print ("ESC Pressed - Quitting.")
					goingOn = False
				#if 4 == eventType:
				#	print ("-------------------- Separator Event 4 --------------------")
				event = k.read(eventSize)

			k.close()
		except IOError as err:
			print ("Can't open keyboard input file due to the error [" + str(err) + "]. Maybe try sudo?")
		except Exception as err:
			print ("Can't open keyboard input file due to some other error [" + str(err) + "].")
	else:
		print ("No keyboard input file could be found.")
	return 0

if "__main__" == __name__:
	main(sys.argv[1:])