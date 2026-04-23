# Multi resistor charts and useful calculators tedh @ galaxysoft.co.uk 2025
# Written to get used to coding in python
# and using ansi codes for terminal dipslays on raspberry pi projects.
# Never seemed to have a colour chart when needed :)
# Hope you find this useful .. enjoy

import sys
import os
os.system("") # NEEDED ON WINDOWS TO START ANSI CONSOLE

# Define 256 Colour Ansi Codes b suffix = background / t = text
yellb = ("\033[48;5;220m")
orangeb = ("\033[48;5;209m")
greyb = ("\033[48;5;246m")
greenb =("\033[48;5;190m")
violetb =("\033[48;5;165m")

# Define 8 Colour Ansi Codes
blackt =("\033[38;5;16m")
bluet = ("\033[38;5;21m")
whitblac = ("\033[1;37;40m")
blacwhit = ("\033[1;30;47m")
white = ("\033[1;30;47m")
red = ("\033[1;30;41m")
blue = ("\033[1;30;44m")
orange = ("\033[1;31;43m")
yellow = ("\033[1;30;43m")
green = ("\033[1;30;42m")
violet = ("\033[1;30;45m")
grey = ("\033[2;37;40m")
brown = ("\033[2;35;43m")
bblue = ("\033[1;37;44m")
white1 = ("\033[1;30;47m")
red1 = ("\033[1;30;41m")
blue1 = ("\033[1;30;44m")
orange1 = ("\033[1;31;43m")
yellow1 = ("\033[1;30;43m")
green1 = ("\033[1;30;42m")
violet1 = ("\033[1;30;45m")
grey1 = ("\033[2;37;40m")
brown1 = ("\033[2;35;43m")
bblue1 = ("\033[1;37;44m")



def myclear(): # Clear screen
	for i in range (1,40):
		print("\n")
print("\033[H") # cursor to 0,0

	
def respic(): # Ansi Resistor picture
	print("\n")
	print("         ",whitblac,"------",blue,"1",white,"  ",red,"2",white,"  ",brown,"3",white,\
	"  ",greenb,blackt,"M",white,"  ",violetb,blackt,"T",whitblac,"------")
	print("\n"," Example ---- 621 x 100K = 621K ohm with a tolerance of +/- 0.10%")
	print("\n   PRESS",bblue, "1",whitblac,"FOR CHARTS ",bblue,"2",whitblac," FOR CALCULATOR ",bblue,"3",whitblac,"FOR COLOUR CHECKER",whitblac)	
	
		
def fivebar(): # Five bar resistor chart
	print("                    ",bblue," FIVE BAR RESISTOR CODE CHART",whitblac,"\n")
	print("  -------------------------------------------------------------------")		
	print("            1st BAR     2nd BAR     3rd BAR   MULTIPLIER   TOLERANCE")
	print("  -------------------------------------------------------------------")
	print(" ",whitblac," BLACK      0           0           0       1    ohm      ",whitblac)
	print(" ",brown," BROWN      1           1           1       1O   ohm     +/- 1%  ",whitblac)
	print(" ",red," RED        2           2           2       100  ohm     +/- 2%  ",whitblac)
	print(" ",orangeb,blackt,"ORANGE     3           3           3       1K   ohm     +/- 2%  ",whitblac)
	print(" ",yellb,blackt,"YELLOW     4           4           4       10K  ohm     +/- 2%  ",whitblac)
	print(" ",greenb,blackt,"GREEN      5           5           5       100K ohm     +/-0.5% ",whitblac)
	print(" ",blue," BLUE       6           6           6       1M   ohm     +/-0.25%",whitblac)
	print(" ",violetb,blackt,"VIOLET     7           7           7       10M  ohm     +/-0.10%",whitblac)
	print(" ",greyb,blackt,"GREY       8           8           8         N/A          N/A   ",whitblac)
	print(" ",white," WHITE      9           9           9         N/A          N/A   ",whitblac)
					

