# learning to use oled  !! #


from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306, ssd1325, ssd1331, sh1106
from time import sleep

serial = i2c(port=1, address=0x3C)
device = ssd1306(serial, rotate=0)
x = 0
y = 0

while True:
	with canvas(device) as draw:
		draw.text((x,y), "Hello Ted", fill="white")
		draw.text((x,y+10), "from Galaxysoft !", fill="white")
		draw.text((x,y+20),"Extra Line", fill="white")
		draw.text((x,y+30),"Another Line",fill="white")
		draw.text((x,y+40),"Line 555555",fill="white")
		draw.text((x,y+50),"Line 666666",fill="white")
		draw.text((x,y+60),"Line 777777",fill="white") #no space
		
		
#def scroll_message(status, font=None, speed=1):
#	#author = f"@{status.author.screen_name}"
#	full_text = "teds text !!!!!!!!!!".replace("\n", " ")
#	x = device.width
#	w = 40
 #  	 # First measure the text size
	#with canvas(device) as draw:
	#	left, top, right, bottom = draw.textbbox((0, 0), full_text, font)
	#	w, h = right - left, bottom - top
#
#		virtual = viewport(device, width=max(device.width, w + x + x), height=max(h, device.height))
#	with canvas(virtual) as draw:
#		draw.text((x, 0), full_text, font=font, fill="white")
#		draw.text((x, 0), author, font=font, fill="yellow")

#i = 0
#w=40
#while i < x + w:
#	scroll_message(i)
#	virtual.set_position((i, 0))
#	i += i
#	sleep(0.025)



