 #This file is part of Lettuce Trance Dance 2009.

    #Lettuce Trance Dance 2009 is free software: you can redistribute it and/or modify
    #it under the terms of the GNU General Public License as published by
    #the Free Software Foundation, either version 3 of the License, or
    #(at your option) any later version.

    #Lettuce Trance Dance 2009 is distributed in the hope that it will be useful,
    #but WITHOUT ANY WARRANTY; without even the implied warranty of
    #MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    #GNU General Public License for more details.

    #You should have received a copy of the GNU General Public License
    #along with Lettuce Trance Dance 2009.  If not, see <http://www.gnu.org/licenses/>.


import pygame
from pygame.locals import *
from Game import imageLoad 

class Entity (pygame.sprite.Sprite):
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

   def changeCoords (self, x, y):
      self.position = (x,y)

   def update (self):
      self.rect.center = self.position
	
