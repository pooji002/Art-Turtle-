import turtle
from turtle import Turtle,Screen
import random
tut=Turtle()

tut.shape("turtle")
tut.color("purple1")
turtle.colormode(255)

#----drawing shapes-----
# color=["red","green","pink","purple","orange","black"]
# def shapes_draw(sides):
#     angle = 360 / sides
#     for _ in range(sides):
#         tut.forward(100)
#         tut.right(angle)
# for side_shape in range(3,11):
#     tut.color(random.choice(color))
#     shapes_draw(side_shape)
#---------Random walk--------------
# def random_color():
#         r=random.randint(0,255)
#         g = random.randint(0, 255)
#         b = random.randint(0, 255)
#         random_color=(r,g,b)
#         return random_color
# dir=[0,90,180,270]
# tut.pensize(10)
# tut.speed(5)
# for _ in range(200):
#         tut.color(random_color())
#         tut.setheading(random.choice(dir))
#         tut.forward(100)
#---draw circle---
tut.speed("fastest")
def random_color():
        r=random.randint(0,255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        random_color=(r,g,b)
        return random_color
def spirograph(size):
        for _ in range(int(360/size)):
                tut.color(random_color())
                tut.circle(100)
                tut.setheading(tut.heading()+size)
spirograph(2)

















sc=Screen()
sc.exitonclick()

