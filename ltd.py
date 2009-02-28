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
   g = Game("Lettuce Trance Dance 2009", 800, 600, 90)
   l = Entity("lettuce.gif", 400, 400)
   b = Entity("bread.gif", 400, 300) 
   t = Entity("tomato.gif", 400, 400)

   #l.toggleVisible()
   #t.toggleVisible()
   #b.toggleVisible()

   g.addSprite("bread", b)
   g.addSprite("lettuce", l)
   g.addSprite("tomato", t)

   mb = Entity("miniBread.gif", 125, 25)
   ml = Entity("miniLettuce.gif", 75, 25)
   mt = Entity("miniTomato.gif", 25, 25)

   g.addMiniSprite("bread", mb)
   g.addMiniSprite("lettuce", ml)
   g.addMiniSprite("tomato", mt)

   g.addGroup("sprites")
   g.addGroup("miniSprites")

   #g.addSpriteToGroup("bread", "sprites")
   #g.addSpriteToGroup("lettuce", "sprites")
   #g.addSpriteToGroup("tomato", "sprites")

   g.addMiniSpriteToGroup("bread", "miniSprites")
   g.addMiniSpriteToGroup("lettuce", "miniSprites")
   g.addMiniSpriteToGroup("tomato", "miniSprites")
   
   g.newSong("baudOfPassion.ogg")
   g.mainLoop()
