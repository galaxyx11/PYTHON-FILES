# example to show sortimg with lambda
from time import sleep

# function to clear terminal screen
def myclear():
    for c in range (1,20):
        print("\n")
    
# function to print a line
def myline():
    print("\n")

# define list to sort ie  a members list/ list is 3 column and any no of rows
members = [["hensman","ted",70],["hensman","dave",49],["smith","andy",29],
["bolton","maria",23],["bailey","sam",19]]

# sort on column 1/2/3 ect /ascending/age is column 2
memberup =sorted(members,key=lambda x:x[2])

# sort on column 1/2/3 ect /descending/age is column 2
memberdown =sorted(members,key=lambda x:x[2],reverse = True)

# sort on surname/surname is column 0
membersur = sorted(members,key=lambda x:x[0])

# sort on first name /firstname is column 1
memberfirst = sorted(members,key=lambda x:x[1])


myclear()

# print list to terminal
print("LISI IN ASCENDING ORDER OF AGE" + "\n")
for t in range (len(members)):
    print(memberup[t])

sleep(2)
myline()

# print list to terminal
print("LISI IN DESENDING ORDER OF AGE" + "\n")
for t in range (len(members)):
    print(memberdown[t])
    
sleep(2)
myline()
                 
# print list to terminal
print("LIST IN ORDER OF SURNAME" + "\n")
for t in range (len(members)):
    print(membersur[t])
    
sleep(2)
myline()
                 
# print list to terminal
print("LIST IN ORDER OF FIRST NAME" + "\n")
for t in range (len(members)):
    print(memberfirst[t])
    