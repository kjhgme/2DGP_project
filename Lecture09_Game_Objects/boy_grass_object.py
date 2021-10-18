from pico2d import *
import random

# Game object class here
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 400), 90
        self.image = load_image('run_animation.png')
        self.frame = 0

    def update(self):
        self.x += 5
        self.frame = (self.frame+1) % 8

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)

class Ball41:
    def __init__(self):
        self.x, self.y = random.randint(0, 800), 599
        self.image = load_image('ball41x41.png')
        self.frame = 0

    def update(self):
        self.y -= 5
        self.frame = 0

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)

class Ball21:
    def __init__(self):
        self.x, self.y = random.randint(0, 800), 599
        self.image = load_image('ball21x21.png')
        self.frame = 0

    def update(self):
        self.y -= 5
        self.frame = 0

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

class Ball:
    def __init__(self):
        self.x, self.y = random.randint(0, 800), 599
        if(self.x % 2 == 1 ):
            self.image = load_image('ball21x21.png')
        else:
            self.image = load_image('ball41x41.png')
        self.frame = 0
        self.falling_speed = random.randint(1, 10)

    def update(self):
        if(self.y <= 100):
            pass
        else:
            self.y -= self.falling_speed
        self.frame = 0

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

# initialization code
open_canvas()

grass = Grass()
boy = Boy()
#ball41 = Ball41()
#ball21 = Ball21()
Balls = [Ball() for i in range(1, 20+1)]


running = True

# game main loop code
while running:
    handle_events()

    #game logic
    boy.update()
    #ball41.update()
    #ball21.update()
    for Ball in Balls:
        Ball.update()


    #game drawing
    clear_canvas()
    grass.draw()
    #ball41.draw()
    #ball21.draw()
    for Ball in Balls:
        Ball.draw()
    boy.draw()
    update_canvas()

    delay(0.01)
# finalization code
close_canvas()