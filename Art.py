# -----------------------------------------------------------------------------
# 
# File Name: Art.py
#
# Author: Donald Summers
#
# Description:  Code that recursively creates a diamond based fractal with a command
#               line argument that gives it the recursion depth using functions
#
# How to use:   Run the main file in the terminal/prompt with a arguement that
#               represents the recursion depth(doesn't show well past 7)
#
# Example use:  python Art.py 4
#
# -----------------------------------------------------------------------------
import StdDraw
import sys
import math

# -----------------------------------------------------------------------------
# Function: filledDiamond
#
# Inputs:
#   x, y, z: positive floating point numbers
#
# Return Value:
#   filledDiamond does not return a value
#
# Example Use:
#   filledDiamond(.5,0,.5)
#     creates an diamond with a bottom at the vertex (.5,0) with sides of .5 length
#
# Description:
#   Draws a shaded diamond determined by the vertex (x,y) and side length s.
#
# Exceptions:
#   None
# -----------------------------------------------------------------------------
def filledDiamond(x, y, r):
    x = float(x)
    y = float(y)
    r = float(r)
    newR = r/math.sqrt(2)
    StdDraw.filledPolygon([x,x-newR,x,x+newR],[y,y+newR,y+(2*newR),y+newR])
    StdDraw.filledPolygon([x+newR*2,x+newR*2+newR,x+newR*2,x+newR*2-newR],[y,y+newR,y+(2*newR),y+newR])

# -----------------------------------------------------------------------------
# Function: recursor
#
# Inputs:
#   x, y, z: positive floating point numbers
#   n: positive integer
#
# Return Value:
#   recursor does not return a value
#
# Example Use:
#   recursor(3,.5,0,.5)
#     creates a diamond type fractal, with the bottom at vertex (0.5,0)
#     and side length .5 with a recursion depth of 3
#
# Description:
#     Draws two diamonds determined by vertex (x, y) and side length s, and recursively
#     calls itself twice to generate the next (smaller) order diamonds diagonally left
#     and right of bigger one
#
# Exceptions:
#   None
# -----------------------------------------------------------------------------
def recursor(n, x, y, s):
    n = int(n)
    if n == 0:
        pass
    else:
        filledDiamond(x,y+s,s*(math.sqrt(2)/2))
        #filledDiamond(x+s,y+s,s*(math.sqrt(2)/2))
        recursor(n-1,x-s/2,y+s,s/2)
        recursor(n-1,x+s,y+s,s/2)

# -----------------------------------------------------------------------------
# Function: __main__
#
# Inputs:
#   none
#
# Return Value:
#   __main__ does not have a return value
#
# Example Use:
#   __main__()
#     runs the main loop to get the recursion depth from the command line and make a sierpinski fractal
#
# Description:
#     Reads depth of recursion n as a command-line argument; 
#     draws filled triangle with endpoints (.375, .375, (.625, .375), and (1/2, 1/2); 
#     generates an N-order fractal 
#
# Exceptions:
#   None
# -----------------------------------------------------------------------------

def __main__():
    StdDraw.setCanvasSize()
    StdDraw.filledPolygon([.375,.625,.5],[.375,.375,.5])
    recursor(sys.argv[1],.375,.125,.25)
    StdDraw.show(5000)

if __name__ == "__main__":
    __main__()
