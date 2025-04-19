# imports
from datetime import datetime
from random import randint

# variables
world = '🌍🌎🌏'
python = 'Python 🐍'
fire = '🔥'
dice = '🎲'

# Function definitions
def roll_dice():
    max = input("How many sides on your dice?:")
    print(f"That is a D {max}")
    roll = randint(1, int(max))
    print(f"You rolled a {roll} {fire + (dice * roll) + fire}")
    
# Put code to run under here
print(f"Hello {world}")
print(f"Welcome to {python}")
# print(f"{python} is good at maths!")
# print(f"{111111111 * 111111111}")
print(f"The date and time is {datetime.now()}")
roll_dice()

