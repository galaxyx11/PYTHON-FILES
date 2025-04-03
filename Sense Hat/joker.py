# jokes from http://www.laughfactory.com/jokes/word-play-jokes

from sense_hat import SenseHat
import random
from time import sleep

sense = SenseHat()
jokes = [
    "What happens to a frog's car when it breaks down?       It gets toad away",
    "Why was six scared of seven?                Because seven eight nine",
    "What do you call a bear with no teeth?           A gummy bear",
    "How do you count cows?           With a cowculator",
    "How do astronomers organize a party?             They Planet . . .",
    "Why does Humpty Dumpty love autumn?              Because He had a great fall   Ha Ha Ha",
    "I went to the bank the other day and asked the teller to check my balance,    so she pushed me !   Get it",
    "Can a kangaroo jump higher than the Empire State Building?      Of course. The Empire State Building can't jump",
    "Did you hear about the kidnapping at school?        It's ok.   He woke up ! ! !",
    "A man got hit in the head with a can of Coke,    but he was ok     it was a soft drink",
]

while True:
    joke = random.choice(jokes)
    speed = 0.05
    text = (0,255,0)
    back = (0,0,0)
    sense.show_message(joke,speed,text,back)
    sleep(5)
