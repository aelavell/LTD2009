import pygame 
from pygame.locals import *
import sys, os
import random

def imageLoad (name):
      try:
         image = pygame.image.load(name)
      except pygame.error, message:
         print 'Cannot load image:', name
         raise SystemExit, message
      
      image = image.convert()
    
      return image, image.get_rect()

class Game:
   def __init__ (self, caption, screenWidth, screenHeight, maxFPS):
      self.screen = pygame.display.set_mode((screenWidth, screenHeight))
      self.setCaption(caption)
      self.clock = pygame.time.Clock()
      self.clock.tick(maxFPS)
      self.groups = {}
      self.sprites = {}
      self.bgCount = 0
      self.bgIndex = 0
      self.bgColors =  [(255,0,0), (0,255,0), (0,0,255)]
      self.captions = ["red!", "green!", "blue!"]
      self.bgcolor = self.bgColors[0]
      pygame.font.init()
      pygame.mixer.init()
      pygame.init()

   def setCaption (self, caption):
      pygame.display.set_caption(caption)

   def addSprite (self, spriteName, sprite):
      self.sprites[spriteName] = sprite

   def addGroup (self, groupName):
      newGroup = pygame.sprite.Group()
      self.groups[groupName] = newGroup

   def addSpriteToGroup (self, sprite, group):
      self.groups[group].add(sprite)

   def newSong (self, filename):
      pygame.mixer.music.load(filename)
      self.playSong() 

   def playSong (self):
      pygame.mixer.music.play()

   def pauseSong (self):
      pygame.mixer.music.pause()

   def unpauseSong (self):
      pygame.mixer.music.unpause()

   def bgChange (self):
      self.bgCount += 1

      if self.bgCount == 60:    
         self.bgIndex += 1

         if self.bgIndex > 2:
            self.bgIndex = 0
            
         self.setCaption(self.captions[self.bgIndex])
         self.bgcolor = self.bgColors[self.bgIndex] 
         self.bgCount = 0

   def handleEvents (self):
      for event in pygame.event.get():
         if event.type == QUIT:
            sys.exit()
         elif event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
               self.sprites["lettuce"].toggleVisible()

   def update (self):
      for group in self.groups.iteritems():
         group[1].update()
         group[1].draw(self.screen)

      pygame.display.flip()

   def mainLoop (self):
      while 1:
         self.bgChange()
         self.screen.fill(self.bgcolor)
         self.handleEvents()
         self.update()
