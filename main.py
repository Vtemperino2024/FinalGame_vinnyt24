# This file was created by: Vinny Temperino

# IMPORTS
import pygame as pg
from pygame.sprite import Sprite
import random
from random import randint
import os
from settings import *
import time
from sprites import *
from time import *

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img_folder")
img_folder = os.path.join(game_folder, "sound_folder")

class Run:
    def __init__(self):
        pg.init()
        pg.mixer.init()
        pg.display.update()
        pg.display.set_caption("Decision Analysis App")
        self.clock = pg.time.Clock()
        self.running = True
    def new(self):
        self.analyzed = False
        self.all_sprites = pg.sprite.Group()
        toplayer = Solids(0,0,800,200,"solid",0,0,PURPLE)
        toplayertext = Solids(0,0,800,200,"text","Decision Analysis App",25,TEXTC)

r = Run()
while r.running:
    r.new()


pg.quit()



