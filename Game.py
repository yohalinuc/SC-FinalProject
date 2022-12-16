## May need to install pygame using pip install pygame

import pygame as pg

pg.init()

width = 800
height = 800

screen = pg.display.set_mode((width, height))
end = False

while not end:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            end = True
    pg.display.flip()

