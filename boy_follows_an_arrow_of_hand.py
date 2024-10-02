from pico2d import *
import random

open_canvas()

def random_locate():
    global x, y

    x, y = random.randint(0, 800), random.randint(0, 600)

character = load_image('run_animation.png')
x, y, frame = 0, 0, 0

while True:
    clear_canvas()
    random_locate()
    character.clip_draw(frame*100, 0, 100, 100, x, y)
    update_canvas()
    frame = (frame + 1) % 8
    delay(0.5)

close_canvas()