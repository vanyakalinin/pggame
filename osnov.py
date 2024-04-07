from pygame import *
from random import *

okno = display.set_mode((1200,600))
 
fps = time.Clock() #контроль fps
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
