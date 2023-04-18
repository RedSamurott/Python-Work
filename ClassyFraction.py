# -----------------------------------------------------------------------------
# 
# File Name: ClassyFraction.py
#
# Author: Donald Summers, code majorly authored by Doug Galarus
#
# Description:  Includes a class, ClassyFraction, that implements functionality
#               for fractions and operations on fractions.
#
# How to use:   Import into another file with "import ClassyFraction as CF" 
#               or similar. Then create instances of the class and use them.
#
#                    import ClassyFraction as CF
#                    
#                    frac1 = CF.ClassyFraction(1, 2)
#                    frac2 = CF.ClassyFraction(2, 3)
#                    frac3 = frac1.multiply(frac2)
#                    print(frac3)
#
# -----------------------------------------------------------------------------


# ----------------------------------------------------------------------------
#
# ClassFraction class - implements functionality for fractions and operations.
#
# ----------------------------------------------------------------------------
class ClassyFraction:
    

    # -----------------------------------------------------------------------------
    # Method: __init__
    #
    # Inputs:
    #   self : reference to the object
    #   numerator, denominator : both integers, non-zero denominator
    #
    # Return Value:
    #   __init__ does not return a value.
    #
    # Example Use:
    #
    #   NOTE: __init__ is not called directly. It is called when the constructor
    #         is called, after space has been allocated for the object.
    #
    #   Example constructor call:
    #
    #   ClassyFraction(1,2)
    #     returns a ClassyFraction object that represents 1/2.
    #
    # Description:
    #   Initializes a ClassyFraction object with given the numerator and denominator.
    #
    # Exceptions:
    #   If either argument is not an integer, then a general Exception
    #     is raised with the message: "The numerator and denominator must be integers."
    #   If the denominator is zero, then a general Exception is rraise with the 
    #     message: "The denominator cannot be zero."
    # -----------------------------------------------------------------------------
    def __init__(self, numerator, denominator):
        # If the numerator is not an integer, throw an exception.
        if isinstance(numerator,int) == False:
            raise Exception("The numerator and denominator must be integers.")
        # If the denominator is not an integer, throw an exception.
        if isinstance(denominator,int) == False:
            raise Exception("The numerator and denominator must be integers.")
        # If the denominator is not an integer, throw an exception.
        if denominator == 0:
            raise Exception("The denominator cannot be zero.")
        # Store the numerator and denominator to instance variables
        self.__numerator = numerator
        self.__denominator = denominator
        
        
    # -----------------------------------------------------------------------------
    # Instance Method: toString
    #
    # Inputs:
    #   none
    #
    # Return Value:
    #   a string representing the ClassyFraction. 
    #
    # Example Use:
    #
    #   frac = ClassyFraction(1,2)
    #   frac.toString()
    #
    #     returns '1/2'
    #
    # Description:
    #   Converts the ClassyFraction to a string.
    #
    # Exceptions:
    #   Should throw no exceptions because the instance ClassyFraction object should
    #   be valid.
    # -----------------------------------------------------------------------------
    def toString(self):
        # Return the string representation.
        return str(self.__numerator) + "/" + str(self.__denominator)
    
    
    # -----------------------------------------------------------------------------
    # Instance Method: __str__
    #
    # Description:
    #   Magic Method to return a simple human readable string representation of the object. 
    #   See toString() method for implementation details.
    # -----------------------------------------------------------------------------
    def __str__(self):
        return self.toString()
    
    
    # -----------------------------------------------------------------------------
    # Instance Method: __repr__
    #
    # Description:
    #   Magic Method to return a simple machine readable string representation of the object.
    #   This text in the string could be used to construct the object.
    # -----------------------------------------------------------------------------
    def __repr__(self):
        return 'ClassyFraction(' + str(self.__numerator) + "," + str(self.__denominator)+')'
    

    # -----------------------------------------------------------------------------
    # Static Method: gcd
    #
    # Inputs:
    #   n1, n2 : positive integers
    #
    # Return Value:
    #   an integer that is the greatest common divisor of n1 and n2
    #
    # Example Use:
    #   ClassyFraction.gcd(100,64)
    #     returns 4
    #
    # Description:
    #   Computes and returns the greatest common divisor of two positive integers 
    #   using Euclid's algorithm. Based on code from the Liang book.
    #
    # Exceptions:
    #   If either argument is not a positive integer, then a general Exception
    #   is raised with the message: "GCD arguments must be positive integers"
    # -----------------------------------------------------------------------------    
    @staticmethod
    def gcd(n1, n2):
        # If the first argument is not an integer, throw an exception.
        if isinstance(n1,int) == False:
            raise Exception("GCD arguments must be positive integers.")
        # If the second argument is not an integer, throw an exception.
        if isinstance(n2,int) == False:
            raise Exception("GCD arguments must be positive integers.")
        # If the first argument is not positive, throw an exception.
        if n1 < 1:
            raise Exception("GCD arguments must be positive integers.")
        # If the second argument is not positive, throw an exception.
        if n2 < 1:
            raise Exception("GCD arguments must be positive integers.")
        # Initial gcd is 1 
        gcd = 1 
        # Candidate gcd
        k = 2  
        # Iterative test candidate gcds to find actual.
        while k <= n1 and k <= n2:
            if n1 % k == 0 and n2 % k == 0:
                # Update gcd
                gcd = k 
            k += 1
        # Return gcd
        return gcd  
    
        
    # -----------------------------------------------------------------------------
    # Instance Method: reduce
    #
    # Inputs:
    #   none
    #
    # Return Value:
    #   a ClassyFraction representing the reduced (lowest terms) fraction
    #
    # Example Use:
    #
    #   frac = ClassyFraction(3,6)
    #   frac.reduce()
    #
    #     returns ClassyFraction(1,2)
    #
    # Description:
    #   Computes and returns a ClassyFraction representing the instance reduced to 
    #   lowest terms
    #
    # Exceptions:
    #   Should throw no exceptions because the instance ClassyFraction object should
    #   be valid.
    # -----------------------------------------------------------------------------
    def reduce(self):
        # Extract the numerator and denominator.
        numerator, denominator = self.__numerator, self.__denominator
        # If the numerator is 0, return (0,1).
        if numerator == 0:
            return (0,1)
        # Keep track of the sign while converter numerator and denominator
        # to positive values.
        sign = 1
        # If the numerator is negative, convert to positive.
        if numerator < 0:
            sign = sign * -1
            numerator = -1 * numerator
        # If the denominator is negative, convert to positive.
        if denominator < 0:
            sign = sign * -1
            denominator = -1 * denominator
        # Compute the gcd. gcd only takes positive values.
        d = self.gcd(numerator, denominator)
        # Compute new (reduced) numerator and denominator.
        newNumerator = sign * numerator // d
        newDenominator = denominator // d
        return ClassyFraction(newNumerator, newDenominator)

    # -----------------------------------------------------------------------------
    # Instance Method: multiply
    #
    # Inputs:
    #   none
    #
    # Return Value:
    #   a ClassyFraction representing the product (in lowest terms)
    #
    # Example Use:
    #
    # frac1 = CF.ClassyFraction(1, 2)
    # frac2 = CF.ClassyFraction(2, 3)
    # frac3 = frac1.multiply(frac2)
    #
    #     returns ClassyFraction(1,3)
    #
    # Description:
    #   Computes and returns a ClassyFraction representing the product of the instance 
    #   and the ClassFraction argument reduced to lowest terms
    #
    # Exceptions:
    #   If the argument passed is not a ClassyFraction, then a general Exception 
    #   is raised with the message: "Not a ClassyFraction"
    # --------------------------------------------------------------------------
    def multiply(self, g):
        # If the first input is not a ClassyFraction, raise an Exception.
        if isinstance(g,ClassyFraction) == False:
            raise Exception("Not a ClassyFraction")
        # Extract the numerators and denominators.
        nf, df = self.__numerator, self.__denominator
        ng, dg = g.__numerator, g.__denominator
        # The product is the product of the numerators over the product of the denominators.
        # Reduce the result and return it.
        return ClassyFraction(nf*ng, df*dg).reduce()
        
        
    # -----------------------------------------------------------------------------
    # Instance Method: __mul__
    #
    # Description:
    #   Magic Method to perform multiplication of ClassyFraction objects. 
    #   See multiple() method for implementation details.
    # -----------------------------------------------------------------------------
    def __mul__(self, g):
        return self.multiply(g)

    # -----------------------------------------------------------------------------
    # Instance Method: toFloat
    #
    # Inputs:
    #   none
    #
    # Return Value:
    #   a ClassyFraction representing the decimal form of a fraction
    #
    # Example Use:
    #
    # frac1 = CF.ClassyFraction(1, 2)
    # frac1.toFloat()
    #
    #     returns 0.5
    #
    # Description:
    #   Computes and returns a ClassyFraction representing the decimal value of the
    #   passed in fraction
    #
    # Exceptions:
    #    Should throw no exceptions because the instance ClassyFraction object should
    #    be valid.
    # --------------------------------------------------------------------------
    def toFloat(self):
        return self.__numerator/self.__denominator
    
    # -----------------------------------------------------------------------------
    # Instance Method: invert
    #
    # Inputs:
    #   none
    #
    # Return Value:
    #   a ClassyFraction that is inverted of the passed in fraction
    #
    # Example Use:
    #
    # frac1 = CF.ClassyFraction(1, 2)
    # frac1.invert()
    #
    #     returns "2/1"
    #
    # Description:
    #   Swaps the numerator and denominator to represent an inverted fraction
    #
    # Exceptions:
    #    If the numerator is 0, then a general Exception is raised
    #    with the message: "Divide by Zero"
    # --------------------------------------------------------------------------
    def invert(self):
        #checks if the numerator is zero
        if self.__numerator == 0:
            raise Exception("Divide by zero")
        return f"{self.__denominator}/{self.__numerator}"
    
    # -----------------------------------------------------------------------------
    # Instance Method: negate
    #
    # Inputs:
    #   none
    #
    # Return Value:
    #   a ClassyFraction that is the negated value of the passed in fraction
    #
    # Example Use:
    #
    # frac1 = CF.ClassyFraction(1, 2)
    # frac1.negate()
    #
    #     returns "-1/2"
    #
    # Description:
    #   Returns a string representation of a negated fraction
    #
    # Exceptions:
    #    Should throw no exceptions because the instance ClassyFraction object should
    #    be valid.
    # --------------------------------------------------------------------------
    def negate(self):
        #checks for cases of positive functions
        if (self.__numerator<0 and self.__denominator<0) or (self.__numerator>0 and self.__denominator>0):
            #returns negative fraction
            return f"-{self.__numerator}/{self.__denominator}"
        #checks for a negative denominator
        elif self.__numerator>0 and self.__denominator<0:
            #returns a positive fraction
            return f"{self.__numerator}/-{self.__denominator}"
        #for a negative numerator
        else:
            #returns a positive fraction
            return f"-{self.__numerator}/{self.__denominator}"

    # -----------------------------------------------------------------------------
    # Instance Method: isEquivalent
    #
    # Inputs:
    #   none
    #
    # Return Value:
    #   Boolean representing if the fractions are equivalent or not
    #
    # Example Use:
    #
    # frac1 = CF.ClassyFraction(1, 2)
    # frac2 = CF.ClassyFraction(3, 6)
    # print(frac1.isEquivalent(frac2))
    #
    #     returns True
    #
    # Description:
    #   Returns a boolean representing whether or not the fraction are equal
    #
    # Exceptions:
    #    Should throw no exceptions because the instance ClassyFraction object should
    #    be valid.
    # --------------------------------------------------------------------------
    def isEquivalent(self, g):
        if self.__numerator/self.__denominator==g.__numerator/g.__denominator:
            return True
        else:
            return False

    # -----------------------------------------------------------------------------
    # Instance Method: divide
    #
    # Inputs:
    #   none
    #
    # Return Value:
    #   A ClassyFraction of a reduced fraciton that was the output of dividing two fractions
    #
    # Example Use:
    #
    # frac1 = CF.ClassyFraction(1, 2)
    # frac2 = CF.ClassyFraction(3, 6)
    # print(frac1.divide(frac2))
    #
    #     returns "1/1"
    #
    # Description:
    #   Returns a ClassyFraction that is a reduced disvisor
    #
    # Exceptions:
    #    If the numerator is 0, then a general Exception is raised
    #    with the message: "Divide by Zero"
    # --------------------------------------------------------------------------
    def divide(self, g):
        #checks if the numerator for the second fraction is 0
        if g.__numerator==0:
            raise Exception("Division by zero")
        else:
            #calls mutiply function with inverted second fraction to then return divided fraction
            return ClassyFraction(self.__numerator*g.__denominator, self.__denominator*g.__numerator).reduce()
    
    # -----------------------------------------------------------------------------
    # Instance Method: add
    #
    # Inputs:
    #   none
    #
    # Return Value:
    #   A ClassyFraction of a reduced fraciton that was the output of adding two fractions
    #
    # Example Use:
    #
    # frac1 = CF.ClassyFraction(1, 2)
    # frac2 = CF.ClassyFraction(3, 6)
    # print(frac1.add(frac2))
    #
    #     returns "1/1"
    #
    # Description:
    #   Returns a ClassyFraction that is a reduced sum
    #
    # Exceptions:
    #    Should throw no exceptions because the instance ClassyFraction object should
    #    be valid.
    # --------------------------------------------------------------------------
    def add(self, g):
        return ClassyFraction((self.__numerator*g.__denominator)+(g.__numerator*self.__denominator), self.__denominator*g.__denominator).reduce()

    # -----------------------------------------------------------------------------
    # Instance Method: subtract
    #
    # Inputs:
    #   none
    #
    # Return Value:
    #   A ClassyFraction of a reduced fraciton that was the output of subtracting two fractions
    #
    # Example Use:
    #
    # frac1 = CF.ClassyFraction(1, 2)
    # frac2 = CF.ClassyFraction(3, 6)
    # print(frac1.subtract(frac2))
    #
    #     returns "0/1"
    #
    # Description:
    #   Returns a ClassyFraction that is a reduced difference
    #
    # Exceptions:
    #    Should throw no exceptions because the instance ClassyFraction object should
    #    be valid.
    # --------------------------------------------------------------------------
    def subtract(self, g):
        return self.add(ClassyFraction(-g.__numerator,g.__denominator))

    # -----------------------------------------------------------------------------
    # Instance Method: pow
    #
    # Inputs:
    #   none
    #
    # Return Value:
    #   A ClassyFraction of a reduced fraciton that was the output of a fraction to a 
    #   certain power
    #
    # Example Use:
    #
    # frac1 = CF.ClassyFraction(1, 2)
    # print(frac1.pow(2))
    #
    #     returns "1/4"
    #
    # Description:
    #   Returns a ClassyFraction that is a reduced exponoated fraction
    #
    # Exceptions:
    #    Should throw no exceptions because the instance ClassyFraction object should
    #    be valid.
    # --------------------------------------------------------------------------
    def pow(self, n):
        if n>=0:
            return ClassyFraction(self.__numerator**n, self.__denominator**n)
        else:
            return ClassyFraction(self.__denominator**abs(n), self.__numerator**abs(n))

    # -----------------------------------------------------------------------------
    # Instance Method: __eq__
    #
    # Description:
    #   Magic Method to perform test of equivalence of ClassyFraction objects. 
    #   See isEquivalent() method for implementation details.
    # -----------------------------------------------------------------------------
    def __eq__(self, g):
        return self.isEquivalent(g)
    
    # -----------------------------------------------------------------------------
    # Instance Method: __add__
    #
    # Description:
    #   Magic Method to perform addition of ClassyFraction objects. 
    #   See add() method for implementation details.
    # -----------------------------------------------------------------------------
    def __add__(self, g):
        return self.add(g)

    # -----------------------------------------------------------------------------
    # Instance Method: __sub__
    #
    # Description:
    #   Magic Method to perform subtraction of ClassyFraction objects. 
    #   See subtract() method for implementation details.
    # -----------------------------------------------------------------------------
    def __sub__(self, g):
        return self.subtract(g)
    
    # -----------------------------------------------------------------------------
    # Instance Method: __truediv__
    #
    # Description:
    #   Magic Method to perform division of ClassyFraction objects. 
    #   See divide() method for implementation details.
    # -----------------------------------------------------------------------------
    def __truediv__(self, g):
        return self.divide(g)

    # -----------------------------------------------------------------------------
    # Instance Method: __pow__
    #
    # Description:
    #   Magic Method to perform exponentation of ClassyFraction objects. 
    #   See pow() method for implementation details.
    # -----------------------------------------------------------------------------
    def __pow__(self, g):
        return self.pow(g)

frac1 = ClassyFraction(1,58)
frac2 = ClassyFraction(3,10)
print(frac1+frac2)