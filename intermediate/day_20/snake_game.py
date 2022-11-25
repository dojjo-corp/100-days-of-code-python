from turtle import Turtle, Screen
import time

screen = Screen()
screen.bgcolor('black')
screen.title("Dojjo's Snake Game")
screen.setup(width=600, height=600)
# pause screen display until
screen.tracer(0)
snake_body = []

screen.tracer(0)
x_pos = 0


# create initial snake body (3 squares adjoined side by side)
for _ in range(3):
    new_body = Turtle('square')
    new_body.pu()
    new_body.color('white')
    new_body.setx(x_pos)
    snake_body.append(new_body)
    x_pos -= 20


def move_snake():
    for _ in range(len(snake_body)-1, 0, -1):
        if snake_body[0].xcor() == 380:
            game_end = True
            break
        previous_loc = snake_body[_ - 1].pos()
        snake_body[_].goto(previous_loc)
    snake_body[0].fd(20)


def turn_right():
    snake_body[0].setheading(0)
    # move_snake()


def turn_left():
    snake_body[0].setheading(180)
    # move_snake()


def up():
    snake_body[0].setheading(90)
    # move_snake()


def down():
    snake_body[0].setheading(270)


game_end = False
while not game_end:
    screen.update()
    time.sleep(0.1)
    
    screen.listen()
    screen.onkey(fun=up, key='Up')
    screen.onkey(fun=down, key='Down')
    screen.onkey(fun=turn_left, key='Left')
    screen.onkey(fun=turn_right, key='Right')
    move_snake()
screen.exitonclick()
