from turtle import Turtle, Screen


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.segments_num = 5
        self.location = [0, 0 + self.segments_num / 2]
        self.segments = []
        self.create_paddle()
        self.pad_dir = 0

    def create_paddle(self):
        for _ in range(self.segments_num):
            paddle_part = Turtle()
            paddle_part.pu()
            paddle_part.color("white")
            paddle_part.shape("square")
            paddle_part.goto(self.location[0], self.location[1] - _ * 20)
            self.segments.append(paddle_part)
        Screen().update()

    def move_paddle_up(self):
        for _ in reversed(range(len(self.segments))):
            if self.segments[0].ycor() < 380:
                if _ == 0:
                    self.segments[_].setheading(90)
                    self.segments[_].forward(20)
                else:
                    self.segments[_].goto(self.segments[_-1].pos())

    def move_paddle_down(self):
        for _ in (range(len(self.segments))):
            if self.segments[4].ycor() > -360:
                if _ == 4:
                    self.segments[_].setheading(270)
                    self.segments[_].forward(20)
                else:
                    self.segments[_].goto(self.segments[_+1].pos())

    x_cor = 0

    def set_x_cor(self):
        for segment in self.segments:
            segment.goto(self.x_cor, segment.ycor())

    def set_pad_dir_up(self):
        self.pad_dir = 1

    def set_pad_dir_down(self):
        self.pad_dir = -1

    def reset_pad_dir(self):
        self.pad_dir = 0

    def pad_moving(self):
        if self.pad_dir > 0:
            self.move_paddle_up()
        elif self.pad_dir < 0:
            self.move_paddle_down()
