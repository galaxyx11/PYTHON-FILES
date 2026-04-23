from gpiozero import DistanceSensor
import time


pintrigger = 23
pinecho = 18
sensor1 = DistanceSensor(echo=pinecho,trigger=pintrigger)
print("UltraSonic Measurement in Progress")
try:
    while True:
        inchs = round(int(sensor1.distance*100) /2.4)
        print("Distance =",int(sensor1.distance * 100),"Cms"," or ",inchs,"inches")
        time.sleep(1)
except KeyboardInterrupt:
    print("EXITING MEASUREMENT SENSOR")
            
        
