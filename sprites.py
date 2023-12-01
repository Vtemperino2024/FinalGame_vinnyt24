import pygame as pg
from pygame.sprite import Sprite
pg.init()

from pygame.math import Vector2 as vec
import os
from settings import *

class Solids:
    def __init__(self, x, y, w, h, type,text,size,color):
        Sprite.__init__(self)
        if type == "text":

            self.draw_text(str(text),size,color,w,h)
            #
            pg.display.flip()
        elif type =="solid":
            self.image = pg.Surface((w,h))
            self.image.fill(PURPLE)
            self.rect = self.image.get_rect()
            self.rect.topleft = vec(x,y)
    

    def draw_text(self,text,size,color,x,y):
        font_name = pg.font.match_font('arial')
        font = pg.font.Font(font_name,size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x,y)
        SCREEN.blit(text_surface,text_rect)
    








