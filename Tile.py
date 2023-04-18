# -----------------------------------------------------------------------------
# 
# File Name: Tile.py
#
# Author: Donald Summers
#
# Description:  Part of the Ultima game that sets up the tiles based on codes
#               put into the class, which then allows the tiles to be set as
#               lit or not, as well as set which tiles can light pass through
#               and which tiles the player can pass through. 
#               
#               Update 0.1: Added method for lava causing damage
#
# How to use:   Import into another file to run it as a part of Ultima, can
#               also be ran with normally in the terminal and will output each
#               tile's values
#
# Example use:  python Tile.py
#
# -----------------------------------------------------------------------------

from enum import Enum, auto
import picture
import StdDraw

#Enumeration class to handle different tile types
class TileType(Enum):
    INVALID = auto()
    FLOOR = auto()
    LAVA = auto()
    WATER = auto()
    FOREST = auto()
    GRASS = auto()
    MOUNTAIN = auto()
    WALL = auto()

# ----------------------------------------------------------------------------
#
# Tile class - impliments functionality Ultima game with all the tiles, 
#              including lit status, opaqueness, and passability by player
#
# ----------------------------------------------------------------------------
class Tile:
    # Static variable associated with tiles to specity the size
    SIZE = 16

    # -----------------------------------------------------------------------------
    # Method: __init__
    #
    # Inputs:
    #   self : reference to the object
    #   code : letter that references tile
    #
    # Return Value:
    #   __init__ does not return a value.
    #
    # Example Use:
    #   a = Tile("B")
    #
    # Description:
    #   Initializes the class for use in Ultima game
    # -----------------------------------------------------------------------------
    def __init__(self, code):
        self.code = code
        self.lit = False

    # -----------------------------------------------------------------------------
    # Method: getLit
    #
    # Inputs:
    #   self : reference to the object
    #
    # Return Value:
    #   self.lit : boolean value
    #
    # Example Use:
    #   a = Tile("B")
    #   print(a.getLit())
    #   would print "False"
    #
    # Description:
    #   Returns the lit value for a tile, intially always False
    # -----------------------------------------------------------------------------
    def getLit(self):
        return self.lit

    # -----------------------------------------------------------------------------
    # Method: setLit
    #
    # Inputs:
    #   self : reference to the object
    #   value : boolean value
    #
    # Return Value:
    #   setLit does not return a value
    #
    # Example Use:
    #   a = Tile("B")
    #   a.setLit(True)
    #   sets tile's lit value to True
    #
    # Description:
    #   Makes a tile's lit value True, which allows it to be drawn
    # -----------------------------------------------------------------------------
    def setLit(self, value):
        self.lit = value

    # -----------------------------------------------------------------------------
    # Method: isOpaque
    #
    # Inputs:
    #   self : reference to the object
    #
    # Return Value:
    #   True/False, depending if the tile is opaque or not
    #
    # Example Use:
    #   a = Tile("B")
    #   print(a.isOpaque())
    #   would print "False"
    #
    # Description:
    #   Returns a boolean value for if the tile is opaque or not
    # -----------------------------------------------------------------------------
    def isOpaque(self):
        if self.code == "F" or self.code == "M" or self.code == "S":
            return True
        return False

    # -----------------------------------------------------------------------------
    # Method: isPassable
    #
    # Inputs:
    #   self : reference to the object
    #
    # Return Value:
    #   True/False, depending if the tile can be passed through ot not
    #
    # Example Use:
    #   a = Tile("B")
    #   print(a.isPassable())
    #   would print "True"
    #
    # Description:
    #   Returns a boolean value for if the tile can be passed through or not
    # -----------------------------------------------------------------------------
    def isPassable(self):
        if self.code == "B" or self.code == "L" or self.code == "F" or self.code == "G":
            return True
        return False
    
    # -----------------------------------------------------------------------------
    # Method: getDamage
    #
    # Inputs:
    #   self : reference to the object
    #
    # Return Value:
    #   1 or 0, depending if the tile is lava or not
    #
    # Example Use:
    #   a = Tile("B")
    #   print(a.getDamage())
    #   would print "0"
    #
    # Description:
    #   Returns 1 or 0, depending on if the tile is lava and therefore, would damage
    # -----------------------------------------------------------------------------
    def getDamage(self):
        if self.code == "L":
            return 1
        else:
            return 0

    # -----------------------------------------------------------------------------
    # Method: draw
    #
    # Inputs:
    #   self : reference to the object
    #   x, y : int, coordinate system to place tiles on
    #
    # Return Value:
    #   draw does not return a value
    #
    # Example Use:
    #   a = Tile("B")
    #   a.draw(1,1)
    #   would place a brick floor tile at coordinates (1,1)
    #
    # Description:
    #   Draws a picture of a specific tile at a specific coordinate if it is lit
    #   otheriwse draws a blank square
    # -----------------------------------------------------------------------------
    def draw(self, x, y):
        if self.lit == True:
            if self.code == "B":
                currentTile = picture.Picture("brickfloor.gif")
            elif self.code == "L":
                currentTile = picture.Picture("lava.gif")
            elif self.code == "W":
                currentTile = picture.Picture("water.gif")
            elif self.code == "F":
                currentTile = picture.Picture("forest.gif")
            elif self.code == "G":
                currentTile = picture.Picture("grasslands.gif")
            elif self.code == "M":
                currentTile = picture.Picture("mountains.gif")
            elif self.code == "S":
                currentTile = picture.Picture("stonewall.gif")
            StdDraw.picture(currentTile,x*16+8,y*16+8)
        else:
            StdDraw.picture(picture.Picture("blank.gif"),x*16+8,y*16+8)

#
# Main code for testing the Tile class
#
if __name__ == "__main__":
    # Set up test parameters
    SIZE 	= 16
    WIDTH 	= 7
    HEIGHT 	= 2

    # Set up a StdDraw canvas on which to draw the tiles
    StdDraw.setCanvasSize(WIDTH * SIZE, HEIGHT * SIZE)
    StdDraw.setXscale(0.0, WIDTH * SIZE)
    StdDraw.setYscale(0.0, HEIGHT * SIZE)

    # Create a list of codes to test tile creation
    codes = ["B", "L", "W", "F", "G", "M", "S"]
    for i in range(0, WIDTH):
        for j in range(0, HEIGHT):
            tile = Tile(codes[i])
            # Light every second tile
            if (i + j) % 2 == 0:
                tile.setLit(True)
            print("%d %d : lit %s\topaque %s\tpassable %s" %(i, j, tile.getLit(), tile.isOpaque(), tile.isPassable()))
            tile.draw(i, j)
    StdDraw.show(5000)
