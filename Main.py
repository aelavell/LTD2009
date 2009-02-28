import pygame
from Lettuce import *
from Game import *

if __name__ == "__main__":
   lGroup = pygame.sprite.Group
   g = Game("Lettuce Techno Tarry", 800, 600, 60)
   l = Lettuce(400, 400)
   g.addGroup("lettuce")
   g.addSpriteToGroup(l, "lettuce")
   g.newSong("baudOfPassion")
   g.mainLoop()
