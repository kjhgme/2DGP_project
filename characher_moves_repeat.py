from pico2d import *
import math
os.chdir('d:/2DGP/2DGP_project/Lecture04_2D_Rendering')
open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def move_square():
    x = 400
    y = 90
    while x < 770:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x += 2
        delay(0.01)      
    while y < 550:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        y += 2
        delay(0.01)
    while x > 30:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x -= 2
        delay(0.01)
    while y > 90:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        y -= 2
        delay(0.01)
    while x < 400:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x += 2
        delay(0.01)

def move_circle():
    angle = 0
    while angle < 360:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(400 + 250 * math.sin((angle * math.pi) / 180), 335 + 250 * math.cos(((180+angle)*math.pi) / 180))
        angle += 2
        print(angle)
        delay(0.01)

while True:
    move_square()
    move_circle()

