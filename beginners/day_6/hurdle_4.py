def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while not at_goal():
    if not wall_in_front():
        move()
    else:
        turn_left()
        steps = 0
        while not right_is_clear():
            move()
            steps += 1

        turn_right()
        move()
        turn_right()
        for i in range(steps):
            move()
        turn_left()


