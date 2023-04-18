# ----------------------------------------------------------------------------
#
# Node class - implements functionality for implementing nodes for a queue structure
#
# ----------------------------------------------------------------------------
class Node:

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
    #   a = Node()
    #
    # Description:
    #   Initializes the class for use through the QueueOfPositions class for a queue structure
    # -----------------------------------------------------------------------------
    def __init__(self):
        self.item = ""
        self.next = None

# ----------------------------------------------------------------------------
#
# QueueOfPositions class - implements functionality for a queue stucture with adding, removing and printing
#
# ----------------------------------------------------------------------------
class QueueOfPositions:

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
    #   a = QueueOfPositions()
    #
    # Description:
    #   Initializes the class for use through the Solve program to make a queue structure
    # -----------------------------------------------------------------------------
    def __init__(self):
        self.first = None
        self.last  = None

    # -----------------------------------------------------------------------------
    # Method: enqueue
    #
    # Inputs:
    #   self : reference to the object
    #   s: Position object
    #
    # Return Value:
    #   enqueue does not return a value.
    #
    # Example Use:
    #   a = QueueOfPositions()
    #   b = Positions(3,4)
    #   a.enqueue(b)
    #
    # Description:
    #   Add a new position to the queue
    # -----------------------------------------------------------------------------
    def enqueue(self, s):
        node = Node()
        node.item = s
        node.next = None

        if self.last != None:
            self.last.next = node
        self.last = node

        if self.first == None:
            self.first = node

    # -----------------------------------------------------------------------------
    # Method: dequeue
    #
    # Inputs:
    #   self : reference to the object
    #
    # Return Value:
    #   dequeue does not return a value.
    #
    # Example Use:
    #   a = QueueOfPositions()
    #   a.dequeue()
    #
    # Description:
    #   Remove the least recently added position
    # -----------------------------------------------------------------------------
    def dequeue(self):
        if self.first == None:
            raise Exception("Queue is empty!")
        result = self.first.item
        self.first = self.first.next
        if self.first == None:
            self.last = None
        return result

    # -----------------------------------------------------------------------------
    # Method: toString
    #
    # Inputs:
    #   self : reference to the object
    #
    # Return Value:
    #   a string representation of the queue
    #
    # Example Use:
    #   a = QueueOfPositions()
    #   print(a.toString())
    #
    # Description:
    #   Return a string representation of the queue
    # -----------------------------------------------------------------------------	
    def toString(self):
        result = ""
        current = self.first
        while current != None:
            result += current.item.toString
            result += " "
            current = current.next.toString
        return result
	
    # -----------------------------------------------------------------------------
    # Method: isEmpty
    #
    # Inputs:
    #   self : reference to the object
    #
    # Return Value:
    #   self.first = None, basically if there's nothing in the queue, it returns None
    #
    # Example Use:
    #   a = QueueOfPositions()
    #   print(a.isEmpty)
    #
    # Description:
    #   Check if the queue is empty
    # -----------------------------------------------------------------------------
    def isEmpty(self):
        return self.first == None
    
# main method for testing out the class
if __name__ == "__main__":
    q = QueueOfPositions()

    print("queue = " + q.toString())

    q.enqueue("this")
    print(q.toString())

    print("dequeue = " + q.dequeue())
    print(q.toString())

    q.enqueue("a")
    q.enqueue("b")
    q.enqueue("c")
    print(q.toString())

    print("dequeue = " + q.dequeue())
    print(q.toString())
    print("dequeue = " + q.dequeue())
    print(q.toString())
    print("dequeue = " + q.dequeue())
    print(q.toString())
