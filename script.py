import pygame
import os
from random import *

from pygame import Rect
from pygame.math import Vector2
score = 0

class GameState():
    def __init__(self):
        self.x = 120
        self.y = 120

    def update(self,spritePos, moveCommand):
        self.spritePos += moveCommand
class Circle(pygame.sprite.Sprite):
    def __init__(self,color,spot,size):
        pygame.sprite.Sprite.__init__(self)
        self.color = (200,0,200)
        self.spot = (randint(30,600),randint(30,400))
        self.size = randint(10,50)


class Interface():
    def __init__(self):
        pygame.init()

        self.gameState = GameState()
        self.unitsTexture = pygame.image.load("sprite.jpg")

        self.window = pygame.display.set_mode((640,480))
        pygame.display.set_caption("Circles")
        self.clock = pygame.time.Clock()
        self.disp_color = (50,50,50)
        self.circle_color = (230,0,230)
        self.running = True

        pygame.display.update()
    def processInput(self, score=None):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                    break
                elif event.key == pygame.K_1:
                    self.disp_color = (0, 255, 0)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.display.set_gamma == self.circle_color:
                    score+=1

    def update(self):
        pass

    def render(self):
        self.window.fill(self.disp_color)
        shape = pygame.draw.circle(self.window, (230, 0, 230), (randint(30, 600), randint(30, 400)), randint(10, 50))
        print(score)
        pygame.display.update()
    def run(self):
        while self.running:
            self.processInput()
            self.update()
            self.render()
            self.clock.tick(5)
circles = []
game = Interface()
game.run()
pygame.quit()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
