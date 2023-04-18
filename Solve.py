# -----------------------------------------------------------------------------
# 
# File Name: Solve.py
#
# Author: Donald Summers
#
# Description:  makes a maze with the given Mazz class and solves it using 
#               a stack solving method and a queue solving method using a 
#               Position class to keep track of movement and a StackOfPositions
#               and QueueOfPositions to keep the positions in their respective
#               data field order
#
# How to use:   Run the main file in the terminal/prompt with a system argument
#               that specifies the size of the maze
#
# Example use:  python Solve.py 5
#
# -----------------------------------------------------------------------------
import sys
from StdDraw import *
from Maze import Maze
from Position import Position
from StackOfPositions import StackOfPositions
from QueueOfPositions import QueueOfPositions

#if the program is called in the terminal/prompt, it will run this code
if __name__ == "__main__":
    #checks for a system argument
    if len(sys.argv) != 2:
        print("Ex. use: python Solve.py 5")
    else:
        #creates the maze
        maze = Maze(int(sys.argv[1]))
        maze.draw()
        mazeStart = maze.getStart()
        mazeFinish = maze.getFinish()
        
        #sets up empty stack and queue
        stack = StackOfPositions()
        queue = QueueOfPositions()
        
        #gets the inital position into the stack, as well as starts the counter for how many positions the code runs through
        stack.push(mazeStart)
        stackLength = 1
        pos = mazeStart
        maze.setVisited(pos)
        
        #while loop to make sure it always runs and solves since it shouldn't terminate before it gets a solution
        while stack.isEmpty != True:
            #draws the current position in light blue, and when it moves to the next postion, draws it in red
            pos.draw(BOOK_LIGHT_BLUE)
            pos = stack.pop()
            pos.draw(RED)
            #functions as the terminator for the loop once it reaches the finish point
            if pos.getX() == mazeFinish.getX() and pos.getY() == mazeFinish.getY():
                break
            #checks and sees if it can go north and the north position hasn't been gone through yet; adds to stack if true
            if maze.openNorth(pos):
                newPos = Position(pos.getX(),pos.getY()+1)
                if not maze.isVisited(newPos):
                    maze.setVisited(newPos)
                    stack.push(newPos)
            #checks and sees if it can go south and the south position hasn't been gone through yet; adds to stack if true
            if maze.openSouth(pos):
                newPos = Position(pos.getX(),pos.getY()-1)
                if not maze.isVisited(newPos):
                    maze.setVisited(newPos)
                    stack.push(newPos)
            #checks and sees if it can go east and the east position hasn't been gone through yet; adds to stack if true
            if maze.openEast(pos):
                newPos = Position(pos.getX()+1,pos.getY())
                if not maze.isVisited(newPos):
                    maze.setVisited(newPos)
                    stack.push(newPos)
            #checks and sees if it can go west and the west position hasn't been gone through yet; adds to stack if true
            if maze.openWest(pos):
                newPos = Position(pos.getX()-1,pos.getY())
                if not maze.isVisited(newPos):
                    maze.setVisited(newPos)
                    stack.push(newPos)
            stackLength += 1 
            time.sleep(0.1)
        
        #prints how many postions the stack method went through before it found the finish position
        print(f"Stack Length: {stackLength}")
        #clears the maze and setVisited for the queue method
        maze.clear()

        #gets the inital position into the queue, as well as starts the counter for how many positions the code runs through
        queue.enqueue(mazeStart)
        queueLength = 1
        pos = mazeStart
        maze.setVisited(pos)

        #while loop to make sure it always runs and solves since it shouldn't terminate before it gets a solution
        while queue.isEmpty != True:
            #draws the current position in light gray, and when it moves to the next postion, draws it in dark red
            pos.draw(LIGHT_GRAY)
            pos = queue.dequeue()
            pos.draw(DARK_RED)
            #functions as the terminator for the loop once it reaches the finish point
            if pos.getX() == mazeFinish.getX() and pos.getY() == mazeFinish.getY():
                break
            #checks and sees if it can go north and the north position hasn't been gone through yet; adds to queue if true
            if maze.openNorth(pos):
                newPos = Position(pos.getX(),pos.getY()+1)
                if not maze.isVisited(newPos):
                    maze.setVisited(newPos)
                    queue.enqueue(newPos)
            #checks and sees if it can go south and the south position hasn't been gone through yet; adds to queue if true
            if maze.openSouth(pos):
                newPos = Position(pos.getX(),pos.getY()-1)
                if not maze.isVisited(newPos):
                    maze.setVisited(newPos)
                    queue.enqueue(newPos)
            #checks and sees if it can go east and the east position hasn't been gone through yet; adds to queue if true
            if maze.openEast(pos):
                newPos = Position(pos.getX()+1,pos.getY())
                if not maze.isVisited(newPos):
                    maze.setVisited(newPos)
                    queue.enqueue(newPos)
            #checks and sees if it can go west and the west position hasn't been gone through yet; adds to queue if true
            if maze.openWest(pos):
                newPos = Position(pos.getX()-1,pos.getY())
                if not maze.isVisited(newPos):
                    maze.setVisited(newPos)
                    queue.enqueue(newPos)
            queueLength += 1 
            time.sleep(0.1)

        #prints how many postions the queue method went through before it found the finish position
        print(f"Queue Length: {queueLength}")

    

