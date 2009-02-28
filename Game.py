import pygame 
from pygame.locals import *
import sys, os
import random 
from Entity import *

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
      self.maxFPS = maxFPS
      self.groups = {}
      self.sprites = {}
      self.miniSprites = {}
      self.order = []
      self.playerOrder = []
      self.MAX_ORDER = 3
      self.bgCount = 0
      self.bgIndex = 0
      self.bgColors =  [(255,0,0), (0,255,0), (0,0,255)]
      self.captions = ["red!", "green!", "blue!"]
      self.bgcolor = self.bgColors[0]
      self.wins = 0
      self.losses = 0
      pygame.font.init()
      self.FONT_SIZE = 60
      self.font = pygame.font.Font(None, self.FONT_SIZE)
      pygame.mixer.init()
      pygame.init()

   def setCaption (self, caption):
      pygame.display.set_caption(caption)

   # miniSprites are used to display the order of what you gotta
   # put shit in at the top of the game
   def addMiniSprite (self, spriteName, sprite):
      self.miniSprites[spriteName] = sprite

   def addSprite (self, spriteName, sprite):
      self.sprites[spriteName] = sprite

   def addGroup (self, groupName):
      newGroup = pygame.sprite.Group()
      self.groups[groupName] = newGroup

   def addMiniSpriteToGroup (self, miniSprite, group):
      self.groups[group].add(self.miniSprites[miniSprite])

   def removeMiniSpriteFromGroup (self, miniSprite, group):
      self.groups[group].remove(self.miniSprites[miniSprite])

   def addSpriteToGroup (self, sprite, group):
      self.groups[group].add(self.sprites[sprite])

   def removeSpriteFromGroup (self, sprite, group):
      self.groups[group].remove(self.sprites[sprite])

   def newSong (self, filename):
      pygame.mixer.music.load(filename)
      self.playSong() 

   def playSong (self):
      pygame.mixer.music.play(-1)

   def pauseSong (self):
      pygame.mixer.music.pause()

   def unpauseSong (self):
      pygame.mixer.music.unpause()

   def bgChange (self):
      self.bgCount += 1

      if self.bgCount == 60:    
         # bgIndex sets the caption (to red!, blue! or green!)
         self.bgIndex += 1

         if self.bgIndex > 2:
            self.bgIndex = 0
            
         self.setCaption(self.captions[self.bgIndex])
         self.bgcolor = self.bgColors[self.bgIndex] 
         self.bgCount = 0

   def chooseOrder (self):
      # The order of the 3 elements is chosen randomly
      # Player must put them together in the same way

      # This will be random each time
      keyList = self.miniSprites.keys()
      random.shuffle(keyList)
      xi = 25
      y = 25
      self.order = []
      self.playerOrder = []

      for sprite in keyList:
         self.miniSprites[sprite].changeCoords(xi, y)
         self.order.append(sprite)
         xi += 50

   def handleEvents (self):
      for event in pygame.event.get():
         if event.type == QUIT:
            sys.exit()
         elif event.type == KEYDOWN:
            if event.key == K_x:
               self.addSpriteToGroup("lettuce", "sprites")
               self.playerOrder.append("lettuce")
            if event.key == K_z:
               self.addSpriteToGroup("bread", "sprites")
               self.playerOrder.append("bread")
            if event.key == K_c:
               self.addSpriteToGroup("tomato", "sprites")
               self.playerOrder.append("tomato")

   def endRound (self, victory):
      if victory == True:
         self.wins += 1
      else:
         self.losses += 1

      for sprite in self.groups["sprites"]:
         self.groups["sprites"].remove(sprite)

      self.chooseOrder()

   def update (self):
      for group in self.groups.iteritems():
         group[1].update()
         group[1].draw(self.screen)

      if len(self.playerOrder) == self.MAX_ORDER:
         i = 0 
         victory = True

         while i < self.MAX_ORDER:
            if self.playerOrder[i] == self.order[i]:
               pass
            else:
               victory = False
               break
            i += 1

         self.endRound(victory)

      pygame.display.flip()
      self.clock.tick(self.maxFPS)

   def displayScore (self):
      score = pygame.font.Font.render(self.font, "Wins: %i Losses: %i" %(self.wins, self.losses), self.FONT_SIZE, (0,0,0))
      self.screen.blit(score, (425, 20))

   def mainLoop (self):
      self.chooseOrder()

      while 1:
         self.bgChange()
         self.screen.fill(self.bgcolor)
         self.handleEvents()
         self.displayScore()
         self.update()
