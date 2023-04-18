# -----------------------------------------------------------------------------
# 
# File Name: Monster.py
#
# Author: Donald Summers
#
# Description:  Part of the Ultima game that sets up the monsters based on code
#               values parsed in, similar to the Tile program. Each monster also
#               has HP, how much damage they deal, current coordinate position, and
#               a timer for how long it takes before they move
#
# How to use:   Import into another file to run it as a part of Ultima
#
# Example use:  python Ultima.py 30x20.txt
#
# -----------------------------------------------------------------------------

from enum import Enum, auto
import time
import StdDraw
import picture
import random
from Tile import Tile
from color import RED

class MonsterType(Enum):
    INVALID = auto()
    SKELETON = auto()
    ORC = auto()
    BAT = auto()
    SLIME = auto()

# ----------------------------------------------------------------------------
#
# Monster class - impliments functionality Ultima game with all monsters, 
#                 including position, damage taken/given, and a worker method
#                 for threading
#
# ----------------------------------------------------------------------------
class Monster:

    # -----------------------------------------------------------------------------
    # Method: __init__
    #
    # Inputs:
    #   self : reference to the object
    #   world : World object, keeps in reference for use in threading
    #   x, y : int, coordinates for monster placement
    #   HP, damage : int, HP total and damage the monster deals
    #   sleepMs : int, how long it takes for the monster to move again
    #
    # Return Value:
    #   __init__ does not return a value.
    #
    # Example Use:
    #   a = World("30x20.txt")
    #   b = Monster(a,1,1,1,1,1000)
    #
    # Description:
    #   Initializes the class for use in Ultima game, sets monsters's start position,
    #   HP, damage, and turn delay
    # -----------------------------------------------------------------------------
    def __init__(self, world, code, x, y, hp, damage, sleepMs):
        self.world = world
        self.code = code
        self.x = x
        self.y = y
        self.hp = hp
        self.damage = damage
        self.sleepMs = sleepMs
        self.timer = 9
        StdDraw._penColor = RED

    # -----------------------------------------------------------------------------
    # Method: incurDamage
    #
    # Inputs:
    #   self : reference to the object
    #   points : int, how much damage taken
    #
    # Return Value:
    #   incurDamage does not return a value.
    #
    # Example Use:
    #   a = World("30x20.txt")
    #   b = Monster(a,1,1,1,1,1000)
    #   b.incurDamage(1)
    #   would set monster HP to 0
    #
    # Description:
    #   Decreses HP by parsed in damage total
    # -----------------------------------------------------------------------------
    def incurDamage(self, points):
        self.hp = self.hp - points
        self.timer = 0

    # -----------------------------------------------------------------------------
    # Method: draw
    #
    # Inputs:
    #   self : reference to the object
    #
    # Return Value:
    #   draw does not return a value.
    #
    # Example Use:
    #   a = World("30x20.txt")
    #   b = Monster(a,1,1,1,1,1000)
    #   b.draw()
    #   draws a monster at (1,1)
    #
    # Description:
    #   Draws a monster based on it's current position, if the enemy has been damaged
    #   recently, displays current HP
    # -----------------------------------------------------------------------------
    def draw(self):
        if self.code == "SK":
            currentTile = picture.Picture("skeleton.gif")
        elif self.code == "OR":
            currentTile = picture.Picture("orc.gif")
        elif self.code == "SL":
            currentTile = picture.Picture("slime.gif")
        elif self.code == "BA":
            currentTile = picture.Picture("bat.gif")
        StdDraw.picture(currentTile,self.x*16+8,self.y*16+8)
        if self.timer < 9:
            StdDraw.text(self.x*16+8,self.y*16+8, str(self.hp))
            self.timer += 1

    # -----------------------------------------------------------------------------
    # Method: getHitPoints
    #
    # Inputs:
    #   self : reference to the object
    #
    # Return Value:
    #   self.hp : current HP of the monster
    #
    # Example Use:
    #   a = World("30x20.txt")
    #   b = Monster(a,1,1,1,1,1000)
    #   print(b.getHitPoints())
    #   would print "1"
    #
    # Description:
    #   Returns the monster's current HP
    # -----------------------------------------------------------------------------
    def getHitPoints(self):
        return self.hp

    # -----------------------------------------------------------------------------
    # Method: getDamage
    #
    # Inputs:
    #   self : reference to the object
    #
    # Return Value:
    #   self.damage : how much damage the monster deals
    #
    # Example Use:
    #   a = World("30x20.txt")
    #   b = Monster(a,1,1,1,1,1000)
    #   print(b.getDamage())
    #   would print "1"
    #
    # Description:
    #   Returns the how much damage the monster deals
    # -----------------------------------------------------------------------------
    def getDamage(self):
        return self.damage

    # -----------------------------------------------------------------------------
    # Method: getX
    #
    # Inputs:
    #   self : reference to the object
    #
    # Return Value:
    #   self.x : current X position of the monster
    #
    # Example Use:
    #   a = World("30x20.txt")
    #   b = Monster(a,1,1,1,1,1000)
    #   print(b.getX())
    #   would print "1"
    #
    # Description:
    #   Returns the monster's current X position
    # -----------------------------------------------------------------------------
    def getX(self):
        return self.x

    # -----------------------------------------------------------------------------
    # Method: getY
    #
    # Inputs:
    #   self : reference to the object
    #
    # Return Value:
    #   self.y : current y position of the monster
    #
    # Example Use:
    #   a = World("30x20.txt")
    #   b = Monster(a,1,1,1,1,1000)
    #   print(b.getY())
    #   would print "1"
    #
    # Description:
    #   Returns the monster's current y position
    # -----------------------------------------------------------------------------
    def getY(self):
        return self.y

    # -----------------------------------------------------------------------------
    # Method: setLocation
    #
    # Inputs:
    #   self : reference to the object
    #   x, y : int, new location of the monster
    #
    # Return Value:
    #   setLocation does not return a value
    #
    # Example Use:
    #   a = World("30x20.txt")
    #   b = Monster(a,1,1,1,1,1000)
    #   b.setLocation(2,2)
    #   monster is now at (2,2)
    #
    # Description:
    #   Changes the monster's coordinates based on parsed values
    # -----------------------------------------------------------------------------
    def setLocation(self, x, y):
        self.x = x
        self.y = y

    # -----------------------------------------------------------------------------
    # Method: run
    #
    # Inputs:
    #   self : reference to the object
    #
    # Return Value:
    #   run does not return a value
    #
    # Example Use:
    #   a = World("30x20.txt")
    #   b = Monster(a,1,1,1,1,1000)
    #   for x in range(len(self.monsterList)):
    #        self.threadList[x] = threading.Thread(target=b.run)
    #        self.threadList[x].start()
    #   starts threads for each monster in the list
    #
    # Description:
    #   Controlls what direction the monster moves in, acts as worker for threading
    # -----------------------------------------------------------------------------
    def run(self):
        while self.hp > 0:
            direction = random.randrange(1,5)
            if direction == 1:
                self.world.monsterMove(self.x,self.y+1, self)
            elif direction == 2:
                self.world.monsterMove(self.x,self.y-1, self)
            elif direction == 3:
                self.world.monsterMove(self.x+1,self.y, self)
            elif direction == 4:
                self.world.monsterMove(self.x-1,self.y, self)
            time.sleep(self.sleepMs/1000)
