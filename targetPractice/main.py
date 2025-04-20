#!/usr/bin/env python3

# Import library code
from p5 import *
from random import randint

# The mouse_pressed function goes here



# The shoot_arrow function goes here



def setup():
    # Setup your game here
    size(400, 400)
    no_stroke()


def draw():
    # Things to do in every frame
    fill('cyan')
    rect(0, 0, 400, 250)
    fill("lightgreen")
    rect(0, 250,400,150)
    fill("sienna")
    triangle(150, 350, 200, 150, 250, 350)
    fill("blue")
    circle(200, 200, 170)
    fill("red")
    circle(200, 200, 110)
    fill("yellow")
    circle(200, 200, 30)


# Keep this to run your code
run(frame_rate=2)

