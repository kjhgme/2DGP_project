from pico2d import *
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


move_square()
delay(1)
close_canvas()
