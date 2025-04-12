# resistor program to determine which resistor
# to use with leds etc / formula is 
# main power volts - working power volts / 0.02 output is in ohms


def myclear(): # clear screen
	for i in range (1,50):
		print("\033[0;37;40m\n")
		
		
while True:
	
	myclear()
	print("\033[H") # ansi code to move cursor to top 0,0
	
	const = 0.02 # constant to divide by
	main = float(input("   ENTER MAIN POWER SOURCE VOLTAGE: "))
	ledpow = float(input("   ENTER LED FORWARD POWER VOLTAGE: "))
	print("\n")
	ohmresult = round(main-ledpow)/(const)
	
	print ("      IF MAIN POWER IS " , main, "VOLTS") 
	print("   & LED FORWARD POWER IS " ,ledpow,"VOLTS","\n")
	print("\033[0;37;44m  POWER OF RESISTOR TO USE IS" , ohmresult , " ohms", "\033[0;37;40m","\n","\n")

	input("HIT ENTER TO CONTINUE OR CNTR/C TO EXIT")



