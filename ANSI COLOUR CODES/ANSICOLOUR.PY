# PYTHON 3 FOR WINDOWS ANSI COLOUR CODES
# TED H (C) GALAXYSOFT.CO.UK 2026

from time import sleep
import os
os.system("")  # enables ansi escape characters in terminal

COLOR = {
    "PURPLE": "\33[95m", # \33 IS THE ESCAPE CODE
    "CYAN": "\33[96m",
    "YELLOW": "\33[93m",
    "BLUE": "\33[94m",
    "GREEN": "\33[92m",
    "RED": "\33[91m",
    "REV": "\33[7m",  # 7m REVERSE COLOUR
    "UND": "\33[4m",  # 4m UNDERLINE
    "BOLD": "\33[1m", # 1m BOLD
    "ENDC": "\33[0m", # RETURN TEXT TO WHITE ON BLACK
    "HOME": "\33[H"   # RETURN CURSOR TO HOME POSITION
}
print(COLOR["HOME"],)
print("")
print(COLOR["REV"],"     TESTING ANSI CODES IN PYTHON ON WIN 10      ")
print(COLOR["ENDC"])
print(COLOR["PURPLE"],"TEST PURPLE TEDDDDDDDDDYY")
print(COLOR["GREEN"], "TEST GREEN TEDDDDDDDDDYY!!")
print(COLOR["RED"],"TEST RED TEDDDDDDDDDDDYY")
print(COLOR["CYAN"],"TEST CYAN TEDDDDDDDDDDDYY")
print(COLOR["YELLOW"],"TEST YELLOW TEDDDDDDDDDYY")
print(COLOR["BLUE"],"TEST BLUE TEDDDDDDDDDYY",COLOR["ENDC"])
print("")
print(COLOR["GREEN"],"TEST TWO COLORS",COLOR["RED"]," ON ONE LINE")
print(COLOR["BLUE"],"ETC",COLOR["RED"]," ETC",COLOR["GREEN"],"ETC",COLOR["YELLOW"],"ETC",COLOR["PURPLE"],"ETC")
print("")
print(COLOR["REV"],"TEST REVERSE",COLOR["YELLOW"],"TEST REVERSE",COLOR["RED"],"TEST REVERSE",COLOR["ENDC"],)
print("")
print(COLOR["UND"],"TESTING UNDERLINE ",COLOR["ENDC"])
print("")
print(COLOR["BOLD"],"TESTING BOLD BOLD BOLD")
print("")
print(COLOR["ENDC"],"TEST BACK TO NORMAL")

sleep(1000)


