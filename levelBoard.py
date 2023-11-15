from turtle import Turtle


class LevelBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.shape("square")
        self.level = 1
        self.update_level()

    def update_level(self):
        self.clear()
        self.goto(-210, 260)
        self.write(f"Level: {self.level}", align="center", font=("Courier", 25, "normal"))

    def level_up(self):
        self.level += 1
        self.update_level()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over!", align="center", font=("Courier", 25, "normal"))