def fourbar(): # Four bar resistor chart
	print("                     ",bblue," FOUR BAR RESISTOR CODE CHART",whitblac,"\n")
	print("     ------------------------------------------------------------")		
	print("            1st BAR     2nd BAR     MULTIPLIER   TOLERANCE")
	print("     ------------------------------------------------------------")
	print("    ",whitblac," BLACK      0           0           1    ohm       ",whitblac)
	print("    ",brown," BROWN      1           1           1O   ohm     +/- 1%  ",whitblac)
	print("    ",red," RED        2           2           100  ohm     +/- 2%  ",whitblac)
	print("    ",orangeb,blackt,"ORANGE     3           3           1K   ohm     +/- 2%  ",whitblac)
	print("    ",yellb,blackt,"YELLOW     4           4           10K  ohm     +/- 2%  ",whitblac)
	print("    ",greenb,blackt,"GREEN      5           5           100K ohm     +/-0.5% ",whitblac)
	print("    ",blue," BLUE       6           6           1M   ohm     +/-0.25%",whitblac)
	print("    ",violetb,blackt,"VIOLET     7           7           10M  ohm     +/-0.10%",whitblac)
	print("    ",greyb,blackt,"GREY       8           8             N/A          N/A   ",whitblac)
	print("    ",white," WHITE      9           9             N/A          N/A   ",whitblac)
	
	
def respower(): # Works out value of resistor needed
	myclear()
	print("\033[H") # ansi code to move cursor to top 0,0
	print("                  \033[0;37;44m  RESISTOR POWER CALCULATOR",whitblac,"\n")
	const = 0.02 # constant to divide by
	main = float(input("    ENTER MAIN POWER SOURCE IN VOLTS:   "))
	ledpow = float(input("    ENTER LED FORWARD POWER IN VOLTS:   "))
	print("\n")
	ohmresult = round(main-ledpow)/(const)
	print ("                IF MAIN POWER IS " , main, "VOLTS") 
	print("           & LED FORWARD POWER IS " ,ledpow,"VOLTS","\n\n")
	print("    \033[0;37;44m  POWER OF RESISTOR TO USE IS ",whitblac,"   ",yellb,bluet, ohmresult , " ohms", "\033[0;37;40m","\n","\n")
	print("\n   PRESS",bblue, "1",whitblac,"FOR CHARTS ",bblue,"2",whitblac," FOR CALCULATOR ",bblue,"3",whitblac,"FOR COLOUR CHECKER",whitblac)
				

def respic4(): # Resistor picture 4 bar
	print("\n")
	print("          ",whitblac,"------",blue1,"1",white1,"  ",red,"2",white1,\
	"  ",green1,"M",white1,"  ",violet1,"T",whitblac,"------")
	print("\n"," Example ---- 625 x 100K = 625K ohm with a tolerance of +/- 0.10%"+"\n")
	

def respic5(): # Resistor picture 5 bar
	print("\n")
	print("          ",whitblac,"------",blue1,"1",white1,"  ",red1,"2",white1,"  ",brown1,"3",white1,\
	"  ",green1,"M",white1,"  ",violet1,"T",whitblac,"------")
	print("\n"," Example ---- 621 x 100K = 621K ohm with a tolerance of +/- 0.10%","\n")


