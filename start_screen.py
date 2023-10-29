from turtle import Turtle

start_screen = []


def create_start_screen():
    title = Turtle()
    title.pu()
    title.ht()
    title.color("white")
    title.goto(0, 200)
    title.write("PONG", align="center", font=("Arial", 48, "normal"))
    start_screen.append(title)

    press_start = Turtle()
    press_start.pu()
    press_start.ht()
    press_start.color("white")
    press_start.goto(0, 80)
    press_start.write("Press Enter to start game", align="center", font=("Arial", 28, "normal"))
    start_screen.append(press_start)

    controls = []
    lines = ["Controls (Up, Down):", "Player 1: W, S", "Player 2: I, K"]
    for _ in range(3):
        new_line = Turtle()
        new_line.pu()
        new_line.ht()
        new_line.color("white")
        new_line.goto(-200, -50-_*50)
        new_line.write(lines[_], align="left", font=("Arial", 18, "normal"))
        start_screen.append(new_line)

def hide_start_screen():
    for _ in start_screen:
        _.reset()