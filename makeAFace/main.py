from p5 import *

screen_size = 400

def setup():
    # Put code to run once here
    size(screen_size, screen_size) 
    rect_mode(CENTER)


def draw():
    # Put code to run every frame here
    background(255, 63, 127)
    # Add code to draw your face here
    fill(255, 0, 0)
    stroke(0, 0, 255)
    stroke_weight(5)
    ellipse(
        screen_size/2,
        screen_size/2,
        150,
        220
    )

# Keep this to run your code
run()

