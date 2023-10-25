from turtle import Turtle, Screen
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.pu()
        self.goto(0, 0)

    directions = [45, 135, 225, 315]

    movement_dir = directions[random.randint(0,3)]
    x_dir = 0
    y_dir = 0

    def move(self):
        if 0 < self.movement_dir < 90:
            self.x_dir = 1
            self.y_dir = 1
        elif 90 < self.movement_dir < 180:
            self.x_dir = -1
            self.y_dir = 1
        elif 180 < self.movement_dir < 270:
            self.x_dir = -1
            self.y_dir = -1
        elif 270 < self.movement_dir < 360:
            self.x_dir = 1
            self.y_dir = -1
        self.goto(self.xcor() + self.x_dir * 5, self.ycor() + self.y_dir * 5)

    def detect_ball_wall_collide(self):
        if self.ycor() > 380:
            if self.movement_dir == 45:
                self.movement_dir = 315
            elif self.movement_dir == 135:
                self.movement_dir = 225
        elif self.ycor() < -370:
            if self.movement_dir == 225:
                self.movement_dir = 135
            elif self.movement_dir == 315:
                self.movement_dir = 45

