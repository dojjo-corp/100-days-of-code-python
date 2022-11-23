import turtle as t
import random
import colorgram

tim = t.Turtle()
t.colormode(255)
tim.speed('fastest')
raw_colors = colorgram.extract('image.jpg', 20)
colors = []
print(colors)
for item in colors:
    
    colors.append(item)

def rgb():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


screen = t.Screen()
screen.exitonclick()