import pygame
from Sprite import *
from Game import *

if __name__ == "__main__":
   g = Game("Lettuce Techno Tarry", 800, 600, 60)
   l = Sprite("lettuce.gif", 400, 400)
   b = Sprite("bread.gif", 400, 400) 
   g.addGroup("sprites")
   g.addSpriteToGroup(b, "sprites")
   g.addSpriteToGroup(l, "sprites")
   g.newSong("baudOfPassion.ogg")
   g.mainLoop()
