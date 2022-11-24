from turtle import Turtle, Screen
import time

screen = Screen()
screen.bgcolor('black')
screen.title("Dojjo's Snake Game")
screen.setup(width=600, height=600)
# puase screen display until 
screen.tracer(0)
snake_body = []

screen.tracer(0)
x_pos = 0
for _ in range(3):
    new_body = Turtle('square')
    new_body.pu()
    new_body.color('white')
    new_body.setx(x_pos)
    snake_body.append(new_body)
    x_pos -= 20


game_end = False
while game_end == False:
    screen.update()
    time.sleep(0.1)
    
    for _ in range(len(snake_body)-1, 0, -1):
        if snake_body[0].xcor() == 380:
            game_end = True
            break
        previous_loc = snake_body[_ - 1].pos()
        snake_body[_].goto(previous_loc)
    snake_body[0].fd(20)

screen.exitonclick()
