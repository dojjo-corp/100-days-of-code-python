# etch-a-sketch program

from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def forward():
    tim.fd(10)


def turn_right():
    tim.right(10)


def turn_left():
    tim.left(10)


def reverse():
    tim.back(10)


def clear():
    tim.pu()
    tim.clear()
    tim.home()
    tim.pd()


screen.listen()
screen.onkey(fun=forward, key='w')
screen.onkey(fun=reverse, key='s')
screen.onkey(fun=turn_right, key='d')
screen.onkey(fun=forward, key='w')
screen.onkey(fun=turn_left, key='a')
screen.onkey(fun=clear, key='c')






screen.exitonclick()