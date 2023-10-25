from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time

# create screen

screen = Screen()
screen.setup(width=1200, height=800)
screen.tracer(0)
screen.bgcolor("black")
screen.title("Pong")

paddle_1 = Paddle()
paddle_1.x_cor = -550
paddle_1.set_x_cor()
paddle_2 = Paddle()
paddle_2.x_cor = 550
paddle_2.set_x_cor()
ball = Ball()


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


# paddle movement functions
def move_p_1_up():
    paddle_1.move_paddle_up()
    screen.update()


def move_p_1_down():
    paddle_1.move_paddle_down()
    screen.update()


def move_p_2_up():
    paddle_2.move_paddle_up()
    screen.update()


def move_p_2_down():
    paddle_2.move_paddle_down()
    screen.update()


def move_ball():
    ball.move()


def detect_ball_paddle_collision():
    if ball.xcor() < -540:
        for segment in paddle_1.segments:
            #collision detection debugging print
            #print(f"dir: {ball.movement_dir}, xcor: {ball.xcor()}, dist: {segment.distance(ball)}")
            if ball.distance(segment) < 10:
                if ball.movement_dir == 135:
                    ball.movement_dir = 45
                elif ball.movement_dir == 225:
                    ball.movement_dir = 315
    elif ball.xcor() > 540:
        for segment in paddle_2.segments:
            # collision detection debugging print
            #print(f"dir: {ball.movement_dir}, xcor: {ball.xcor()}, dist: {segment.distance(ball)}")
            if ball.distance(segment) < 10:
                if ball.movement_dir == 45:
                    ball.movement_dir = 135
                elif ball.movement_dir == 315:
                    ball.movement_dir = 225


game_active = True


# key bindings
screen.listen()
screen.onkeypress(paddle_1.set_pad_dir_up, "w")
screen.onkeyrelease(paddle_1.reset_pad_dir, "w")
screen.onkeypress(paddle_1.set_pad_dir_down, "s")
screen.onkeyrelease(paddle_1.reset_pad_dir, "s")
screen.onkeypress(paddle_2.set_pad_dir_up, "i")
screen.onkeyrelease(paddle_2.reset_pad_dir, "i")
screen.onkeypress(paddle_2.set_pad_dir_down, "k")
screen.onkeyrelease(paddle_2.reset_pad_dir, "k")

while game_active:
    move_ball()
    paddle_1.pad_moving()
    paddle_2.pad_moving()
    ball.detect_ball_wall_collide()
    detect_ball_paddle_collision()
    time.sleep(0.025)
    screen.update()


screen.exitonclick()
