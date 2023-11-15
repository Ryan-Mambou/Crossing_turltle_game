from turtle import Screen
from brick import BrickManager
from levelBoard import LevelBoard
from player import Player
import time

screen = Screen()
player = Player()
brick = BrickManager()
level_board = LevelBoard()
screen.setup(600, 600)
screen.title("Car Collide Game")
screen.tracer(0)
screen.listen()
screen.onkey(player.move_up, "Up")

game_is_on = True
while game_is_on:
    brick.create_brick()
    brick.move_cars()
    time.sleep(0.1)
    screen.update()

    # If a brick hits a player
    # if player.distance(brick) < 20:
    #     game_is_on = False

    # If player reaches other end
    if player.ycor() == 290:
        player.reset_position()
        level_board.level_up()




screen.exitonclick()
