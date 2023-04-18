# ----------------------------------------------------------------------------
#
# Node class - implements functionality for implementing nodes for a stack structure
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
    #   Initializes the class for use through the StackOfPositions class for a stack structure
    # -----------------------------------------------------------------------------
    def __init__(self):
        self.item = ""
        self.next = None

# ----------------------------------------------------------------------------
#
# StackOfPositions class - implements functionality for a stack stucture with adding, removing and printing
#
# ----------------------------------------------------------------------------
class StackOfPositions:

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
    #   a = StackOfPositions()
    #
    # Description:
    #   Initializes the class for use through the Solve program to make a stack structure
    # -----------------------------------------------------------------------------
    def __init__(self):
        self.first = None

    # -----------------------------------------------------------------------------
    # Method: push
    #
    # Inputs:
    #   self : reference to the object
    #   s: Position object
    #
    # Return Value:
    #   push does not return a value.
    #
    # Example Use:
    #   a = StackOfPositions()
    #   b = Positions(3,4)
    #   a.push(b)
    #
    # Description:
    #   Add a new position to the stack
    # -----------------------------------------------------------------------------
    
    def push(self, s):
        node = Node()
        node.item = s;

        if self.first == None:
            self.first = node
        else:
            node.next = self.first
            self.first = node

    # -----------------------------------------------------------------------------
    # Method: pop
    #
    # Inputs:
    #   self : reference to the object
    #
    # Return Value:
    #   pop does not return a value.
    #
    # Example Use:
    #   a = StackOfPositions()
    #   a.pop()
    #
    # Description:
    #   Remove the most recently added position
    # -----------------------------------------------------------------------------
    def pop(self):
        if self.first == None:
            raise Exception("Stack is empty!")
        result = self.first.item
        self.first = self.first.next
        return result

    # -----------------------------------------------------------------------------
    # Method: toString
    #
    # Inputs:
    #   self : reference to the object
    #
    # Return Value:
    #   a string representation of the stack
    #
    # Example Use:
    #   a = StackOfPositions()
    #   print(a.toString())
    #
    # Description:
    #   Return a string representation of the stack	
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
    #   self.first = None, basically if there's nothing in the stack, it returns None
    #
    # Example Use:
    #   a = StackOfPositions()
    #   print(a.isEmpty)
    #
    # Description:
    #   Check if the stack is empty
    # -----------------------------------------------------------------------------
    def isEmpty(self):
        return self.first == None
    
# main method for testing out the class
if __name__ == "__main__":
    q = StackOfPositions()

    print("stack = " + q.toString())

    q.push("this")
    print(q.toString())

    print("pop = " + q.pop())
    print(q.toString())

    q.push("a")
    q.push("b")
    q.push("c")
    print(q.toString())

    print("pop = " + q.pop())
    print(q.toString())
    print("pop = " + q.pop())
    print(q.toString())
    print("pop = " + q.pop())
    print(q.toString())		
