from turtle import *
import turtle as t

def my_turtle():
    side =str(4)
    loops =str(280)
    pen =5
    for i in range(int(loops)):
        forward(i * 2/int(side)+i)
        right(180/int(side) +.150)
        hideturtle()
        pensize(4)
        pencolor("black")
        speed(200)
        right(180)
my_turtle()
t.done()
