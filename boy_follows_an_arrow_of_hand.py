from pico2d import *
import random

open_canvas()

def random_locate():
    global x, y

    x, y = random.randint(0, 800), random.randint(0, 600)

x, y = 0, 0
random_locate()
print(x, y)

close_canvas()