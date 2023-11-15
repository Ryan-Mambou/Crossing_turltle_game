from turtle import Turtle
import random

STARTING_POSITIONS = [(320, 0), (320, 0), (320, -30), (320, -60), (320, -90), (320, -120), (320, -150),
                      (320, -180), (320, -210,), (320, -240), (320, -250), (320, 30), (320, 60), (320, 90),
                      (320, 120), (320, 150), (320, 180), (320, 210,), (320, 240), (320, 250), (320, 0)]

COLORS = ["pink", "yellow", "green", "blue", "red", "violet"]


class BrickManager:
    def __init__(self):
        self.all_bricks = []
        self.create_brick()

    def create_brick(self):
        new_brick = Turtle()
        new_brick.shape("square")
        new_brick.penup()
        new_brick.shapesize(stretch_wid=1, stretch_len=2)
        new_brick.color(random.choice(COLORS))
        y_position = random.randint(-250, 250)
        new_brick.goto(300, y_position)
        self.all_bricks.append(new_brick)

    def move_cars(self):
        for brick in self.all_bricks:
            new_x = brick.xcor() - 5
            brick.goto(new_x, brick.ycor())


