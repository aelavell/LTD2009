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
      self.framesElapsed = 0
      self.speedList = []
      self.avgSpeed = 0
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
            if event.key == K_RETURN:
               self.endGame()

   def calcAvgSpeed (self):
      self.speedList.append(self.framesElapsed)
      totalSpeed = 0
      for speed in self.speedList:
         totalSpeed += speed

      self.avgSpeed = totalSpeed / len(self.speedList)
      self.framesElapsed = 0

   def endRound (self, victory):
      if victory == True:
         self.wins += 1
      else:
         self.losses += 1
   
      self.calcAvgSpeed() 

      for sprite in self.groups["sprites"]:
         self.groups["sprites"].remove(sprite)
      
      self.chooseOrder()

   def endGame (self):
      while 1:
         self.screen.fill((0,0,0))
         self.displayScore()
         exitMsg = pygame.font.Font.render(self.font, "Game Over. Press Enter to Quit.", self.FONT_SIZE, (255,255,255))
         self.screen.blit(exitMsg, (65, 275))
         pygame.display.flip()
         for event in pygame.event.get():
            if event.type == KEYDOWN:
               if event.key == K_RETURN:
                  sys.exit()
            if event.type == QUIT:
               sys.exit()

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

      self.framesElapsed += 1
      pygame.display.flip()
      self.clock.tick(self.maxFPS)

   def displayScore (self):
      score = pygame.font.Font.render(self.font, "Wins: %i Losses: %i" %(self.wins, self.losses), self.FONT_SIZE, (255,255,255))
      avgSpeed = pygame.font.Font.render(self.font, "Avg Speed: %i frames per attempt" %(self.avgSpeed), self.FONT_SIZE / 2, (255,255,255))
      self.screen.blit(score, (425, 20))
      self.screen.blit(avgSpeed, (10, 555))

   def mainLoop (self):
      self.chooseOrder()

      while 1:
         self.bgChange()
         self.screen.fill(self.bgcolor)
         self.handleEvents()
         self.displayScore()
         self.update()
         
