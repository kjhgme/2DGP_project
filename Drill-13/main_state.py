import random
import json
import os

from pico2d import *
import game_framework
import game_world
import server

from boy import Boy
from grass import Grass
from ball import Ball
from brick import Brick

name = "MainState"






def enter():
    server.boy = Boy()
    game_world.add_object(server.boy, 1)

    server.grass = Grass()
    game_world.add_object(server.grass, 0)

    server.balls = [Ball() for i in range(200)]
    game_world.add_objects(server.balls, 1)

    server.brick = Brick()
    game_world.add_object(server.brick, 1)

def exit():
    game_world.clear()

def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()
        else:
            server.boy.handle_event(event)


def update():
    for game_object in game_world.all_objects():
        game_object.update()

    # ball과 grass의 총돌을 체크하고 처리. 이건 어디서 하면 좋을까?
    # 상관은 없지만. 잔디가 충돌을 체크.
    # ball과 brick의 처리.


#    for ball in balls.copy():
#        if collide(ball, grass):
#            ball.stop()
#        if collide(ball, boy):
#            balls.remove(ball)
#            game_world.remove_object(ball)
#        elif collide(ball, brick):
#            brick.attach_ball(ball)
#            balls.remove(ball)  #발판에 포함됐기 때문에 충돌체크X
#        else:   #볼이 발판 안의 공과 총될되는지
#            for brick_ball in brick.child_balls:    #가각의 벽돌안의 공들과
#                if collide(ball, brick_ball):
#                    brick.attach_ball(ball)
#                    balls.remove(ball)
#                    break



def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()






