from turtle import *
import random

width = 400
height = 400
setup(width, height)

tracer(0, 0)
bgcolor(random.choice(['lightblue', 'white']))
bg_color = bgcolor()
color('#000')

ray_count = 24
ray_length = 120
ray_angle = 360 / ray_count + 1

penup()
goto(0, 0)
pendown()

if bg_color == 'lightblue':
    for i in range(ray_count):
        color('yellow')
        forward(ray_length)
        backward(ray_length)
        right(ray_angle)
        for i in range(ray_count - 1):
            color(random.choice(['lightyellow', 'white', 'gold']))
            forward(ray_length / 2)
            backward(ray_length /2)
            right(ray_angle)
else:
    for i in range(ray_count):
        color('pink')
        forward(ray_length)
        backward(ray_length)
        right(ray_angle)
        for i in range(ray_count - 1):
            color(random.choice(['red', 'magenta', 'orange']))
            forward(ray_length / 2)
            backward(ray_length / 2)
            right(ray_angle)


exitonclick()
