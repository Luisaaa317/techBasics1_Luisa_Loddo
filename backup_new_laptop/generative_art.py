from turtle import *
import random
# initial setup: canvas size
width = 400
height = 400
setup(width, height)

# turn off animation, comment it out to see the drawing process
tracer(0, 0)
# set background color
bgcolor('white') # You can either use color names
# change the color of the lines
color('#000') # Or Hex Code

#parameter
size = 50
noise = 1


for i in range(5):
    penup()
    goto(-200+i*size, y=100)
    pendown()
    right(noise)
    angle = random.uniform(-noise, noise)

    for i in range(4):
        forward(size) # draw from starting point, go forward
        right(90) # turn right 90 degree


penup()

#quit
exitonclick()


