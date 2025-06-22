# Emanuel Biruk Seifegebreal - 2024 --> This project is for learning purposes

from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(20)


def move_back():
    tim.back(20)


def move_clockwise():
    tim.right(20)


def move_counter_clockwise():
    tim.left(20)

def reset_screen():
    tim.reset()

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_back)
screen.onkey(key="d", fun=move_clockwise)
screen.onkey(key="a", fun=move_counter_clockwise)
screen.onkey(key="c", fun=reset_screen)
screen.exitonclick()
