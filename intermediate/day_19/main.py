import random
from turtle import Turtle, Screen

tim = Turtle('turtle')
tom = Turtle('turtle')
ben = Turtle('turtle')
ban = Turtle('turtle')
bay = Turtle('turtle')
bet = Turtle('turtle')
screen = Screen()
screen.setup(width=500, height=400)

tim.pu()
tim.color('red')
tim.setpos(-230, -100)

tom.pu()
tom.color('orange')
tom.setpos(-230, -50)

ben.pu()
ben.color('yellow')
ben.setpos(-230, 0)

ban.pu()
ban.color('green')
ban.setpos(-230, 50)

bay.pu()
bay.color('blue')
bay.setpos(-230, 100)

bet.pu()
bet.color('indigo')
bet.setpos(-230, 150)

turtles = [tim, tom, ben, ban, bay, bet]
user_bet = screen.textinput(title='Make a bet!', prompt='Which turtle will win the race? Choose a color!')
is_game_on = True

while is_game_on:

    for obj in turtles:
        if obj.xcor() > 245:
            is_game_on = False
            if user_bet == obj.pencolor():
                print(f"You've won!. The {obj.pencolor()} turtle is the winner!")
            else:
                print(f"You've lost!. The {obj.pencolor()} turtle is the winner!")

        random_paces = random.randint(0, 10)
        obj.fd(random_paces)



screen.exitonclick()