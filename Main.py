import pygame
from Lettuce import *
from Game import *

if __name__ == "__main__":
   lGroup = pygame.sprite.Group
   g = Game(800, 600)
   l = Lettuce(0, 0)
   g.addGroup("lettuce")
   g.addSpriteToGroup(l, "lettuce")
   g.mainLoop()
