# TEDS MINI DASHBOARD PROGRAM
 
import os
import psutil
import socket
import time
from time import sleep
from datetime import datetime
print("\033[1;37;40m")

def myclear():
	for i in range (1,30):
		print("\n")
	print("\033[H")

def getip(): # Get host name and ip address
	testIP = "8.8.8.8"
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect((testIP, 0))
	ipaddr = s.getsockname()[0]
	host = socket.gethostname()
	print (" Host Computer is  ","\033[1;37;44m", host, "\033[1;37;40m")
	print (" IP:", ipaddr,"\n")
	
def getdate(): # Get date
	date = str(datetime.now().date())
	print (" Date is now        ", date,)
	
def gettime(): # get time
	time = str(datetime.now().time())
	print(" Time is now         ","\033[1;37;41m",datetime.now().strftime("%H:%M"),"\033[1;37;40m","\n")


# Return CPU temperature as a character string                                      
def getCPUtemperature():
    res = os.popen('vcgencmd measure_temp').readline()
    return(res.replace("temp=","").replace("'C\n",""))
   

# Return RAM information (unit=kb) in a list                                        
# Index 0: total RAM                                                                
# Index 1: used RAM                                                                 
# Index 2: free RAM                                                                 
def getRAMinfo():
    p = os.popen('free')
    i = 0
    while 1:
        i = i + 1
        line = p.readline()
        if i==2:
            return(line.split()[1:4])
            

# Return % of CPU used by user as a character string                                
def getCPUuse():
    return(str(os.popen("top -n1 | awk '/Cpu\(s\):/ {print $2}'").readline().strip(\
)))

# Return information about disk space as a list (unit included)                     
# Index 0: total disk space                                                         
# Index 1: used disk space                                                          
# Index 2: remaining disk space                                                     
# Index 3: percentage of disk used                                                  
                        

def getram(): # RAM information
	# Output is in kb, here I convert it in Mb for readability
	RAM_stats = getRAMinfo()
	RAM_total = round(int(RAM_stats[0]) / 1000,1)
	RAM_used = round(int(RAM_stats[1]) / 1000,1)
	RAM_free = round(int(RAM_stats[2]) / 1000,1)
	print(" Ram Total is      " ,RAM_total, "MBytes")
	print(" Ram Used is        " ,RAM_used, "MBytes")
	print(" Ram Free is       " ,RAM_free, "MBytes","\n")
	
def uptime():
	#return time.time() - psutil.boot_time()
	t = os.popen('uptime -p').read()[:-1]
	print("\n","System  ","\033[1;37;43m",t,"\033[1;37;40m")

while True:
	getip()
	getdate()
	gettime()
	getram()
	CPU_temp = getCPUtemperature() #cpu temp info
	CPU_usage = getCPUuse() # cpu use info
	print(" CPU Temp  is        ","\033[1;37;42m",CPU_temp,"\033[1;37;40m", "Deg")
	print(" CPU Usage is       ",CPU_usage, "Percent")
	uptime()
	sleep(10)
	myclear()
