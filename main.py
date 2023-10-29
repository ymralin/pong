from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Score
import random
from start_screen import create_start_screen, hide_start_screen

# create screen

screen = Screen()
screen.setup(width=1200, height=800)
screen.tracer(0)
screen.bgcolor("black")
screen.title("Pong")

create_start_screen()
screen.update()

game_started = False


def start_game():
    screen.onkey(None, "Return")
    hide_start_screen()
    paddle_1 = Paddle()
    paddle_1.x_cor = -550
    paddle_1.set_x_cor()
    paddle_2 = Paddle()
    paddle_2.x_cor = 550
    paddle_2.set_x_cor()
    ball = Ball()
    score_1 = Score()
    score_1.location = (-150, 300)
    score_1.create_score()
    score_2 = Score()
    score_2.location = (120, 300)
    score_2.create_score()

    # create boundary
    boundary = []
    for _ in range(2, int(screen.window_height()/20), 2):
        bound_part = Turtle()
        bound_part.pu()
        bound_part.color("white")
        bound_part.shape("square")
        bound_part.shapesize(1, 0.5)
        bound_part.goto(0, -int(screen.window_height()/2)+_*20)
        boundary.append(bound_part)

    screen.update()

    def move_ball():
        ball.move()

    def detect_ball_paddle_collision():
        if ball.xcor() < -540:
            for segment in paddle_1.segments:
                # collision detection debugging print
                # print(f"dir: {ball.movement_dir}, xcor: {ball.xcor()}, dist: {segment.distance(ball)}")
                if ball.distance(segment) < 10:
                    if ball.movement_dir == 135:
                        ball.movement_dir = 45
                    elif ball.movement_dir == 225:
                        ball.movement_dir = 315
        elif ball.xcor() > 540:
            for segment in paddle_2.segments:
                # collision detection debugging print
                # print(f"dir: {ball.movement_dir}, xcor: {ball.xcor()}, dist: {segment.distance(ball)}")
                if ball.distance(segment) < 10:
                    if ball.movement_dir == 45:
                        ball.movement_dir = 135
                    elif ball.movement_dir == 315:
                        ball.movement_dir = 225

    def detect_point_loss():
        #global game_active
        if ball.xcor() > 560:
            score_1.raise_score()
            ball.goto(0, 0)
            ball.movement_dir = ball.directions[random.randint(0, 3)]
            ball.ball_speed = 5
        elif ball.xcor() < -560:
            score_2.raise_score()
            ball.goto(0, 0)
            ball.movement_dir = ball.directions[random.randint(0, 3)]
            ball.ball_speed = 5


    game_active = True


    # key bindings
    #screen.listen()
    screen.onkeypress(paddle_1.set_pad_dir_up, "w")
    screen.onkeyrelease(paddle_1.reset_pad_dir, "w")
    screen.onkeypress(paddle_1.set_pad_dir_down, "s")
    screen.onkeyrelease(paddle_1.reset_pad_dir, "s")
    screen.onkeypress(paddle_2.set_pad_dir_up, "i")
    screen.onkeyrelease(paddle_2.reset_pad_dir, "i")
    screen.onkeypress(paddle_2.set_pad_dir_down, "k")
    screen.onkeyrelease(paddle_2.reset_pad_dir, "k")

    game_tick = 0
    tick_duration = 0.025

    while game_active:
        move_ball()
        paddle_1.pad_moving()
        paddle_2.pad_moving()
        ball.detect_ball_wall_collide()
        detect_ball_paddle_collision()
        detect_point_loss()
        game_tick += 1
        if game_tick % 200 == 0:
            ball.ball_speed *= 1.1
        time.sleep(tick_duration)
        screen.update()

screen.listen()
screen.onkey(start_game, "Return")


screen.exitonclick()
