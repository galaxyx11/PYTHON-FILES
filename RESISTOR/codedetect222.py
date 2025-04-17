 # code to work out resistor power from colour codes
 

# Define Colours Ansi Codes
whitblac = ("\033[1;37;40m")
blacwhit = ("\033[1;30;47m")
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

def myclear():
	for i in range (1,30):
		print("\n")
		print("\033[H")
				

def respic4(): # Resistor pic 4 bar
	print("\n")
	print("          ",whitblac,"------",blue1,"1",white1,"  ",red1,"2",white1,\
	"  ",green1,"M",white1,"  ",violet1,"T",whitblac,"------")
	print("\n"," Example ---- 625 x 100K = 625K ohm with a tolerance of +/- 0.10%"+"\n")
	

def respic5(): # Resistor pic 5 bar
	print("\n")
	print("          ",whitblac,"------",blue1,"1",white1,"  ",red1,"2",white1,"  ",brown1,"3",white1,\
	"  ",green1,"M",white1,"  ",violet1,"T",whitblac,"------")
	print("\n"," Example ---- 621 x 100K = 621K ohm with a tolerance of +/- 0.10%","\n")


def gofour():
	print("\n" + "     FOUR BAND RESISTORS HAVE 2 VALUES + MULTIPLIER + TOLERANCE" +"\n"+"\n")
	band1 = input(" Please Enter Colour for Band 1  ")
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
		
	band2 = input(" Please Enter Colour for Band 2  ")
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
		
	band3 = input(" Please Enter Colour for Band 3  ")#multiplier
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
	if band3 == "silver":
		res3 = 0.1
	if band3 == "gold":
		res3 = 0.01
	
		
	band4 = input(" Please Enter Colour for Band 4  ")#tolerance
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
	if band4 == "silver":
		res4 = 5
	if band4 == "gold":
		res4 = 10
	print("\n")
	print("BAR 1 - VALUE",res1)
	print("BAR 2 - VALUE",res2)
	print("BAR 3 - MULTIPLIER",res3)
	print("BAR 4 - TOLERANCE",res4,"%","\n")
	total1 = int((res1 * 10) + (res2))# work out 1st 2 places
	print("\n","TOTAL IS",total1,"X MULTIPLIER",res3,"WITH A TOLERANCE OF +/-",res4,"PERCENT","\n")
	total2 = int(total1 * res3) # take total of bar1 and bar2 and multiply by multiplier
	total3 = (total2/1000) # divide by 1000 to get 'K'
	print("       RESISTOR IS",total3,"K Ohms")
		
	
def gofive():
	print("\n" + "     FIVE BAND RESISTORS HAVE 3 VALUES + MULTIPLIER + TOLERANCE" +"\n")
	band1 = input(" Please Enter Colour for Band 1  ")
	
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
		
	band2 = input(" Please Enter Colour for Band 2  ")
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
		
	band3 = input(" Please Enter Colour for Band 3  ")
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
		
	
	band4 = input(" Please Enter Colour for Band 4  ")#multiplier
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
	if band4 == "silver":
		res4 = 0.1
	if band4 == "gold":
		res4 = 0.01
		
	band5 = input(" Please Enter Colour for Band 5  ") #tolerance
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
	if band5 == "siver":
		res5 = 5
	if band5 == "gold":
		res5 = 10
		
		
		
	print("\n")
	print("BAR 1 - VALUE",res1)
	print("BAR 2 - VALUE",res2)
	print("BAR 3 - VALUE",res3)
	print("BAR 4 - MULTIPLIER",res4)
	print("BAR 5 - TOLERANCE",res5,"%","\n")
	total1 = int((res2 * 10) + (res1 *100) + (res3)) # work out 3 places
	print("\n","TOTAL IS",total1,"X MULTIPLIER",res4,"WITH A TOLERANCE OF +/-",res5,"PERCENT","\n")
	total2 = int(total1 * res4) # take total of bar1 bar2 bar3 and multiply by multiplier
	total3 = (total2/1000) # divide by 1000 to get 'K'
	print("       RESISTOR IS",total3,"K Ohms")
	
	
	
myclear()
print("                    ",bblue1,"RESISTOR COLOUR BAND CHECKER",whitblac + "\n")
print("                         COLOURS AVAILABLE ARE" + "\n") 
print("    BLACK BROWN RED ORANGE YELLOW GREEN BLUE VIOLET GREY WHITE SILVER GOLD" + "\n")
fofive= input("    IS THIS A 4 OR 5 BAND RESISTOR    ")
if fofive == "4":
	respic4()
	gofour()
	input()
if fofive == "5":
	respic5()
	gofive()
	input()


 
 
 
