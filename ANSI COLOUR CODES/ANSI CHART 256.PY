# LISTING ANSI COLOURS IN CHART FORM
# 231 TO 255 ARE IN GREYSCALE
# (C) tedh@galaxysoft.co.uk 2026

from time import sleep
import sys
import os
os.system("") # NEEDED ON WINDOWS TO START ANSI CONSOLE

# print("\33[38;5;154m	   = 38 SET FOREGROUND COLOUR
# print("\33[48;5;215m	   = 48 SET BACKGROUND COLOUR
# print("\33[7m")          = TURN ON REVERSE PRINTING
# print ("\33[0m")         = RETURN TO NORMAL PRINTING
# print ("\33[38;5;231m")  = ATTRIBUTES CAN BE ADDED TO THE LIST WITH SEMI COLON SEPERATOR

print("")
print("\33[0m" + "                 " + "\33[38;5;231m" + "\33[48;5;196m"+ "        " + "  LISTING ANSI COLOURS IN CHART FORM              ")
print("\33[0m" + "                 " + "\33[38;5;196m" + "\33[48;5;227m" + "        " + "FIRST WITH REVERSE ON THEN TEXT COLOUR ONLY       ")
print ("\33[0m")
print("")
print("\33[7m")


for i in range(0, 16):
	for j in range(0, 16):
	 colcode = str(i * 16 + j)
	 sys.stdout.write("\33[38;5;" + colcode + "m   " + colcode)
	 
print("")
print ("\33[0m")	
 
for i in range(0, 16):
	for j in range(0, 16):	
	 colcode = str(i * 16 + j)
	 sys.stdout.write("\33[38;5;" + colcode + "m   " + colcode)
	 
print("")
print("")
print(" \33[94m" + "              YOU CAN MIX AND MATCH THE" + "\33[93m" + "  CODE NUMBERS IN THE ESCAPE STRINGS")
print("\33[92m" + "                          SO ADD SOME COLOUR " + "\33[91m" + "TO YOUR PROGRAMS ")	 
print("\33[95m" + "                                   HAVE SOME FUN !!")
print("")
print("\33[38;5;231m" + "\33[48;5;196m" + " PRESS CONTROL C TO EXIT ")	 
	 

sleep(1000)
