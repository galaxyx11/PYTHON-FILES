# TEDS PROGRAM TO COMBINE LED'S BUZZER
# LCD SCREEN AND BUTTONS

# IMPORT NEEDED LIBRARYS
from time import sleep
from datetime import datetime
from gpiozero import Button,LED,Buzzer
import drivers # lcd drivers

# SETUP VARIABLES AND GPIO PINS
# LCD IS ON I2C
display = drivers.Lcd()
button = Button(25)
buzzer = Buzzer(22)
red = LED(18)
yellow = LED(23)
green = LED(24)
stime = 0.5

# set screen colour to white on black
print("\033[1;37;40m")


# DEFINE SUB ROUTINES this clears screen
def myclear():
	for i in range (1,40):
		print("\n")


# RUN MAIN PROGRAM
myclear() # clear screen and lcd
display.lcd_clear()
print("\033[1;37;46m" + " ********************************************* " + "\033[1;37;40m")
print("\033[1;37;46m" + " *  PROGRAM TO DEMONSTRATE MIXTURE OF ITEMS  * " + "\033[1;37;40m")
print("\033[1;37;46m" + " *  USING GPIO PINS, LEDS, BUTTONS, BUZZERS  * " + "\033[1;37;40m")
print("\033[1;37;46m" + " *    AND AN LCD 1602 OR 2004 LCD SCREEN     * " + "\033[1;37;40m" )
print("\033[1;37;46m" + " ********************************************* " + "\033[1;37;40m" + "\n")

print("      " + "\033[0;37;44m" + " ALSO USING SCREEN CODES FOR COLOURS " + "\033[1;37;40m" + "\n")

print("              " + "\033[6;37;41m" + "  TURNING ON LEDS  " + "\033[1;37;40m" + "\n")
for i in range (1,6):
	# Turn LEDs on and off
	red.off()
	yellow.off()
	green.off()
	sleep(1)
	red.on()
	yellow.on()
	green.on()
	sleep(1)

print("              " + "\033[6;37;42m" + " TURNING ON BUZZER " + "\033[1;37;40m" + "\n")
for i in range (1,6):
	buzzer.on()
	sleep(0.1)
	buzzer.off()
	sleep(0.1)
sleep(3)
	
	
print("            " + "\033[6;37;43m" + " TURNING ON LCD SCREEN " + "\033[1;37;40m" + "\n")
for i in range (1,3):
	display.lcd_display_string("MY GPIO PROGRAM", 1) # Write line of text to first line of display
	# Write just the time to the display
	display.lcd_display_string(str(datetime.now().time()), 2)
	sleep(3)
	display.lcd_display_string("CURRENT TIME IS", 1)
	sleep(3)
	
	
print("  " + "\033[0;37;45m" + " PRESS THE BUTTON FOR EVERYTHING TOGETHER " + "\033[1;37;40m" + "\n")

while True:
    # If the button is pressed, button.is_pressed will be 'true'
    if button.is_pressed:
        print("      " + "\033[1;37;46m" + " ********************************** " + "\033[1;37;40m")
        print("      " + "\033[1;37;46m" + " **   BUTTON PRESSED ON GPIO 25  ** " + "\033[1;37;40m")
        print("      " + "\033[1;37;46m" + " **    LED PROGRAM IS RUNNING    ** " + "\033[1;37;40m")
        print("      " + "\033[1;37;46m" + " ********************************** " + "\033[1;37;40m" + "\n")
        
        # Turn LEDs off
        red.off()
        yellow.off()
        green.off()
        
        print("      " + "\033[6;37;41m" + "  " + "  RED LED FLASHING ON GPIO 18     " + "\033[1;37;40m" + "\n")
        for t in range (1,4):
            buzzer.on()
            red.on()
            sleep(stime)
            buzzer.off()
            red.off()
            sleep(stime)
            
        print("      " + "\033[6;37;43m" + " " + "  YELLOW LED FLASHING ON GPIO 23   " + "\033[1;37;40m" + "\n")     
        for t in range (1,4):
            buzzer.on()
            yellow.on()
            sleep(stime)
            buzzer.off()
            yellow.off()
            sleep(stime)
            
        
       
        print("      " + "\033[6;37;42m" + "  " + "  GREEN LED FLASHING ON GPIO 24   " + "\033[1;37;40m" + "\n")   
        for t in range (1,4):
            buzzer.on()
            green.on()
            sleep(stime)
            buzzer.off()
            green.off()
            sleep(stime)
            
        print("    " + "\033[6;37;45m" + "  " + "  LCD SCREEN IS SHOWING TIME ON I2C   " + "\033[1;37;40m" + "\n")   
        for t in range (1,4):
            display.lcd_display_string(str(datetime.now().time()), 2)
            sleep(1)
            display.lcd_display_string("CURRENT TIME IS", 1)
            buzzer.on()
            green.on()
            sleep(stime)
            buzzer.off()
            green.off()
            sleep(stime)
             
             
        print("      " + "\033[5;35;47m" + "    " + "     BUZZER IS ON GPIO 22      " + "\033[1;37;40m" + "\n")
        print("      " + "\033[0;37;44m" + " ********************************** " + "\033[1;37;40m")
        print("      " + "\033[0;37;44m" + " **   PROGRAM FINISHED RUNNING   ** " + "\033[1;37;40m")
        print("      " + "\033[0;37;44m" + " **      CLEANING UP GOODBYE     ** " + "\033[1;37;40m")
        print("      " + "\033[0;37;44m" + " ********************************** " + "\033[1;37;40m")
        
        # TURN IT ALL OFF if FINISHED
        sleep(5)
        red.off()
        yellow.off()
        green.off()
        buzzer.off()
        display.lcd_clear()
        input("\n" + "PRESS ENTER TO FINISH")
        myclear()
        quit()
    else: # IF PROGRAM GOT THIS FAR BUTTON STILL WAITING
		  # FOR PRESS (FALSE) SO WAIT 1 SECOND AND LOOP
		  # AGAIN UNTIL PRESSED(BUTTON WILL RETURN TRUE WHEN PRESSED)
        sleep(1)  # Sleep for a second
 
