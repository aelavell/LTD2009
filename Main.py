import pygame
from Entity import *
from Game import *

if __name__ == "__main__":
   g = Game("Lettuce Trance Dance 2009", 800, 600, 90)
   l = Entity("lettuce.gif", 400, 400)
   b = Entity("bread.gif", 400, 400) 
   t = Entity("tomato.gif", 400, 400)

   l.toggleVisible()
   t.toggleVisible()
   #b.toggleVisible()

   g.addSprite("bread", b)
   g.addSprite("lettuce", l)
   g.addSprite("tomato", t)

   mb = Entity("miniBread.gif", 125, 25)
   ml = Entity("miniLettuce.gif", 75, 25)
   mt = Entity("miniTomato.gif", 25, 25)

   g.addMiniSprite("miniBread", mb)
   g.addMiniSprite("miniLettuce", ml)
   g.addMiniSprite("miniTomato", mt)

   g.addGroup("sprites")
   g.addGroup("miniSprites")

   g.addSpriteToGroup("bread", "sprites")
   g.addSpriteToGroup("lettuce", "sprites")
   g.addSpriteToGroup("tomato", "sprites")

   g.addMiniSpriteToGroup("miniBread", "miniSprites")
   g.addMiniSpriteToGroup("miniLettuce", "miniSprites")
   g.addMiniSpriteToGroup("miniTomato", "miniSprites")
   
   g.newSong("baudOfPassion.ogg")
   g.mainLoop()
