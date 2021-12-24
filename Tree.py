import turtle

import time as tm

from turtle import *

from random import *

# star background

s = Screen()

s.title(' + @ ')

w, h = 700, 700

s.setup(w, h)

s.bgcolor('black')

star = Turtle()

star.shape('circle')

star.shapesize(0.2,0.2)

star.color('white')

star.pu()

star.speed('fastest')

for i in range(130):

    x = randint(-w, w)

    y = randint(-h/2, h)

    star.goto(x, y)

    star.stamp()

    turtle.color('white')

    style = ('Courier', 10, 'italic')

    turtle.write("print('It's Christmas')\n\n\n\n\n\n\n\n\n\n\n\n\n\n", font=style, align='center')

    turtle.write('',align='center')

#    turtle.hideturtle()

#moon 1

cycle = Turtle()

cycle.ht()  #turtle.hideturtle()

cycle.speed(99999)

cycle.color('white')

cycle.pu()

cycle.pensize(3)

radius = 5  #Circle radius

acc_ext = 0  #Cumulative arc

for i in range(250):

    extent = random() * 90  #0 to 90 random number, the length of the arc drawn each time is random

    color = choice([(1,1,1),(0/255, 0/255, 0/255)])  #White and black are randomly selected

    cycle.color(color)

    cycle.circle(radius, extent)

    acc_ext += extent  #Statistical arc length

    if acc_ext > 360:  #If exactly one circle, the radius increases by 3

        acc_ext = 0

        radius += 3

        cycle.penup()

        cycle.goto(370,640)  #The starting point of each circle of the brush is the next radius of the center of the circle

        cycle.pendown()  #pendown , ready to start over

        cycle.setheading(100)  # Put your head straight, the direction is 0 degrees to the right

#moon2

cycle = Turtle()

cycle.ht()  

cycle.speed(99999)

cycle.color('white')

cycle.pu()

cycle.pensize(2)

radius = 5  

acc_ext = 0  

for i in range(100):

    extent = random() * 90 

    color = choice([(1,1,1),(0/255, 0/255, 0/255)])  

    cycle.color(color)

    cycle.circle(radius, extent)

    acc_ext += extent  

    if acc_ext > 360:  

        acc_ext = 0

        radius += 3

        cycle.penup()

        cycle.goto(-200,580) 

        cycle.pendown()  

        cycle.setheading(180)  

#moon3

cycle = Turtle()

cycle.ht()  

cycle.speed(99999)

cycle.color('white')

cycle.pu()

cycle.pensize(1)

radius = 5  

acc_ext = 0  

for i in range(120):

    extent = random() * 90  

    color = choice([(1,1,1),(0/255, 0/255, 0/255)])  

    cycle.color(color)

    cycle.circle(radius, extent)

    acc_ext += extent  

    if acc_ext > 360:  

        acc_ext = 0

        radius += 3

        cycle.penup()

        cycle.goto(-390,240)  

        cycle.pendown()  

        cycle.setheading(-50)

        

#moon4

cycle = Turtle()

cycle.ht()  

cycle.speed(99999)

cycle.color('white')

cycle.pu()

cycle.pensize(1)

radius = 5  

acc_ext = 0  

for i in range(140):

    extent = random() * 90  

    color = choice([(1,1,1),(0/255, 0/255, 0/255)]) 

    cycle.color(color)

    cycle.circle(radius, extent)

    acc_ext += extent  

    if acc_ext > 360:  

        acc_ext = 0

        radius += 3

        cycle.penup()

        cycle.goto(-400,380)  

        cycle.pendown()  

        cycle.setheading(50)  

n = 200

#turtle.goto(0, -20)

#star

turtle.pensize(4)

turtle.speed('fastest')

turtle.left(90)

turtle.forward(3*n)

#turtle.color('#ffae42')

turtle.color('white')

turtle.begin_fill()

turtle.left(126)

turtle.pendown()

for _ in range(5):

    turtle.forward(n/5)

    turtle.right(144)

    turtle.forward(n/5)

    turtle.left(72)

turtle.end_fill()

turtle.right(126)

#tree

#turtle.pencolor('#01281a')

turtle.pencolor('white')

turtle.back(n*4.8)

def tree(d,s):

    if d <= 0:

        return

    turtle.forward(s)

    tree(d-1, s*.8)

    turtle.right(120)

    tree(d-3, s*.5)

    turtle.right(120)

    tree(d-3, s*.5)

    turtle.right(120)

    turtle.back(s)

 

turtle.pendown()

turtle.pencolor('white')

tree(15, n)

turtle.back(n/2)

#bucket

turtle.color('white')

turtle.begin_fill()

turtle.left(90)

turtle.forward(-100)

turtle.left(60)

turtle.forward(100)

turtle.right(60)

turtle.forward(100)

turtle.left(300)

turtle.forward(100)

turtle.left(60)

turtle.forward(-200)

turtle.left(60)

turtle.end_fill()

turtle.penup()

turtle.goto(0, -120)

tm.sleep(20)

while True:

	pass
