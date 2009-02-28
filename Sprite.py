import pygame
from pygame.locals import *
from Game import *

class Sprite (pygame.sprite.Sprite):
   def __init__ (self, imageFile, x, y):
      pygame.sprite.Sprite.__init__(self)
      self.imageFile = imageFile
      self.image, self.rect  = imageLoad(imageFile)
      self.position = (x,y)
      self.visible = True 
		
   def toggleVisible (self):
      if self.visible == True: 
         self.image, self.rect = imageLoad("blank.gif")
         self.visible = False
      else: 
         self.image, self.rect = imageLoad(self.imageFile)
         self.visible = True

   def update (self):
      self.rect.center = self.position
	
