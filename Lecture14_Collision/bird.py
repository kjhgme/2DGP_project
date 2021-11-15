import random
from pico2d import *
import game_world
import game_framework

BIRD_PIXEL_PER_METER = (10.0 / 0.3)
BIRD_SPEED_KMPH = 123.0     # 비둘기의 평균속도
BIRD_SPEED_MPM = (BIRD_SPEED_KMPH * 1000.0 / 60.0)
BIRD_SPEED_MPS = (BIRD_SPEED_MPM / 60.0)
BIRD_SPEED_PPS = (BIRD_SPEED_MPS * BIRD_PIXEL_PER_METER)


class Bird:
    def __init__(self):
        self.image = load_image('bird100x100x14.png')
        self.x = random.randint(0, 1600)
        self.y = random.randint(400, 500)
        self.frame = 0
        self.direction = 0

    def update(self):
        if self.direction <= 0:
            self.x += game_framework.frame_time * BIRD_SPEED_PPS
        elif self.direction >= 1:
            self.x -= game_framework.frame_time * BIRD_SPEED_PPS

        self.frame = (self.frame + BIRD_SPEED_PPS * game_framework.frame_time) % 14

        if self.x >= 1600 - 25:
            self.direction += 1
        elif self.x <= 25:
            self.direction -= 1



        pass

    def draw(self):
        self.image.clip_draw(int(self.frame) * 100, 0, 100, 100, self.x, self.y)



        # fill here


    # fill here
    def get_bb(self):
        return 0, 0, 0, 0

    #fill here for def stop


# fill here
# class BigBall