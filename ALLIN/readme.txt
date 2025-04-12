Used python 3 ....    allin.py

**** WARNING  if you have any problem with flashing
text and lights dont use this program ****

python program to test gpio and lcd use
written for me to get used to using all of this !!
you can find me and more programs at galaxy@galaxysoft.co.uk
and my github repos at galaxyx11


used breadboard to wire as follows
used raspberry pi 400. but any raspi with the
40 pin gpio will work (tried and works on raspi 5)
the gpiozero library is used for the leds buttons and buzzer
https://github.com/gpiozero/gpiozero

gpio 18 red led
gpio 24 yellow led
gpio 24 green led
gpio 22 buzzer
gpio  25 button

leds wired with 470 ohm pullup resistors
button and buzzer need no resistors. 
you can adjust the code if you use different pins

the lcd is a 1602 (16x2) wired with an i2c backpack easier as just 2 wires sda and sdc
plus 5v and ground. Driver library folder must be in same directory as the allin.py prog
lcd driver library is from 
git clone https://github.com/the-raspberry-pi-guy/lcd.git
clone this repo for installation instructions and some demo progs

2004 (20x4) lcd can also be used with this library the only difference is
you write to lines 3 and 4 for the extra display lines.

	display.lcd_display_string("MY GPIO PROGRAM", 1) # Write text to first line of display
	display.lcd_display_string(" THIS IS LINE 2", ) # Write text to second line of display
	display.lcd_display_string("THIS IS LINE 3", ) # Write text to third line of display
	display.lcd_display_string("THIS IS LINE 4", ) # Write text to forth line of display

Dont forget 1602 only has 16 charachters / 2004 has 20 charachters per line

The terminal (ansi) colour codes are great for formatting the terminal display
adds a lot to the quality of the output. they take the following format
see these for a full explaination.
https://en.wikipedia.org/wiki/ANSI_escape_code
https://gist.github.com/ConnerWill/d4b6c776b509add763e17f9f113fd25b

#  ie set screen colour to white on black
print("\033[1;37;40m") etc : colour codes can be copied
or cut and pasted from the following program.
Run this for a colourful treat...

########### print terminal colour chart  ############
# not my program found on the web so thanks to whoever
# wrote this very useful code.

def print_format_table():
    """
    prints table of formatted text format options
    """
    for style in range(8):
        for fg in range(30, 38):
            s1 = ''
            for bg in range(40, 48):
                format = ';'.join([str(style), str(fg), str(bg)])
                s1 += '\x1b[%sm %s \x1b[0m' % (format, format)
            print(s1)
        print('\n')
print_format_table()

##################################################

Have fun modifying and trying different thing yourself
hope it helps in learning python and use of gpio's and i2c
on raspberry pi. Just learning this myself so any comments
and tips gratefully received...... galaxy



