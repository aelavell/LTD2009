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
from Entity import *
from Game import *

if __name__ == "__main__":
   g = Game("Lettuce Trance Dance 2009", 800, 500, 90)
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

   
   g.newSong("baudOfPassion.ogg")
   g.mainLoop()
