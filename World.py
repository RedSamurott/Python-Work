# -----------------------------------------------------------------------------
# 
# File Name: World.py
#
# Author: Donald Summers
#
# Description:  Part of the Ultima game that sets up the world, including
#               tiles(drawn, lit values), avatar(movement, placement), and
#               prints coordinates for current position, torch radius, and
#               how many tiles are lit
#
#               Update 0.1: updated for threading and monster implimntation
#
# How to use:   Import into another file to run it as a part of Ultima, can
#               also be ran with normally in the terminal with a file system arguemnt
#               and will output the starting position, torch radius, and how many
#               tiles are lit
#
# Example use:  python World.py 10x5.txt
#
# -----------------------------------------------------------------------------

from Tile import Tile
from Avatar import Avatar
from Monster import Monster
import threading
import math
import sys
import StdDraw

# ----------------------------------------------------------------------------
#
# World class - impliments functionality for Ultima game with the world, including
#               tile setup, avatar setup, enemy set up, lighting, and threading
#
# ----------------------------------------------------------------------------
class World:

    # -----------------------------------------------------------------------------
    # Method: __init__
    #
    # Inputs:
    #   self : reference to the object
    #   filename : text file, the actual world in text format so the program can
    #              read it
    #
    # Return Value:
    #   __init__ does not return a value.
    #
    # Example Use:
    #   a = World("30x20.txt")
    #
    # Description:
    #   Initializes the class for use in Ultima game, sets world tiles and avatar
    #   position based on inputed world file, as well as enemy placement and enemy
    #   threads
    # -----------------------------------------------------------------------------
    def __init__(self, filename):
        self.monsterList = []
        self.threadList = []
        self.filename = filename
        self.lock = threading.Lock()
        self.filenameRead = open(filename, "rt")
        self.board = []
        while True:
            line = self.filenameRead.readlines()
            if not line:
                break
            self.board += line
        self.filenameRead.close()
        for x in range(0,len(self.board)):
            self.board[x] = self.board[x].strip()
            self.board[x] = self.board[x].split(" ")
        for x in range(len(self.board)):
            self.board[x] = ' '.join(self.board[x]).split()
        self.width = int(self.board[0][0])
        self.height = int(self.board[0][1])
        self.Ax = int(self.board[1][0])
        self.Ay = int(self.board[1][1])
        self.Ahp = int(self.board[1][2])
        self.Adamage = int(self.board[1][3])
        self.torchRadius = float(self.board[1][4])
        self.avatar = Avatar(self.Ax,self.Ay,self.Ahp,self.Adamage,self.torchRadius)
        self.boardTile = []
        for i in range(self.width):
            self.boardColumn = []
            for j in range(2,self.height+2):
                self.boardColumn.append(Tile(self.board[j][i]))
            self.boardColumn.reverse()
            self.boardTile.append(self.boardColumn)
        for x in range(self.height+2,len(self.board)):
            self.monsterList.append(Monster(self, self.board[x][0], int(self.board[x][1]), int(self.board[x][2]), int(self.board[x][3]), int(self.board[x][4]), int(self.board[x][5])))
        self.threadList = [None] * len(self.monsterList)
        for x in range(len(self.monsterList)):
            self.threadList[x] = threading.Thread(target=self.monsterList[x].run)
            self.threadList[x].start()
        self.tilesLit = 0

        SIZE 	= 16
        WIDTH 	= self.width
        HEIGHT 	= self.height


    # Set up a StdDraw canvas on which to draw the tiles
        StdDraw.setCanvasSize(WIDTH * SIZE, HEIGHT * SIZE)
        StdDraw.setXscale(0.0, WIDTH * SIZE)
        StdDraw.setYscale(0.0, HEIGHT * SIZE)
    
    # -----------------------------------------------------------------------------
    # Method: handleKey
    #
    # Inputs:
    #   self : reference to the object
    #   ch : str, representation of keystroke
    #
    # Return Value:
    #   handleKey does not return a value
    #
    # Example Use:
    #   a = World("30x20.txt")
    #   a.handleKey("w")
    #   moves avatar up one tile if possible
    #
    # Description:
    #   Takes keyboard inputs and makes appropriate movements if possible
    # -----------------------------------------------------------------------------
    def handleKey(self, ch):
        if ch == "w":
            self.avatarMove(self.avatar.x,self.avatar.y+1)
        elif ch == "s":
            self.avatarMove(self.avatar.x,self.avatar.y-1)
        elif ch == "a":
            self.avatarMove(self.avatar.x-1,self.avatar.y)
        elif ch == "d":
            self.avatarMove(self.avatar.x+1,self.avatar.y)
        elif ch == "+":
            self.avatar.increaseTorch()
        elif ch == "-":
            self.avatar.decreaseTorch()
    
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
    #   a = World("30x20.txt")
    #   a.draw
    #   draws the world(any lit tiles) and the avatar
    #
    # Description:
    #   Sets up a int that counts the amount of tiles lit, sets every tile's lit
    #   value to False, then goes into the light method to light specific tiles
    #   according to the torch radius, draws them out, and then draws the avatar and
    #   enemies if the tiles they are on are lit
    # -----------------------------------------------------------------------------
    def draw(self):
        self.tilesLit = 0
        self.setLit(False)
        self.light(self.avatar.getX(),self.avatar.getY(),self.avatar.getTorchRadius())
        for i in range(self.width):
            for j in range(self.height):
                self.boardTile[i][j].draw(i,j)
        self.avatar.draw()
        for x in range(len(self.monsterList)):
            if self.boardTile[self.monsterList[x].x][self.monsterList[x].y].getLit() == True:
                self.monsterList[x].draw()
    
    # -----------------------------------------------------------------------------
    # Method: light
    #
    # Inputs:
    #   self : reference to the object
    #   x, y: int, coordinate system of the avatar's position
    #   r : float, torch radius
    #
    # Return Value:
    #   light does not return a value
    #
    # Example Use:
    #   a = World("30x20.txt")
    #   a.light(1,1,4.0)
    #   goes into recursive method lightDFS and counts how many tiles are lit,
    #   then prints out a formatted list of avatar's position, torch radius,
    #   and how many tiles are lit
    #
    # Description:
    #   Calls the recursive method lightDFS to count how many tiles are lit, and then
    #   print out the avatar's position, torch radius, and how many tiles are lit
    # -----------------------------------------------------------------------------
    def light(self, x, y, r):
        lightTile = self.lightDFS(x,y,x,y,r)
        print(f"light({x}, {y}, {r}) = {lightTile}")

    # -----------------------------------------------------------------------------
    # Method: lightDFS
    #
    # Inputs:
    #   self : reference to the object
    #   x, y : int, avatar's position
    #   currentX, currentY : int, tile coordinates to check to light or not
    #   r : float, torch radius
    #
    # Return Value:
    #   self.tilesLit : int, how many tiles are lit
    #
    # Example Use:
    #   a = World("30x20.txt")
    #   print(a.lightDFS(1,1,1,1,4.0))
    #   prints how many tiles are lit from avatar position (1,1) with torch radius 4
    #
    # Description:
    #   Recursively calls itself to light every tile within radius as long as it doesn't
    #   exceed bounds of game and isn't alredy lit, lights opaque tiles but does not
    #   recurse from there, counts how many tiles were lit
    # -----------------------------------------------------------------------------
    def lightDFS(self, x, y, currentX, currentY, r):
        dx = currentX - x
        dy = currentY - y

        distance = (dx**2 + dy**2) ** .5
        if distance >= r:
            pass
        else:
            if currentX>=self.width or currentY>=self.height:
                pass
            else:
                if self.boardTile[currentX][currentY].getLit() == True:
                    pass
                else:
                    if self.boardTile[currentX][currentY].isOpaque() == True:
                        self.boardTile[currentX][currentY].lit = True
                        self.tilesLit += 1
                    else:
                        if currentX>=0 and currentX<self.width:
                            if currentY>=0 and currentY<self.height:
                                self.boardTile[currentX][currentY].lit = True
                                self.tilesLit += 1
                                self.lightDFS(x,y,currentX+1,currentY,r)
                                self.lightDFS(x,y,currentX-1,currentY,r)
                                self.lightDFS(x,y,currentX,currentY+1,r)
                                self.lightDFS(x,y,currentX,currentY-1,r)
        return self.tilesLit
            
    # -----------------------------------------------------------------------------
    # Method: setLit
    #
    # Inputs:
    #   self : reference to the object
    #   value : boolean, tells if tiles are lit or not
    #
    # Return Value:
    #   setLit does not return a value
    #
    # Example Use:
    #   a = World("30x20.txt")
    #   a.setLit(True)
    #   all tiles are now lit
    #
    # Description:
    #   Sets every tile to value, True means they are all lit, False means they are
    #   all not lit
    # -----------------------------------------------------------------------------
    def setLit(self, value):
        for i in range(self.width):
            for j in range(self.height):
                self.boardTile[i][j].setLit(value)

    # -----------------------------------------------------------------------------
    # Method: avatarAlive
    #
    # Inputs:
    #   self : reference to the object
    #
    # Return Value:
    #   True/False : boolean based on whether the avatar has above 0 HP or not
    #
    # Example Use:
    #   a = World("30x20.txt")
    #   print(a.avatarAlive())
    #   would show "True"
    #
    # Description:
    #   Returns a boolean value to see if the avatar is alive or not
    # -----------------------------------------------------------------------------
    def avatarAlive(self):
        if self.avatar.hp > 0:
            return True
        else:
            return False
    
    # -----------------------------------------------------------------------------
    # Method: avatarMove
    #
    # Inputs:
    #   self : reference to the object
    #   x, y : int, new position to try and move to
    #
    # Return Value:
    #   avatarMove does not return a value
    #
    # Example Use:
    #   a = World("30x20.txt")
    #   a.avatarMove(2,2)
    #   would attempt to move the avatar to (2,2)
    #
    # Description:
    #   Determines if it's possible for the avatar to move to (x,y), if not, it stays
    #   in place. If an enemy is there, it deals damage to the enemy and removes the
    #   enemy from the monsterList if it's HP drops below 0. If the tile it moves to 
    #   is lava, the avatar takes one damage
    # -----------------------------------------------------------------------------
    def avatarMove(self, x, y):
        self.lock.acquire()
        if y < self.height and y >= 0 and x < self.width and x >= 0 and self.boardTile[x][y].isPassable() == True:
            tileOpen = True
            for z in range(len(self.monsterList)):
                if x == self.monsterList[z].x and y ==self.monsterList[z].y:
                    tileOpen = False
                    monsterNumber = z
            if tileOpen == True:
                self.avatar.setLocation(x,y)
                if self.boardTile[x][y].getDamage() == 1:
                    self.avatar.incurDamage(1)
            else:
                self.monsterList[monsterNumber].incurDamage(self.avatar.getDamage())
                if self.monsterList[monsterNumber].hp <= 0:
                    self.monsterList.pop(monsterNumber)
        self.lock.release()

    # -----------------------------------------------------------------------------
    # Method: monsterMove
    #
    # Inputs:
    #   self : reference to the object
    #   x, y : int, position to try and move to
    #   monster : Monster object, current monster object to try and move
    #
    # Return Value:
    #   monsterMove does not return a value
    #
    # Example Use:
    #   a = World("30x20.txt")
    #   a.monsterMove(2,2,monster1)
    #   would attempt to move monster1 to (2,2)
    #
    # Description:
    #   Determines if it's possible for the monster to move to (x,y), if not, it stays
    #   in place. If the avatar is there, it deals damage to the avatar and ends the
    #   game if it's HP drops below 0. If the tile it moves to is lava, the monster takes one damage
    # -----------------------------------------------------------------------------
    def monsterMove(self, x, y, monster):
        self.lock.acquire()
        if y < self.height and y >= 0 and x < self.width and x >= 0 and self.boardTile[x][y].isPassable() == True:
            tileOpen = True
            avatarThere = False
            for z in range(len(self.monsterList)):
                if x == self.monsterList[z].x and y == self.monsterList[z].y:
                    tileOpen = False
                if x == self.avatar.x and y == self.avatar.y:
                    tileOpen = False
            if x == self.avatar.x and y == self.avatar.y:
                avatarThere = True
            if tileOpen == True:
                monster.setLocation(x,y)
                if self.boardTile[x][y].getDamage() == 1:
                    monster.incurDamage(1)
                    if monster.hp <= 0:
                        self.monsterList.remove(monster)
            else:
                if avatarThere == True:
                    self.avatar.incurDamage(monster.damage)
        self.lock.release()

    # -----------------------------------------------------------------------------
    # Method: getNumMonsters
    #
    # Inputs:
    #   self : reference to the object
    #
    # Return Value:
    #   len(self.monsterList) : int, how many monsters are alive
    #
    # Example Use:
    #   a = World("30x20.txt")
    #   print(a.getNumMonsters())
    #   would print however many monster objects are in the list currently
    #
    # Description:
    #   Returns how many monsters are still alive
    # -----------------------------------------------------------------------------
    def getNumMonsters(self):
        return len(self.monsterList)
    
# Main code to test the world class
if __name__ == "__main__":
    world0 = World(sys.argv[1])
    world0.draw()
    StdDraw.show()
