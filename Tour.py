# -----------------------------------------------------------------------------
# 
# File Name: Tour.py
#
# Author: Donald Summers
#
# Description:  Takes points from test API code and makes a tour out of the points
#               trying to solve the Traveling Salesmen problem
#
# How to use:   Import the file into another Python file as "import Tour" and use
#               any of the methods listed below to display a solution to the
#               Travelling Salesmen problem, as well as draw the tour, print out
#               the tour, and the distance of the tour.
#
# Example use:  (in another file titled "InOrderInsertion.py")
#               python InOrderInsertion.py tsp10.txt
#
# -----------------------------------------------------------------------------

import StdDraw
import math
import Point


# ----------------------------------------------------------------------------
#
# Node class - implements functionality for implementing nodes for a linked list structure
#
# ----------------------------------------------------------------------------
class Node:

    # -----------------------------------------------------------------------------
    # Method: __init__
    #
    # Inputs:
    #   self : reference to the object
    #   P: Point object
    #
    # Return Value:
    #   __init__ does not return a value.
    #
    # Example Use:
    #   a = Node(p)
    #
    # Description:
    #   Initializes the class for use through the Tour class to make a linked list structure
    # -----------------------------------------------------------------------------

    def __init__(self, p):
    # This will hold the data, in this case a 2D point
        self.p = p
    # This will be the pointer to the next node
        self.next = None

# ----------------------------------------------------------------------------
#
# Tour class - implements functionality for outputting the tours created by three of the methods to solve for the Traveling Salesperson Problem
#
# ----------------------------------------------------------------------------

class Tour:

    # -----------------------------------------------------------------------------
    # Method: __init__
    #
    # Inputs:
    #   self : reference to the object
    #
    # Return Value:
    #   __init__ does not return a value.
    #
    # Example Use:
    #   a = Tour()
    #
    # Description:
    #   Initializes the class for use through a main fuction or imported into another code for solving the Traveling Salesperson Problem
    # -----------------------------------------------------------------------------
    def __init__(self):
        self.length = 0
        self.start = None
        self.end = None

    # -----------------------------------------------------------------------------
    # Instance Method: show
    #
    # Inputs:
    #   self : reference to the object
    #
    # Return Value:
    #   none
    #
    # Example Use:
    #
    #   a = Tour()
    #   Tour.show()
    #
    #     prints out all coordinates in tour order
    #
    # Description:
    #   print the tour to standard output
    # -----------------------------------------------------------------------------
    def show(self):
        count = 0
        current = self.start
        while count < self.length: 
            print(current.p.toString())
            current = current.next
            count += 1

    # -----------------------------------------------------------------------------
    # Instance Method: draw
    #
    # Inputs:
    #   self : reference to the object
    #
    # Return Value:
    #   none
    #
    # Example Use:
    #
    #   a = Tour()
    #   Tour.draw()
    #
    #     draws the complete tour in order
    #
    # Description:
    #   draw the tour to standard draw
    # -----------------------------------------------------------------------------
    def draw(self):
        count = 0
        current = self.start
        while count < self.length:
            current.p.draw()
            current = current.next
            count += 1
        count = 0
        current = self.start
        while count < self.length: 
            current.p.drawTo(current.next.p)
            current = current.next
            count += 1

    # -----------------------------------------------------------------------------
    # Instance Method: size
    #
    # Inputs:
    #   self : reference to the object
    #
    # Return Value:
    #   self.length: the length of the tour
    #
    # Example Use:
    #
    #   a = Tour()
    #   b = Tour.size()
    #   print(b)
    #
    #     returns the tour size as an integer
    #
    # Description:
    #   number of points on tour (int)
    # -----------------------------------------------------------------------------
    def size(self):
        return self.length

    # -----------------------------------------------------------------------------
    # Instance Method: distance
    #
    # Inputs:
    #   self : reference to the object
    #
    # Return Value:
    #   none
    #
    # Example Use:
    #
    #   a = Tour()
    #   b = Tour.distance()
    #   print(b)
    #
    #     returns the distance of the entire tour
    #
    # Description:
    #   return the total distance of the tour(float)
    # -----------------------------------------------------------------------------
    def distance(self):
        count = 0
        distance = 0
        current = self.start
        while count < self.length:
            distance += current.p.distanceTo(current.next.p)
            current = current.next
            count += 1
        return distance

    # -----------------------------------------------------------------------------
    # Instance Method: insertInOrder
    #
    # Inputs:
    #   self : reference to the object
    #   p: Point object
    #
    # Return Value:
    #   none
    #
    # Example Use:
    #
    #   a = Tour()
    #   b = Tour.insertInOrder(p)
    #
    #     creates a tour for the Traveling Salesperson Problem where each point is in order
    #     of how it was put in
    #
    # Description:
    #   insert p using in order heuristic
    # -----------------------------------------------------------------------------
    def insertInOrder(self, p):
        if self.length == 0:
            self.start = Node(p)
            self.length = 1
        else:
            count = 1
            current = self.start
            while count < self.length: 
                current=current.next
                count += 1
            current.next = Node(p)
            self.end = current.next
            self.end.next = self.start
            self.length += 1

    # -----------------------------------------------------------------------------
    # Instance Method: insertNearest
    #
    # Inputs:
    #   self : reference to the object
    #   p: Point object
    #
    # Return Value:
    #   none
    #
    # Example Use:
    #
    #   a = Tour()
    #   b = Tour.insertNearest(p)
    #
    #     creates a tour for the Traveling Salesperson Problem where each point is in order
    #     of which other point in the tour is closest to it
    #
    # Description:
    #   insert p using nearest neighbor heuristic
    # -----------------------------------------------------------------------------
    def insertNearest(self, p):
        if self.length == 0:
            self.start = Node(p)
            self.start.next = self.start
            self.length = 1
        else:
            count = 1
            current = self.start
            nearestNode = Node(p)
            smallestDistance = math.inf
            while count < self.length:
                if current.p.distanceTo(p) < smallestDistance:
                    smallestDistance = current.p.distanceTo(p)
                    nearestNode = current
                current = current.next
                count += 1
            newNode = Node(p)
            newNode.next = nearestNode.next
            nearestNode.next = newNode
            self.length += 1
            
    # -----------------------------------------------------------------------------
    # Instance Method: insertSmallest
    #
    # Inputs:
    #   self : reference to the object
    #   p: Point object
    #
    # Return Value:
    #   none
    #
    # Example Use:
    #
    #   a = Tour()
    #   b = Tour.insertSmallest(p)
    #
    #     creates a tour for the Traveling Salesperson Problem where each point is in order
    #     of where in the tour it would at the least amount of distance between two point
    #
    # Description:
    #   insert p using nearest neighbor heuristic
    # -----------------------------------------------------------------------------     
    # insert p using smallest increase heuristic
    def insertSmallest(self, p):
        if self.length == 0:
            self.start = Node(p)
            self.start.next = self.start
            self.length = 1
        else:
            count = 1
            current = self.start
            nearestNode = Node(p)
            smallestDistance = math.inf
            while count < self.length:
                distance = p.distanceTo(current.p) + current.next.p.distanceTo(p) - current.p.distanceTo(current.next.p)
                if distance < smallestDistance:
                    smallestDistance = distance
                    nearestNode = current
                current = current.next
                count += 1
            newNode = Node(p)
            newNode.next = nearestNode.next
            nearestNode.next = newNode
            self.length += 1