def gofour(): # Work out value of 4 bar resistors
	print("\n" + "     FOUR BAND RESISTORS HAVE 2 VALUES + MULTIPLIER + TOLERANCE" +"\n"+"\n")
	band1 = input(" Please Enter Colour for Band 1  ").lower()
	if band1 == "black":
		res1 = 0
	if band1 == "brown":
		res1 = 1
	if band1 == "red":
		res1 = 2
	if band1 == "orange":
		res1 = 3
	if band1 == "yellow":
		res1 = 4
	if band1 == "green":
		res1 = 5
	if band1 == "blue":
		res1 = 6
	if band1 == "violet":
		res1 = 7
	if band1 == "grey":
		res1 = 8
	if band1 == "white":
		res1 = 9
		
	band2 = input(" Please Enter Colour for Band 2  ").lower()
	if band2 == "black":
		res2 = 0
	if band2 == "brown":
		res2 = 1
	if band2 == "red":
		res2 = 2
	if band2 == "orange":
		res2 = 3
	if band2 == "yellow":
		res2 = 4
	if band2 == "green":
		res2 = 5
	if band2 == "blue":
		res2 = 6
	if band2 == "violet":
		res2 = 7
	if band2 == "grey":
		res2 = 8
	if band2 == "white":
		res2 = 9
		
	band3 = input(" Please Enter Colour for Band 3  ").lower()#multiplier
	if band3 == "black":
		res3 = 0
	if band3 == "brown":
		res3 = 10
	if band3 == "red":
		res3 = 100
	if band3 == "orange":
		res3 = 1000
	if band3 == "yellow":
		res3 = 10000
	if band3 == "green":
		res3 = 100000
	if band3 == "blue":
		res3 = 1000000
	if band3 == "violet":
		res3 = 10000000
	if band3 == "grey":
		res3 = 0
	if band3 == "white":
		res3 = 0
	if band3 == "gold":
		res3 = 0.1
	if band3 == "silver":
		res3 = 0.01
	
		
	band4 = input(" Please Enter Colour for Band 4  ").lower()#tolerance
	if band4 == "black":
		res4 = 0
	if band4 == "brown":
		res4 = 1
	if band4 == "red":
		res4 = 2
	if band4 == "orange":
		res4 = 2
	if band4 == "yellow":
		res4 = 2
	if band4 == "green":
		res4 = 0.5
	if band4 == "blue":
		res4 = 0.25
	if band4 == "violet":
		res4 = 0.10
	if band4 == "grey":
		res4 = 0.05
	if band4 == "white":
		res4 =0.05
	if band4 == "gold":
		res4 = 5
	if band4 == "silver":
		res4 = 10
	print("\n")
	print("  BAR 1 - VALUE",res1)
	print("  BAR 2 - VALUE",res2)
	print("  BAR 3 - MULTIPLIER",res3)
	print("  BAR 4 - TOLERANCE",res4,"%","\n")
	total1 = int((res1 * 10) + (res2))# work out 1st 2 places
	print("\n","TOTAL IS",total1,"X MULTIPLIER",res3,"WITH A TOLERANCE OF +/-",res4,"PERCENT","\n")
	total2 = int(total1 * res3) # take total of bar1 and bar2 and multiply by multiplier
	total3 = (total2/1000) # divide by 1000 to get 'K'
	print("       RESISTOR IS ",bblue,total3," K Ohms",whitblac)
		
	
