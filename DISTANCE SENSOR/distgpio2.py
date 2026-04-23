from gpiozero import DistanceSensor
import time

yellb = "\033[1;37;44m" # ansi blue
black = "\033[1;37;40m" # ansi black

pintrigger = 23 #trigger on gpio 23
pinecho = 18 # echo pin on gpio 18
sensor1 = DistanceSensor(echo=pinecho,trigger=pintrigger,max_distance =4)# up to 4 metres

try:
    while True:
        print("   ",yellb,"UltraSonic Measurement in Progress",black,"\n")
        inchs = round(int(sensor1.distance*100) /2.54)# convert for inches
        feet = round(inchs / 12) # convert to feet
        print(" Distance =",int(sensor1.distance * 100),"Cms","or",inchs,"Inches", "or",feet,"Feet","\n\n\n")
        time.sleep(2)
except KeyboardInterrupt:
    print("EXITING MEASUREMENT SENSOR")
            
        
