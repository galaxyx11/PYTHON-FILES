from time import sleep

# a = 4.5
# b = 6
# area = a*b/2
# pname = "Dave"
# print("Area =",area)
# hiscore = 25
# print(pname,"Your score is",hiscore,"\nGOODBYE","\nGOODBYE")
# print("\tWIDTH"+"\tHEIGHT "+"\tAREA ")  # \n newline \t tab 
# print("\t",a,"\t ",b,"\t",area)

# define a function/this one clears screen
def newline():
    for nl in range(0,25):
        print("\n")
        

# define function print ascii charachters
def prasc():
    for s in range(33,127):
        x = chr(s)
        print(x,end = " ")

# call the functions  
newline()
prasc()



 

    