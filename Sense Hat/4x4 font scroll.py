#4x4 font scrolling through an 8x8 matrix
# (c) Ted Hensman @ galaxysoft 2025

# IMPORT the required libraries (sense_hat, time) 
from sense_hat import SenseHat
from time import sleep

# CREATE a sense object
sense = SenseHat()

# Set up the colours (red, empty)

r = (255, 0, 0)
e = (0, 0, 0)
   
# Create Design images for 4x4 font

# Alphabet data here 4x4 in a 64 bit matrix
a = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,r,e,e,e,e,e,e,
r,e,r,e,e,e,e,e,
r,r,r,e,e,e,e,e,
r,e,r,e,e,e,e,e
]

b = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
r,e,e,e,e,e,e,e,
r,r,r,e,e,e,e,e,
r,e,r,e,e,e,e,e,
r,r,r,e,e,e,e,e
]

c = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,r,r,e,e,e,e,e,
r,e,e,e,e,e,e,e,
r,e,e,e,e,e,e,e,
e,r,r,e,e,e,e,e
]

d = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
r,r,e,e,e,e,e,e,
r,e,r,e,e,e,e,e,
r,e,r,e,e,e,e,e,
r,r,e,e,e,e,e,e
]

E = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
r,r,r,e,e,e,e,e,
r,e,e,e,e,e,e,e,
r,r,e,e,e,e,e,e,
r,r,r,e,e,e,e,e
]

f = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
r,r,r,e,e,e,e,e,
r,e,e,e,e,e,e,e,
r,r,e,e,e,e,e,e,
r,e,e,e,e,e,e,e
]

g = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,r,r,r,e,e,e,e,
r,e,e,e,e,e,e,e,
r,e,r,r,e,e,e,e,
e,r,r,r,e,e,e,e
]

h = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
r,e,e,e,e,e,e,e,
r,r,r,e,e,e,e,e,
r,e,r,e,e,e,e,e,
r,e,r,e,e,e,e,e
]

i = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,r,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,r,e,e,e,e,e,e,
e,r,e,e,e,e,e,e
]

j = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
r,r,r,r,e,e,e,e,
e,e,r,e,e,e,e,e,
r,e,r,e,e,e,e,e,
r,r,r,e,e,e,e,e
]

k = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
r,e,e,r,e,e,e,e,
r,e,r,e,e,e,e,e,
r,r,r,e,e,e,e,e,
r,e,e,r,e,e,e,e
]

l = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
r,e,e,e,e,e,e,e,
r,e,e,e,e,e,e,e,
r,e,e,e,e,e,e,e,
r,r,r,e,e,e,e,e
]

m = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
r,e,e,r,e,e,e,e,
r,r,r,r,e,e,e,e,
r,e,e,r,e,e,e,e,
r,e,e,r,e,e,e,e
]

n = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
r,e,e,e,e,e,e,e,
r,r,r,r,e,e,e,e,
r,e,e,r,e,e,e,e,
r,e,e,r,e,e,e,e
]

o = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,r,r,e,e,e,e,e,
r,e,e,r,e,e,e,e,
r,e,e,r,e,e,e,e,
e,r,r,e,e,e,e,e
]

p = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
r,r,e,e,e,e,e,e,
r,e,r,e,e,e,e,e,
r,r,e,e,e,e,e,e,
r,e,e,e,e,e,e,e
]

q = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
r,r,r,e,e,e,e,e,
r,e,r,e,e,e,e,e,
r,r,r,e,e,e,e,e,
e,e,e,r,e,e,e,e
]

R = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
r,r,r,e,e,e,e,e,
r,e,r,e,e,e,e,e,
r,r,r,e,e,e,e,e,
r,e,e,r,e,e,e,e
]

s = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,r,r,r,e,e,e,e,
e,r,e,e,e,e,e,e,
e,e,r,e,e,e,e,e,
r,r,r,e,e,e,e,e
]

t = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
r,r,r,e,e,e,e,e,
e,r,e,e,e,e,e,e,
e,r,e,e,e,e,e,e,
e,r,e,e,e,e,e,e
]

u = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
r,e,e,r,e,e,e,e,
r,e,e,r,e,e,e,e,
r,r,r,r,e,e,e,e,
e,e,e,r,e,e,e,e
]

v = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
r,e,e,r,e,e,e,e,
r,e,e,r,e,e,e,e,
e,r,r,e,e,e,e,e,
e,e,e,e,e,e,e,e
]

w = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
r,e,e,r,e,e,e,e,
r,e,e,r,e,e,e,e,
e,r,r,e,e,e,e,e,
e,r,r,e,e,e,e,e
]


X = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
r,e,e,r,e,e,e,e,
e,r,r,e,e,e,e,e,
e,r,r,e,e,e,e,e,
r,e,e,r,e,e,e,e
]

y = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
r,e,e,r,e,e,e,e,
r,e,e,r,e,e,e,e,
e,r,r,e,e,e,e,e,
r,r,e,e,e,e,e,e
]

z = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
r,r,r,r,e,e,e,e,
e,e,r,e,e,e,e,e,
e,r,e,e,e,e,e,e,
r,r,r,r,e,e,e,e
]

dot = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,r,r,e,e,e,e,e,
e,r,r,e,e,e,e,e
]

colon = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,r,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,r,e,e,e,e,e,e
]

# Number data and maths signs here

one = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,r,r,e,e,e,e,e,
e,e,r,e,e,e,e,e,
e,e,r,e,e,e,e,e,
e,r,r,r,e,e,e,e
]

two = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
r,r,r,r,e,e,e,e,
e,e,r,e,e,e,e,e,
e,r,e,e,e,e,e,e,
r,r,r,r,e,e,e,e
]

three = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
r,r,r,r,e,e,e,e,
e,e,r,r,e,e,e,e,
e,e,e,r,e,e,e,e,
r,r,r,r,e,e,e,e
]

four = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
r,e,e,e,e,e,e,e,
r,e,r,e,e,e,e,e,
r,r,r,r,e,e,e,e,
e,e,r,e,e,e,e,e
]

five = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,r,r,r,e,e,e,e,
e,r,e,e,e,e,e,e,
e,r,r,e,e,e,e,e,
r,r,r,e,e,e,e,e
]

six = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,r,r,r,e,e,e,e,
r,r,e,e,e,e,e,e,
r,e,r,e,e,e,e,e,
r,r,r,e,e,e,e,e
]

seven = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
r,r,r,r,e,e,e,e,
e,e,r,e,e,e,e,e,
e,r,r,e,e,e,e,e,
r,r,e,e,e,e,e,e
]

eight = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,r,r,e,e,e,e,e,
r,e,r,r,e,e,e,e,
r,r,e,r,e,e,e,e,
e,r,r,e,e,e,e,e
]

nine = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
r,r,r,r,e,e,e,e,
r,e,e,r,e,e,e,e,
r,r,r,r,e,e,e,e,
e,e,e,r,e,e,e,e
]

zero = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,r,r,e,e,e,e,e,
r,e,e,r,e,e,e,e,
r,e,e,r,e,e,e,e,
e,r,r,e,e,e,e,e
]

plus = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,r,e,e,e,e,e,e,
r,r,r,e,e,e,e,e,
e,r,e,e,e,e,e,e,
e,e,e,e,e,e,e,e
]

minus = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
r,r,r,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e
]

times = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
r,e,e,r,e,e,e,e,
e,r,r,e,e,e,e,e,
e,r,r,e,e,e,e,e,
r,e,e,r,e,e,e,e
]

div = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,r,e,e,e,e,
e,e,r,e,e,e,e,e,
e,r,e,e,e,e,e,e,
r,e,e,e,e,e,e,e
]

equ = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
r,r,r,e,e,e,e,e,
e,e,e,e,e,e,e,e,
r,r,r,e,e,e,e,e
]

perc = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
r,e,e,r,e,e,e,e,
e,e,r,e,e,e,e,e,
e,r,e,e,e,e,e,e,
r,e,e,r,e,e,e,e
]

# Miscillanious Charachters here

blank = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e
]

block = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
r,r,r,r,e,e,e,e,
r,r,r,r,e,e,e,e,
r,r,r,r,e,e,e,e,
r,r,r,r,e,e,e,e
]

revb = [
r,r,r,r,r,r,r,r,
r,r,r,r,r,r,r,r,
r,r,r,r,r,r,r,r,
r,r,r,r,r,r,r,r,
e,e,e,e,r,r,r,r,
e,e,e,e,r,r,r,r,
e,e,e,e,r,r,r,r,
e,e,e,e,r,r,r,r
]


dice1 = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,r,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e
]
dice2 = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,r,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,r,e,e,e,e,e,e
]

dice3 = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
r,e,e,e,e,e,e,e,
e,r,e,e,e,e,e,e,
e,e,r,e,e,e,e,e,
e,e,e,e,e,e,e,e
]

dice4 = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
r,e,r,e,e,e,e,e,
e,e,e,e,e,e,e,e,
r,e,r,e,e,e,e,e
]

dice5 = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
r,e,r,e,e,e,e,e,
e,r,e,e,e,e,e,e,
r,e,r,e,e,e,e,e
]

dice6 = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
r,e,r,e,e,e,e,e,
e,r,e,e,e,e,e,e,
r,e,r,e,e,e,e,e,
e,r,e,e,e,e,e,e
]

aup = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,r,e,e,e,e,e,e,
r,r,r,e,e,e,e,e,
e,r,e,e,e,e,e,e,
e,r,e,e,e,e,e,e
]

adn = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,r,e,e,e,e,e,e,
e,r,e,e,e,e,e,e,
r,r,r,e,e,e,e,e,
e,r,e,e,e,e,e,e
]

art = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,r,e,e,e,e,e,
r,r,r,r,e,e,e,e,
e,e,r,e,e,e,e,e
]

alf = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,r,e,e,e,e,e,e,
r,r,r,r,e,e,e,e,
e,r,e,e,e,e,e,e
]

qst = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
r,r,r,r,e,e,e,e,
r,e,e,r,e,e,e,e,
e,e,r,e,e,e,e,e,
e,e,r,e,e,e,e,e
]


 # DISPLAY the Charachters
while True :
    abet = [a,b,c,d,E,f,g,h,i,j,k,l,m,n,o,p,q,R,s,t,u,v,w,X,y,z,
            dot,colon,one,two,three,four,five,six,seven,eight,nine,zero,
            perc,plus,minus,times,div,equ,blank,block,revb,qst,
            dice1,dice2,dice3,dice4,dice5,dice6,aup,adn,art,alf]
    for x in abet:
            sense.clear()
            sense.set_pixels(x)
            sleep(0.4)
  

    