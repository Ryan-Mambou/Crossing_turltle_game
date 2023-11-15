from turtle import Screen
from brickmanager import BrickManager
from levelBoard import LevelBoard
from player import Player
import time

screen = Screen()
player = Player()
brick_manager = BrickManager()
level_board = LevelBoard()
screen.setup(600, 600)
screen.title("Car Collide Game")
screen.tracer(0)
screen.listen()
screen.onkey(player.move_up, "Up")

game_is_on = True
while game_is_on:
    brick_manager.create_brick()
    brick_manager.move_cars()
    time.sleep(0.1)
    screen.update()

    # If a brick hits a player
    for brick in brick_manager.all_bricks:
        if player.distance(brick) < 20:
            game_is_on = False
            level_board.game_over()

    # If player reaches other end
    if player.ycor() > 290:
        player.reset_position()
        brick_manager.speed_up_bricks()
        level_board.level_up()


screen.exitonclick()
