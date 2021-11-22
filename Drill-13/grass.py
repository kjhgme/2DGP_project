from pico2d import *
import server
import collision

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def update(self):
        for ball in server.balls:
            if collision.collide(self, ball):
                ball.stop()

        pass

    def draw(self):
        self.image.draw(400, 30)
        self.image.draw(1200, 30)
        # fill here
        draw_rectangle(*self.get_bb())


    # fill here
    def get_bb(self):
        return 0, 0, 1600-1, 50
