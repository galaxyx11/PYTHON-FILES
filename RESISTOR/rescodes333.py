# resistor code charts (C)2025 Ted H @ Galaxysoft.co.uk

# define colours
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


def myclear():
	for i in range (1,30):
		print("\033[H")
		
def respic():
	print("\n")
	print("        ",whitblac," ------",blue,"1",white,"  ",red,"2",white,"  ",brown,"3",white,\
	"  ",green,"M",white,"  ",violet,"T",whitblac,"------")
	print(" Example ---- 621 x 100K = 621K ohm with a tolerance of +/- 0.10%")
		
		
def fivebar(): # 5 bar chart
	print("                    ",bblue," FIVE BAR RESISTOR CODE CHART",whitblac,"\n")
	print("  -------------------------------------------------------------------")		
	print("            1st BAR     2nd BAR     3rd BAR   MULTIPLIER   TOLERANCE")
	print("  -------------------------------------------------------------------")
	print(" ",whitblac," BLACK      0           0           0       1    ohm      N\A",whitblac)
	print(" ",brown," BROWN      1           1           1       1O   ohm     +/- 1%  ",whitblac)
	print(" ",red," RED        2           2           2       100  ohm     +/- 2%  ",whitblac)
	print(" ",blacwhit," ORANGE     3           3           3       1K   ohm     +/- 2%  ",whitblac)
	print(" ",yellow," YELLOW     4           4           4       10K  ohm     +/- 2%  ",whitblac)
	print(" ",green," GREEN      5           5           5       100K ohm     +/-0.5% ",whitblac)
	print(" ",blue," BLUE       6           6           6       1M   ohm     +/-0.25%",whitblac)
	print(" ",violet," VIOLET     7           7           7       10M  ohm     +/-0.10%",whitblac)
	print(" ",grey," GREY       8           8           8         N/A          N/A   ",whitblac)
	print(" ",white," WHITE      9           9           9         N/A          N/A   ",whitblac)
					

def fourbar(): # four bar chart
	print("                     ",bblue," FOUR BAR RESISTOR CODE CHART",whitblac,"\n")
	print("     ------------------------------------------------------------")		
	print("            1st BAR     2nd BAR     MULTIPLIER   TOLERANCE")
	print("     ------------------------------------------------------------")
	print("    ",whitblac," BLACK      0           0           1  ohm       N\A",whitblac)
	print("    ",brown," BROWN      1           1           1O   ohm     +/- 1%  ",whitblac)
	print("    ",red," RED        2           2           100  ohm     +/- 2%  ",whitblac)
	print("    ",blacwhit," ORANGE     3           3           1K   ohm     +/- 2%  ",whitblac)
	print("    ",yellow," YELLOW     4           4           10K  ohm     +/- 2%  ",whitblac)
	print("    ",green," GREEN      5           5           100K ohm     +/-0.5% ",whitblac)
	print("    ",violet," VIOLET     7           7           10M  ohm     +/-0.10%",whitblac)
	print("    ",grey," GREY       8           8             N/A          N/A  ",whitblac)
	print("    ",white," WHITE      9           9             N/A          N/A   ",whitblac)


myclear()	
fourbar()
print()
fivebar()
respic()
input()

