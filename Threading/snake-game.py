import pygame as pg

class Game:
    def __init__(self):               
        self.width = 800
        self.height = 600       
        self.gameDisplay = pg.display.set_mode((self.width, self.height))