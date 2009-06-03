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

try:
    import osso
    os.environ["SDL_VIDEO_X11_WMCLASS"]="ltd.py"
    osso_c=osso.Context("org.free.ltd2009","1.1",False)
    maemo=True
except:
    print 'no maemo'
    maemo=False

def imageLoad (name):
      try:
         image = pygame.image.load(name)
      except pygame.error, message:
         print 'Cannot load image:', name
         raise SystemExit, message
      
      image = image.convert()
    
      return image, image.get_rect()

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

class Game:
   def __init__ (self, caption, screenWidth, screenHeight, maxFPS):
		if maemo:
		   self.screen = pygame.display.set_mode((screenWidth, screenHeight), FULLSCREEN)
		else:
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
		self.sounds = {}
		self.order = []
		self.playerOrder = []
		self.MAX_ORDER = 0 
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

   def setMaxOrder (self, max):
      self.MAX_ORDER = max

   def setCaption (self, caption):
      pygame.display.set_caption(caption)

   # miniSprites are used to display the order of what you gotta
   # put shit in at the top of the game
   def addMiniSprite (self, spriteName, sprite):
      self.miniSprites[spriteName] = sprite

   def addSprite (self, spriteName, sprite):
      self.sprites[spriteName] = sprite

   def addGroup (self, groupName):
      newGroup = pygame.sprite.OrderedUpdates()
      self.groups[groupName] = newGroup

   def addMiniSpriteToGroup (self, miniSprite, group):
      self.groups[group].add(self.miniSprites[miniSprite])

   def removeMiniSpriteFromGroup (self, miniSprite, group):
      self.groups[group].remove(self.miniSprites[miniSprite])

   def addSpriteToGroup (self, sprite, group):
      self.groups[group].add(self.sprites[sprite])

   def removeSpriteFromGroup (self, sprite, group):
      self.groups[group].remove(self.sprites[sprite])

   def loadSound (self, filename, name):
      self.sounds[name] = pygame.mixer.Sound(filename)

   def playSound (self, name):
      pygame.mixer.Sound.play(self.sounds[name])

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
            if event.key == K_z or event.key == K_UP:
               if self.groups["sprites"].has(self.sprites["bread"]) and self.MAX_ORDER == 5:
                  self.addSpriteToGroup("bread1", "sprites")
                  self.playerOrder.append("bread1")
               else:
                  self.addSpriteToGroup("bread", "sprites")
                  self.playerOrder.append("bread")
            if event.key == K_x or event.key == K_LEFT:
               self.addSpriteToGroup("lettuce", "sprites")
               self.playerOrder.append("lettuce")
            if event.key == K_c or event.key == K_RIGHT:
               self.addSpriteToGroup("tomato", "sprites")
               self.playerOrder.append("tomato")
            if (event.key == K_v and self.MAX_ORDER > 3) or (event.key == K_DOWN and self.MAX_ORDER > 3):
               self.addSpriteToGroup("butter", "sprites")
               self.playerOrder.append("butter")
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
         self.playSound("yes")
      else:
         self.losses += 1
         self.playSound("no")
   
      self.calcAvgSpeed() 

      for sprite in self.groups["sprites"]:
         self.groups["sprites"].remove(sprite)

      self.chooseOrder()

   def renderFont (self, msg, color):
      return pygame.font.Font.render(self.font, msg, self.FONT_SIZE, color)
  
   def menu (self):
      menuTitle = self.renderFont("Lettuce Trance Dance 2009", (255,255,0))
      a = self.renderFont("Up: Easy", (255,255,255))
      b = self.renderFont("Left: Medium", (0,0,255))
      c = self.renderFont("Right: Hard", (255,0,0))
      r = self.renderFont("Down: Retarded", (0,255,255))
      h = self.renderFont("H: Help!", (255,255,255))

      while 1:
         self.screen.fill((0,0,0))
         self.screen.blit(menuTitle, (100, 25))
         self.screen.blit(a, (100, 100))
         self.screen.blit(b, (100, 160))
         self.screen.blit(c, (100, 220))
         #self.screen.blit(r, (100, 280))
         #self.screen.blit(h, (100, 340))
         pygame.display.flip()

         for event in pygame.event.get():
            if event.type == KEYDOWN:
               if event.type == QUIT:
                  sys.exit()
               if event.type == KEYDOWN:
                  if event.key == K_a or event.key == K_UP:
                     return "easy"
                  elif event.key == K_b or event.key == K_LEFT:
                     return "medium"
                  elif event.key == K_c or event.key == K_RIGHT:
                     return "hard"
                  elif event.key == K_r or event.key == K_DOWN:
                     #return "retarded"
                     pass
                  elif event.key == K_h:
                     pass

   def endGame (self):
      exitMsg = self.renderFont("Game Over. Press Enter to Quit.", (255,255,255))

      while 1:
         self.screen.fill((0,0,0))
         self.displayScore()
         self.screen.blit(exitMsg, (65, 210))
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
            # special bread case
            if (self.playerOrder[i] == "bread" or self.playerOrder[i] == "bread1") and (self.order[i] == "bread" or self.order[i] == "bread1"):
               pass
            elif self.playerOrder[i] == self.order[i]:
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
      score = self.renderFont("Wins: %i   Losses: %i" %(self.wins, self.losses), (255,255,255))
      avgSpeed = pygame.font.Font.render(self.font, "Avg Speed: %i frames per attempt" %(self.avgSpeed), self.FONT_SIZE / 2, (255,255,255))
      self.screen.blit(score, (325, 20))
      self.screen.blit(avgSpeed, (10, 420))

   def mainLoop (self):
      # Initial order
      self.chooseOrder()

      while 1:
         self.bgChange()
         self.screen.fill(self.bgcolor)
         self.handleEvents()
         self.displayScore()
         self.update()

