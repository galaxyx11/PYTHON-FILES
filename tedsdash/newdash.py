# new dashboard using ansi codes on raspi
# (C) 2025 Galaxysoft.co.uk
# using dht11 sensor for temp/humidity

from time import sleep
from datetime import datetime
import adafruit_dht
import board


#import os
#import socket
#os.system("") # NEEDED ON WINDOWS TO START ANSI CONSOLE


dht_device = adafruit_dht.DHT11(board.D17) # set gpio pin for temp/hum ie 17

# define screen colours
red = "\033[48;5;196m"
white = "\033[1;37;40m"
green = "\033[48;5;254m"
blue = "\033[48;5;21m"
orange = "\033[48;5;214m"
purple = "\033[1;37;45m"
cyan = "\033[1;37;46m"
grey = "\033[1;37;47m"
yellow = ("\033[48;5;226m")
paleg = ("\033[48;5;82m")
yellb = ("\033[48;5;220m")
bluet = ("\033[38;5;21m")
print ("\033[?25l") # hide cursor

try:
	temperature_c = int(dht_device.temperature) # get temp in farenheit
	temperature_f = int(temperature_c * (9 / 5) + 32) # convert to centigrade
	humidity = int(dht_device.humidity) # get humidity
except RuntimeError as err: # catch errors
	print(err.args[0])


def myclear(): #clear screen
	for i in range (1,30):
		print("\n")
		
		
# Return % of CPU used by user as a character string                                
def getCPUuse():
    return(str(os.popen("top -n1 | awk '/Cpu\(s\):/ {print $2}'").readline().strip()))
	
	
def getCPUtemperature(): # get cpu temp
    res = os.popen('vcgencmd measure_temp').readline()
    return(res.replace("temp=","").replace("'C\n",""))
    
def getDf(): # get disk useage
	global df
	df = os.popen("df -h /")
	i = 0
	while True:
		i = i + 1
		line = df.readline()
		if i==2:
			return(line.split()[0:6])
	
def getRAMinfo(): # get ram info
    p = os.popen('free')
    i = 0
    while 1:
        i = i + 1
        line = p.readline()
        if i==2:
            return(line.split()[1:4])
		
RAM_stats = getRAMinfo()
RAM_total = round(int(RAM_stats[0]) / 1000,1)
RAM_used = round(int(RAM_stats[1]) / 1000,1)
RAM_free = round(int(RAM_stats[2]) / 1000,1)

testIP = "8.8.8.8" # get ip address and hostname
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect((testIP, 0))
ipaddr = s.getsockname()[0]
host = socket.gethostname()

CPU_temp = getCPUtemperature() #cpu temp info
CPU_usage = getCPUuse() # cpu use
		 
		
while True:
	myclear()
	time1 = datetime.now()
	ctime = time1.strftime("%H:%M:%S")
	date = str(datetime.now().date())
	ut = (os.popen('uptime -p').read()[:-1])
	getDf()
	print("\033[H")
	
	print("\n",white,"             **************************************",white)		
	print(white,"              *     CURRENT COMPUTER DASHBOARD     *",white)
	print(white,"              *    HOST COMPUTER IS ",host,"  *",white)
	print(white,"              **************************************",white,"\n")
	print("  ",red,"                     ",green,"                  ",blue,"                 ",white,)
	print("  ",red," ",white," CURRENT TIME  ",red," ",green," ",white,"TODAYS DATE ",green," ",blue," ",white,"TEMPERATURE",blue," ",white,)
	print("  ",red," ",white,"      IS       ",red," ",green," ",white,"     IS     ",green," ",blue," ",white,"     IS    ",blue," ",white,)
	print("  ",red," ",white,"               ",red," ",green," ",white,"            ",green," ",blue," ",white,"           ",blue," ",white,)
	print("  ",red," ",white,"  ",ctime,"   ",red," ",green," ",white,"",date,"",green," ",blue," ",white,"",temperature_c,"Deg C"," ",blue," ",white,)
	print("  ",red," ",white,"               ",red," ",green," ",white,"            ",green," ",blue," ",white,"",temperature_f,"Deg F"," ",blue," ",white,)
	print("  ",red,"                     ",green,"                  ",blue,"                 ",white,)
	
	
	print()
	print("  ",grey,"                     ",purple,"                  ",cyan,"                 ",white,)
	print("  ",grey," ",white,"    HUMIDITY   ",grey," ",purple," ",white,"    HOME    ",purple," ",cyan," ",white," WEB PORTAL",cyan," ",white,)
	print("  ",grey," ",white,"       IS      ",grey," ",purple," ",white,"     IS     ",purple," ",cyan," ",white,"     IS    ",cyan," ",white,)
	print("  ",grey," ",white,"               ",grey," ",purple," ",white,"            ",purple," ",cyan," ",white,"           ",cyan," ",white,)
	print("  ",grey," ",white," ",humidity,"Percent","  ",grey," ",purple," ",white,"/home/galaxy",purple," ",cyan," ",white," SKYNKRH8",white,"",cyan," ",white,)
	print("  ",grey," ",white,"               ",grey," ",purple," ",white,"            ",purple," ",cyan," ",white,"           ",cyan," ",white,)
	print("  ",grey,"                     ",purple,"                  ",cyan,"                 ",white,)
	
	
	print()
	print("  ",yellow,"                     ",orange,"                  ",paleg,"                 ",white,)
	print("  ",yellow," ",white,"   IP ADDRESS  ",yellow," ",orange," ",white," CPU USEAGE ",orange," ",paleg," ",white,"  MEMORY   ",paleg," ",white,)
	print("  ",yellow," ",white,"       IS      ",yellow," ",orange," ",white,"     IS     ",orange," ",paleg," ",white,"  USEAGE   ",paleg," ",white,)
	print("  ",yellow," ",white,"               ",yellow," ",orange," ",white,CPU_usage," Percnt",orange," ",paleg," ",white,"Total",RAM_total,paleg," ",white,)
	print("  ",yellow," ",white,"",ipaddr,"",yellow," ",orange," ",white,CPU_temp," Temp C",orange," ",paleg," ",white,"Used ",RAM_used,paleg," ",white,)
	print("  ",yellow," ",white,"               ",yellow," ",orange," ",white,"            ",orange," ",paleg," ",white,"Free ",RAM_free,paleg," ",white,)
	print("  ",yellow,"                     ",orange,"                  ",paleg,"                 ",white,)
	
	print("\n              Computer * ",ut," *")
	print("\n","            HAVE A GREAT DAY ----  CTRL/C TO EXIT")
	sleep(1)



