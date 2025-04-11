# LCD CODES FOR I2C INTERFACE
## lsmod | grep i2c_ CHECK INTERFACE ADDRESS I2C SHOULD BE #027
# sudo pip3 install RPLCD smbus
# nano lcd_display.py / create python script
# REPLACE 0X27 WITH THE ADDESS FROM EARLIER

 # sudo i2cdetect 1   detect which i2c devices present

#from RPLCD.i2c import CharLCD
#lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1, cols=16, rows=2, dotsize=8)
#lcd.clear()
#lcd.write_string('Hello, World!')

# RUN WITH /python3 lcd_display.py

#Connect VCC (power) to the 5V pin (pin 4)
#Connect GND (ground) to any GND pin (pin 6)
#Connect SDA (data) to GPIO 2 (pin 3)
#Connect SCL (clock) to GPIO 3 (pin 5)

