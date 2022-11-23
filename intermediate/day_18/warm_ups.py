import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
tim.speed('fastest')


def rgb():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


# ->DRAW a square
def square():
    for i in range(4):
        tim.forward(100)
        tim.right(90)


# ->DASHED lines
def dashed_lines():
    for _ in range(10):
        tim.forward(10)
        tim.pu()
        tim.forward(10)
        tim.pd()


# ->POLYGONS overlapping
# an outer loop to iterate 8 times -> range(3, 11)
def polygons_overlap():
    for _ in range(3, 11):
        tim.pencolor(rgb(), rgb(), rgb())
    #   # for each iteration (_) of the outer loop, the inner loop draws (_) lines
        for line in range(_):
            # each with an angle 360/_, after moving 100 paces
            tim.forward(100)
            tim.right(360/_)

# ->RANDOM walk
def random_walk():
    directions = [0, 90, 180, 270]
    size = 1
    for i in range(200):
        tim.color(rgb(), rgb(), rgb())
        tim.pensize(10)
        tim.setheading(random.choice(directions))
        tim.forward(25)


# SPIROGRAPH
def spirograph():
    # def circle(): alternate method for drawing a circle with turtle
    #     tim.color(rgb())
    #     for i in range(36):
    #         tim.right(10)
    #         tim.fd(10)

    tilt = 5
    num_circles = 360 // tilt
    for i in range(num_circles):
        tim.color(rgb())
        tim.circle(100)
        tim.setheading(tilt)
        tilt += 5

# ***************************************************
# UNCOMMENT THE FUNCTION CALL YOU WANT TO WORK WITH # 
# ***************************************************
# square()
# dashed_lines()
# polygons_overlap()
# random_walk()
# spirograph()