if __name__ == "__main__":
   g = Game("Lettuce Trance Dance 2009", 800, 480, 90)
   difficulty = g.menu()

   # for easy
   g.setMaxOrder(3)

   g.addGroup("sprites")
   g.addGroup("miniSprites")

   l = Entity("lettuce.gif", 450, 300)
   b = Entity("bread.gif", 300, 300) 
   t = Entity("tomato.gif", 550, 300)

   g.addSprite("bread", b)
   g.addSprite("lettuce", l)
   g.addSprite("tomato", t)

   mb = Entity("miniBread.gif", 125, 25)
   ml = Entity("miniLettuce.gif", 75, 25)
   mt = Entity("miniTomato.gif", 25, 25)

   g.addMiniSprite("bread", mb)
   g.addMiniSprite("lettuce", ml)
   g.addMiniSprite("tomato", mt)

   g.addMiniSpriteToGroup("bread", "miniSprites")
   g.addMiniSpriteToGroup("lettuce", "miniSprites")
   g.addMiniSpriteToGroup("tomato", "miniSprites")

   # Will be used if difficult is changed from easy
   bu = Entity("butter.gif", 350, 300)
   mbu = Entity("miniButter.gif", 175, 25)

   if difficulty == "medium":
      g.setMaxOrder(4)
      g.addSprite("butter", bu)
      g.addMiniSprite("butter", mbu)
      g.addMiniSpriteToGroup("butter", "miniSprites")

   elif difficulty == "hard":
      g.setMaxOrder(5)
      g.addSprite("butter", bu)
      g.addMiniSprite("butter", mbu)
      g.addMiniSpriteToGroup("butter", "miniSprites")

      mb1 = Entity("miniBread.gif", 225, 25)
      b1 = Entity("bread.gif", 500, 300)
      g.addMiniSprite("bread1", mb1) 
      g.addSprite("bread1", b1)
      g.addMiniSprite("bread1", mb1) 
      g.addMiniSpriteToGroup("bread1", "miniSprites")

   elif difficulty == "retarded":
      pass

   g.loadSound("yes.wav", "yes")
   g.loadSound("no.wav", "no")
   
   g.newSong("baudOfPassion.mp3")
   g.mainLoop()
