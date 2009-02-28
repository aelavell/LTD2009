import pygame 
from pygame.locals import *
import sys, os

def imageLoad (name):
      try:
         image = pygame.image.load(name)
      except pygame.error, message:
         print 'Cannot load image:', name
         raise SystemExit, message
      
      image = image.convert()
    
      return image, image.get_rect()

class Game:
   def __init__ (self, screenWidth, screenHeight):
      try:
         self.screen = pygame.display.set_mode((screenWidth, screenHeight))
         self.clock = pygame.time.Clock()
         self.groups = {}
         pygame.font.init()
         pygame.mixer.init()
      except:
         print "Could not initialize"
         sys.exit(0)

   def addGroup (self, groupName):
      newGroup = pygame.sprite.Group()
      self.groups[groupName] = newGroup

   def addSpriteToGroup (self, sprite, group):
      self.groups[group].add(sprite)

   def update (self):
      for group in self.groups.iteritems():
         group[1].update(0, 0)
         group[1].draw(self.screen)

      pygame.display.flip()

   def mainLoop (self):
      while 1:
         self.update()
