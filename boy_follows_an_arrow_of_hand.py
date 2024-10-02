from pico2d import *
import random

open_canvas()
character = load_image('run_animation.png')
point = load_image('hand_arrow.png')
TUK = load_image('TUK_GROUND.png')

def random_locate():
    global base_x, base_y, des_x, des_y
    base_x , base_y = des_x, des_y

    des_x, des_y = random.randint(0,800), random.randint(0, 600)

    pass

def character_move_animation(p1, p2):
    x1, y1 = p1[0], p1[1]
    x2, y2 = p2[0], p2[1]
    frame = 0

    random_locate()

    for i in range(0, 100 + 1, 4):
        clear_canvas()
        TUK.draw(400, 300)
        point.draw(x2, y2)
        t = i / 100
        x = (1 - t) * x1 + t * x2
        y = (1 - t) * y1 + t * y2
        if x2 > x1 :
            character.clip_draw(frame * 100, 0, 100, 100, x, y)
        else:
            character.clip_composite_draw(frame*100, 0, 100, 100, 0, 'h', x, y, 100, 100)
        update_canvas()
        frame = (frame + 1) % 8
        delay(0.05)

    pass

base_x, base_y, des_x, des_y = 0, 0, 0, 0

while True:

    character_move_animation((base_x, base_y), (des_x, des_y))

close_canvas()