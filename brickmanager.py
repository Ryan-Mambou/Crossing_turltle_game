from turtle import Turtle
import random

COLORS = ["pink", "yellow", "green", "blue", "red", "violet"]
MOVE_INCREMENT = 5


class BrickManager:
    def __init__(self):
        self.all_bricks = []
        self.create_brick()
        self.brick_speed = MOVE_INCREMENT

    def create_brick(self):
        # Create car if random_chance equals 1 to reduce number of cars created to avoid saturation of car
        random_chance = random.randint(1, 6)
        if random_chance == 1:
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
            new_x = brick.xcor() - self.brick_speed
            brick.goto(new_x, brick.ycor())

    def speed_up_bricks(self):
        self.brick_speed += MOVE_INCREMENT
