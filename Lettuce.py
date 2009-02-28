import pygame
from pygame.locals import *
from Game import *

class Lettuce (pygame.sprite.Sprite):
   def __init__ (self, x, y):
      pygame.sprite.Sprite.__init__(self)
      self.image, self.rect  = imageLoad("bread.gif")
      self.position = (x,y)
		
   def update (self, x, y):
      self.position = (x,y)
      self.rect.center = self.position
	