def gofive(): # work out value of 5 bar resistor
	print("\n" + "     FIVE BAND RESISTORS HAVE 3 VALUES + MULTIPLIER + TOLERANCE" +"\n")
	band1 = input(" Please Enter Colour for Band 1  ").lower()
	
	if band1 == "black":
		res1 = 0
	if band1 == "brown":
		res1 = 1
	if band1 == "red":
		res1 = 2
	if band1 == "orange":
		res1 = 3
	if band1 == "yellow":
		res1 = 4
	if band1 == "green":
		res1 = 5
	if band1 == "blue":
		res1 = 6
	if band1 == "violet":
		res1 = 7
	if band1 == "grey":
		res1 = 8
	if band1 == "white":
		res1 = 9
		
	band2 = input(" Please Enter Colour for Band 2  ").lower()
	if band2 == "black":
		res2 = 0
	if band2 == "brown":
		res2 = 1
	if band2 == "red":
		res2 = 2
	if band2 == "orange":
		res2 = 3
	if band2 == "yellow":
		res2 = 4
	if band2 == "green":
		res2 = 5
	if band2 == "blue":
		res2 = 6
	if band2 == "violet":
		res2 = 7
	if band2 == "grey":
		res2 = 8
	if band2 == "white":
		res2 = 9
		
	band3 = input(" Please Enter Colour for Band 3  ").lower()
	if band3 == "black":
		res3 = 0
	if band3 == "brown":
		res3 = 1
	if band3 == "red":
		res3 = 2
	if band3 == "orange":
		res3 = 3
	if band3 == "yellow":
		res3 = 4
	if band3 == "green":
		res3 = 5
	if band3 == "blue":
		res3 = 6
	if band3 == "violet":
		res3 = 7
	if band3 == "grey":
		res3 = 8
	if band3 == "white":
		res3 = 9
		
	
	band4 = input(" Please Enter Colour for Band 4  ").lower()#multiplier
	if band4 == "black":
		res4 = 1
	if band4 == "brown":
		res4 = 10
	if band4 == "red":
		res4 = 100
	if band4 == "orange":
		res4 = 1000
	if band4 == "yellow":
		res4 = 10000
	if band4 == "green":
		res4 = 100000
	if band4 == "blue":
		res4 = 1000000
	if band4 == "violet":
		res4 = 10000000
	if band4 == "grey":
		res4 = 0
	if band4 == "white":
		res4 = 0
	if band4 == "gold":
		res4 = 0.1
	if band4 == "silver":
		res4 = 0.01
		
	band5 = input(" Please Enter Colour for Band 5  ").lower() #tolerance
	if band5 == "black":
		res5 = 0
	if band5 == "brown":
		res5 = 1
	if band5 == "red":
		res5 = 2
	if band5 == "orange":
		res5 = 2
	if band5 == "yellow":
		res5 = 2
	if band5 == "green":
		res5 = 0.5
	if band5 == "blue":
		res5 = 0.25
	if band5 == "violet":
		res5 = 0.10
	if band5 == "grey":
		res5 = 0.05
	if band5 == "white":
		res5 = 0
	if band5 == "gold":
		res5 = 5
	if band5 == "silver":
		res5 = 10
		
	print("\n")
	print("  BAR 1 - VALUE",res1)
	print("  BAR 2 - VALUE",res2)
	print("  BAR 3 - VALUE",res3)
	print("  BAR 4 - MULTIPLIER",res4)
	print("  BAR 5 - TOLERANCE",res5,"%","\n")
	total1 = int((res2 * 10) + (res1 *100) + (res3)) # work out 3 places
	print("\n","TOTAL IS",total1,"X MULTIPLIER",res4,"WITH A TOLERANCE OF +/-",res5,"PERCENT","\n")
	total2 = int(total1 * res4) # take total of bar1 bar2 bar3 and multiply by multiplier
	total3 = (total2/1000) # divide by 1000 to get 'K'
	print("       RESISTOR IS ",bblue,total3,whitblac,"K Ohms")
	
	
def colband_check(): # Work out resistor value from colour bars
	print("\033[H")
	print("                    ",bblue1,"RESISTOR COLOUR BAND CHECKER",whitblac + "\n")
	print("               ENTER THE COLOURS OF YOUR RESISTOR BANDS")
	print("\n","                        COLOURS AVAILABLE ARE" + "\n") 
	print("    BLACK BROWN RED ORANGE YELLOW GREEN BLUE VIOLET GREY WHITE SILVER GOLD" + "\n\n")
	fofive = input("    IS THIS A 4 OR 5 BAND RESISTOR    ")
	if fofive == "4":
		respic4()
		gofour()
	if fofive == "5":
		respic5()
		gofive()
	print("\n   PRESS",bblue, "1",whitblac,"FOR CHARTS ",bblue,"2",whitblac," FOR CALCULATOR ",bblue,"3",whitblac, "FOR COLOUR CHECKER",whitblac)
		
		
# Main Page Heading		
print("   ",bblue,"     RESISTOR POWER CALCULATOR AND COLOUR CHARTS    ",whitblac)
print("\n               WHICH WOULD YOU LIKE ")
print("\n       PRESS ",bblue," 1 ",whitblac, " FOR RESISTOR COLOUR CHARTS")
print("\n       PRESS ",bblue," 2 ",whitblac," FOR LED / RESISTOR CALCULATOR")
print("\n       PRESS ",bblue," 3 ",whitblac," FOR RESISTOR COLOUR BAR CHECKER \n")
print("\n       PRESS ",bblue," Cntr/C ",whitblac,"  TO EXIT")

# Main Code Loop
while True:
	
	print ("\033[?25l") # hide cursor
	# print ("\033[?25h") # bring cursor back
	
	choice = input() # Get user input
	
	myclear()
	if choice == "1":
		myclear()
		print("\033[H")
		fourbar()
		print("\n")
		fivebar()
		respic()
	if choice == "2":
		myclear()
		respower()
	if choice == "3":
		myclear()
		colband_check()
		
		 
 
 



