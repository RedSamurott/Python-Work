# -----------------------------------------------------------------------------
# 
# File Name: Sierpinski.py
#
# Author: Donald Summers
#
# Description:  Code that recursively creates a sierpinski fractal with a command
#               line argument that gives it the recursion depth using functions
#
# How to use:   Run the main file in the terminal/prompt with a arguement that
#               represents the recursion depth(doesn't show well past 7)
#
# Example use:  python Sierpinski.py 4
#
# -----------------------------------------------------------------------------
import StdDraw
import sys
import math

# -----------------------------------------------------------------------------
# Function: filledTriangle
#
# Inputs:
#   x, y, s: positive floating point numbers
#
# Return Value:
#   filledTriangle does not return a value
#
# Example Use:
#   filledTriangle(.5,0,.5)
#     creates an upside triangle at the vertex (.5,0) with sides of .5 length
#
# Description:
#   Draws a shaded equilateral triangle determined by the vertex (x,y) and side length s.
#
# Exceptions:
#   None
# -----------------------------------------------------------------------------
def filledTriangle(x, y, s):
    x = float(x)
    y = float(y)
    s = float(s)
    StdDraw.filledPolygon([x,x-s/2,x+s/2],[y,y+s/math.sqrt(4/3),y+s/math.sqrt(4/3)])


# -----------------------------------------------------------------------------
# Function: sierpinski
#
# Inputs:
#   x, y, s: positive floating point numbers
#   n: positive integer
#
# Return Value:
#   sierpinski does not return a value
#
# Example Use:
#   sierpinski(3,.5,0,.5)
#     creates a sierpinski fractal triangle, with the inital triangle at vertex (0.5,0)
#     and side length .5 with a recursion depth of 3
#
# Description:
#     Draws one triangle determined by vertex (x, y) and side length s, and recursively
#     calls itself three times to generate the next (smaller) order triangles above, left
#     and right of the current triangle
#
# Exceptions:
#   None
# -----------------------------------------------------------------------------
def sierpinski(n, x, y, s):
    n = int(n)
    if n == 0:
        pass
    else:
        filledTriangle(x,y,s)
        sierpinski(n-1,x-s/2,y,s/2)
        sierpinski(n-1,x,y+s/math.sqrt(4/3),s/2)
        sierpinski(n-1,x+s/2,y,s/2)

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
#     draws gray outline triangle with endpoints (0, 0), (1, 0), and (1/2, √3/2); 
#     generates an N-order Sierpinski triangle inside the outline
#
# Exceptions:
#   None
# -----------------------------------------------------------------------------

def __main__():
    StdDraw.setCanvasSize()
    StdDraw.polygon([0,1,.5],[0,0,math.sqrt(3)/2])
    sierpinski(sys.argv[1],.5,0,.5)
    StdDraw.show(5000)

if __name__ == "__main__":
    __main__()
