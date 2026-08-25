# Código feito para o Reeborg's World.
# As funções abaixo são fornecidas pelo Reeborg.
def turn_right():
    turn_left()
    turn_left()
    turn_left()


def move_ahead():
    if wall_on_right() and front_is_clear():
        move()
    elif right_is_clear():
        turn_right()
        move()
    else:
        turn_left()


while not at_goal():
    move_ahead()
