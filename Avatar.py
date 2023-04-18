# -----------------------------------------------------------------------------
# 
# File Name: Avatar.py
#
# Author: Donald Summers
#
# Description:  Part of the Ultima game that sets up the avatar/player
#               with a coordinate system and a torch radisu that determines
#               what palyers can see
#
#               Update 0.1: Added functionality in new methods for damage 
#               that the avatar can deal to enemies and taken damage from enemies 
#               as well
#
# How to use:   Import into another file to run it as a part of Ultima, can
#               also be ran with normally in the terminal and will output specific
#               avatar palcements and torch radius values
#
# Example use:  python Avatar.py
#
# -----------------------------------------------------------------------------
import StdDraw
from Tile import Tile
import picture

# ----------------------------------------------------------------------------
#
# Avatar class - impliments functionality Ultima game with avatar, including
#                position, damage taken/given, and torch radius/visability
#
# ----------------------------------------------------------------------------
class Avatar :

    # -----------------------------------------------------------------------------
    # Method: __init__
    #
    # Inputs:
    #   self : reference to the object
    #   x, y : int, coordinates for avatar placement
    #   HP, damage : int, HP total and damage the avatar deals
    #   torchRadius : float, how much the avatar can see at the start
    #
    # Return Value:
    #   __init__ does not return a value.
    #
    # Example Use:
    #   a = Avatar(1,1,1,1,1.0)
    #
    # Description:
    #   Initializes the class for use in Ultima game, sets Avatar's start position,
    #   HP, damage, and torch radius
    # -----------------------------------------------------------------------------
    def __init__(self, x, y, hp, damage, torchRadius):
        self.x = x
        self.y = y
        self.hp = hp
        self.damage = damage
        self.torchRadius = torchRadius

    # -----------------------------------------------------------------------------
    # Method: setLocation
    #
    # Inputs:
    #   self : reference to the object
    #   x, y : int, coordinates for avatar placement
    #
    # Return Value:
    #   setLocation does not return a value
    #
    # Example Use:
    #   a = Avatar(1,1)
    #   a.setLocation(0,0)
    #   avatar is now set at (0,0)
    #
    # Description:
    #   Changes the location of the avatar based on the inputed coordinates
    # -----------------------------------------------------------------------------
    def setLocation(self, x, y):
        self.x = x
        self.y = y

    # -----------------------------------------------------------------------------
    # Method: getX
    #
    # Inputs:
    #   self : reference to the object
    #
    # Return Value:
    #   self.x : x coordinate of the avatar
    #
    # Example Use:
    #   a = Avatar(1,1)
    #   print(a.getX())
    #   would print "1"
    #
    # Description:
    #   Returns the x coordinate of the avatar
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
    #   self.y : y coordinate of the avatar
    #
    # Example Use:
    #   a = Avatar(1,1)
    #   print(a.gety())
    #   would print "1"
    #
    # Description:
    #   Returns the y coordinate of the avatar
    # -----------------------------------------------------------------------------
    def getY(self):
        return self.y
    
    # -----------------------------------------------------------------------------
    # Method: getHitPoints
    #
    # Inputs:
    #   self : reference to the object
    #
    # Return Value:
    #   self.hp : current HP of the player
    #
    # Example Use:
    #   a = Avatar(1,1,1,1,4.0)
    #   print(a.getHitPoints())
    #   would print "1"
    #
    # Description:
    #   Returns the current HP of the player
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
    #   self.damage : y coordinate of the avatar
    #
    # Example Use:
    #   a = Avatar(1,1,1,1,4.0)
    #   print(a.getDamage())
    #   would print "1"
    #
    # Description:
    #   Returns the damage the player does to enemies
    # -----------------------------------------------------------------------------
    def getDamage(self):
        return self.damage
    
    # -----------------------------------------------------------------------------
    # Method: getTorchRadius
    #
    # Inputs:
    #   self : reference to the object
    #
    # Return Value:
    #   self.torchRadius : torch radius of the avatar
    #
    # Example Use:
    #   a = Avatar(1,1)
    #   print(a.getTorchRadius())
    #   would print "4.0"
    #
    # Description:
    #   Returns the torch radius of the avatar
    # -----------------------------------------------------------------------------
    def getTorchRadius(self):
        return self.torchRadius

    # -----------------------------------------------------------------------------
    # Method: incurDamage
    #
    # Inputs:
    #   self : reference to the object
    #   damage : damage an enemy does
    #
    # Return Value:
    #   incurDamage does not return a value
    #
    # Example Use:
    #   a = Avatar(1,1,2,1,4.0)
    #   a.incurDamage(1)
    #   HP is now set at 1
    #
    # Description:
    #   Decreases current HP by passed in damage total
    # -----------------------------------------------------------------------------
    def incurDamage(self, damage):
        self.hp = self.hp - damage

    # -----------------------------------------------------------------------------
    # Method: increaseTorch
    #
    # Inputs:
    #   self : reference to the object
    #
    # Return Value:
    #   increaseTorch does not return a value
    #
    # Example Use:
    #   a = Avatar(1,1)
    #   a.increaseTorch()
    #   increase self.torchRadius to 4.5
    #
    # Description:
    #   Increases the torch radius by .5 for every call
    # -----------------------------------------------------------------------------
    def increaseTorch(self):
        self.torchRadius += .5
    
    # -----------------------------------------------------------------------------
    # Method: decreaseTorch
    #
    # Inputs:
    #   self : reference to the object
    #
    # Return Value:
    #   decreaseTorch does not return a value
    #
    # Example Use:
    #   a = Avatar(1,1)
    #   a.decreaseTorch()
    #   decrease self.torchRadius to 3.5
    #
    # Description:
    #   Decreases the torch radius by .5 for every call, cannot go below 2.0
    # -----------------------------------------------------------------------------
    def decreaseTorch(self):
        if self.torchRadius <= 2.0:
            pass
        else:
            self.torchRadius -= .5

    # -----------------------------------------------------------------------------
    # Method: draw
    #
    # Inputs:
    #   self : reference to the object
    #
    # Return Value:
    #   draw does not return a value
    #
    # Example Use:
    #   a = Avatar(1,1)
    #   a.draw()
    #   draws avatar at (1,1)
    #
    # Description:
    #   Draws the avatar at the set position
    # -----------------------------------------------------------------------------
    def draw(self):
        StdDraw.picture(picture.Picture("avatar.gif"),self.x*16+8,self.y*16+8)

# Main code to test the avatar class    
if __name__ == "__main__":
    # Create an avatar at 5,5
    avatar = Avatar(5, 5)
    print("%d %d %.1f" %(avatar.getX(), avatar.getY(), avatar.getTorchRadius()))
    # Change the avatar's position
    avatar.setLocation(1, 4)
    print("%d %d %.1f" %(avatar.getX(), avatar.getY(), avatar.getTorchRadius()))
    # Increase the torch radius
    avatar.increaseTorch()
    print("%d %d %.1f" %(avatar.getX(), avatar.getY(), avatar.getTorchRadius()))
    # Decrease the torch radius 6 times to make sure it doesn't go below 2.0
    for i in range(0, 6):
        avatar.decreaseTorch()
        print("%d %d %.1f" %(avatar.getX(), avatar.getY(), avatar.getTorchRadius()))
