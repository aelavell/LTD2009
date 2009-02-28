import pygame
from pygame.locals import *
from Game import *

class Sprite (pygame.sprite.Sprite):
   def __init__ (self, imageFile, x, y):
      pygame.sprite.Sprite.__init__(self)
      self.image, self.rect  = imageLoad(imageFile)
      self.position = (x,y)
		
   def update (self):
      self.rect.center = self.position
	
