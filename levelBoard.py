from turtle import Turtle


class LevelBoard(Turtle):
    def __int__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.shape("square")
        self.level = 1
        self.update_level()

    def update_level(self):
        self.clear()
        self.goto(-280, 280)
        self.write(f"Level: {self.level}", align="center", font=("Courier", 80, "normal"))

    def level_up(self):
        self.level += 1
        self.update_level()
