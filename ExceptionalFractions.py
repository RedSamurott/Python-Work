# -----------------------------------------------------------------------------
# 
# File Name: ExceptionalFractions.py
#
# Author: Donald Summers, major parts authored by Douglas Galarus
#
# Description:  A collection of functions to represent fractions and  
#               perform operations on fractions. Fractions are represented
#               as tuples (n,d) where n and d are integers and d is non-
#               zero. n is the numerator and d is the denominator. 
#               For instance (1,2) represents one-half.
#
# How to use:   Import into another file with "import ExceptionalFractions as EF" 
#               or similar. The functions can then be called and used. 
#               For example:
#
#                   EF.makeFraction(1,2)
#                   EF.addFractions((1,2),(3,4))
#
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# Function: gcd
#
# Inputs:
#   n1, n2 : positive integers
#
# Return Value:
#   an integer that is the greatest common divisor of n1 and n2
#
# Example Use:
#   gcd(100,64)
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
# Function: makeFraction
#
# Inputs:
#   numerator, denominator : both integers, non-zero denominator
#
# Return Value:
#   a tuple that represents the fraction: (numerator, denominator)
#
# Example Use:
#   makeFraction(1,2)
#     returns (1, 2)
#
# Description:
#   Makes a tuple that represents the fraction with the given numerator and 
#   denominiator.
#
# Exceptions:
#   If either argument is not an integer, then a general Exception
#     is raised with the message: "The numerator and denominator must be integers."
#   If the denominator is zero, then a general Exception is rraise with the 
#     message: "The denominator cannot be zero."
# -----------------------------------------------------------------------------
def makeFraction(numerator, denominator):
    # If the numerator is not an integer, throw an exception.
    if isinstance(numerator,int) == False:
        raise Exception("The numerator and denominator must be integers.")
    # If the denominator is not an integer, throw an exception.
    if isinstance(denominator,int) == False:
        raise Exception("The numerator and denominator must be integers.")
    # If the denominator is not an integer, throw an exception.
    if denominator == 0:
        raise Exception("The denominator cannot be zero.")
    # Return the tuple containing the numerator and denominator.
    return (numerator, denominator)
   

# -----------------------------------------------------------------------------
# Function: isValidFraction
#
# Inputs:
#   f : a tuple representation of a fraction (numerator, denominator)
#
# Return Value:
#   a boolean indicating whether the input is a valid representation of a fraction.
#
# Example Use:
#   isValidFraction((1,2))
#     returns True
#   isValidFraction((1,0))
#     returns False
#
# Description:
#   Tests to see if the input is a valid representation of a fraction as a tuple.
#
# Exceptions:
#   No exceptions should be raised. False will be returned if the input is not
#     a valid representation.
# -----------------------------------------------------------------------------
def isValidFraction(f):
    # If it isn't a tuple, return False.
    if isinstance(f,tuple) == False:
        return False
    # If the length is not 2, return false.
    if len(f) != 2:
        return False
    # Extract the numerator and denominator.
    numerator, denominator = f
    # If the numerator is not an integer, return false.
    if isinstance(numerator,int) == False:
        return False
        # If the denominator is not an integer, return false.
    if isinstance(denominator,int) == False:
        return False
        # If the denominator is zero, return false.
    if denominator == 0:
        return False
    # Otherwise, it passed all tests and is a valid representation.
    return True


# -----------------------------------------------------------------------------
# Function: fractionToString
#
# Inputs:
#   f : a tuple representation of a fraction (numerator, denominator)
#
# Return Value:
#   a string representing the fraction. 
#
# Example Use:
#   fractionToString((1,2))
#     returns '1/2'
#
# Description:
#   Converts the tuple representation of a fraction to a string.
#   For instance, converts (1,2) to "1/2"
#
# Exceptions:
#   If the input is not a valid fraction, then a general Exception is raised
#     with the message: "Invalid fraction"
# -----------------------------------------------------------------------------
# TO-DO def fractionToString(f):
def fractionToString(f):
    #checks for if the function can work
    if isValidFraction(f):
        #gives back a string that represents a fraction
        return f"{f[0]}/{f[1]}"
    else:
        raise Exception("Invalid fraction")



# -----------------------------------------------------------------------------
# Function: fractionToDecimal
#
# Inputs:
#   f : a tuple representation of a fraction (numerator, denominator)
#
# Return Value:
#   a float representing the fraction. 
#
# Example Use:
#   fractionToDecimal((1,2))
#     returns 0.5
#
# Description:
#   Converts the tuple representation of a fraction to a float.
#   For instance, converts (1,2) to 0.5.
#
# Exceptions:
#   If the input is not a valid fraction, then a general Exception is raised
#     with the message: "Invalid fraction"
# -----------------------------------------------------------------------------
# TO-DO def fractionToDecimal(f):
def fractionToDecimal(f):
    #checks for if the function can work
    if isValidFraction(f):
        #gives back a decimal representation of fraction
        return f[0]/f[1]
    else:
        raise Exception("Invalid fraction")

# -----------------------------------------------------------------------------
# Function: reduceFraction
#
# Inputs:
#   f : a tuple representation of a fraction (numerator, denominator)
#
# Return Value:
#   a tuple representation of the reduced (lowest terms) fraction
#
# Example Use:
#   reduceFraction((6,8))
#     returns (3, 4)
#   reduceFraction((6,-8))
#     returns (-3, 4)
#   reduceFraction((-6,-8))
#     returns (3, 4)
#   reduceFraction((0,5))
#     returns (0, 1)
#
# Description:
#   Reduces a fraction to lowest terms by dividing numerator and denominator
#   by their greatest common divisor. If the numerator is 0, returns (0,1).
#
# Exceptions:
#   If the input is not a valid fraction, then a general Exception is raised
#     with the message: "Invalid fraction"
# -----------------------------------------------------------------------------
def reduceFraction(f):
    # If it is a valid tuple representation of a fraction, return the 
    # lowest terms representation.
    if isValidFraction(f):
        # Extract the numerator and denominator.
        numerator, denominator = f
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
        d = gcd(numerator, denominator)
        # Compute new (reduced) numerator and denominator.
        newNumerator = sign * numerator // d
        newDenominator = denominator // d
        return (newNumerator, newDenominator)
    # Otherwise, raise an Exception.
    else:
        raise Exception("Invalid fraction")


# -----------------------------------------------------------------------------
# Function: invertFraction
#
# Inputs:
#   f : a tuple representation of a fraction (numerator, denominator)
#
# Return Value:
#   a tuple representation of the inverted fraction
#
# Example Use:
#   invertFraction((1,2))
#     returns (2, 1)
#
# Description:
#   Inverts a fraction by flipping the numerator and denominator.
#
# Exceptions:
#   If the input is not a valid fraction, then a general Exception is raised
#     with the message: "Invalid fraction"
#   If the numerator is 0, then a general Exception is raised
#     with the message: "Divide by Zero"
# -----------------------------------------------------------------------------        
# TO-DO def invertFraction(f):
def invertFraction(f):
    #checks to see if the fraction is valid
    if isValidFraction(f):
        #checks to see if the numerator is 0
        if f[0]==0:
            raise Exception("Divide by Zero")
        else:
            #gives back an inverted tuple representation of a fraction
            return (f[1],f[0])
    else:
        raise Exception("Invalid fraction")



# -----------------------------------------------------------------------------
# Function: negateFraction
#
# Inputs:
#   f : a tuple representation of a fraction (numerator, denominator)
#
# Return Value:
#   a tuple representation of the negated fraction
#
# Example Use:
#   negateFraction((1,2))
#     returns (-1, 2)
#   negateFraction((-1,2))
#     returns (1, 2)
#
# Description:
#   Negates a fraction by flipping the sign of the fraction.
#   Ensures that if a negative result, only the numerator is negative.
#
# Exceptions:
#   If the input is not a valid fraction, then a general Exception is raised
#     with the message: "Invalid fraction"
# -----------------------------------------------------------------------------          
# TO-DO def negateFraction(f):
def negateFraction(f):
    #checks to see if the fraction is valid
    if isValidFraction(f):
        #checks for cases of positive functions
        if (f[0]<0 and f[1]<0) or (f[0]>0 and f[1]>0):
            #returns negative fraction
            return (-f[0],f[1])
        #checks for a negative denominator
        elif f[0]>0 and f[1]<0:
            #returns a positive fraction
            return (f[0],-f[1])
        #for a negative numerator
        else:
            #returns a positive fraction
            return (-f[0],f[1])
    else:
        raise Exception("Invalid fraction")


# -----------------------------------------------------------------------------
# Function: areFractionsEquivalent
#
# Inputs:
#   f : a tuple representation of a fraction (numerator, denominator)
#   g : a tuple representation of a fraction (numerator, denominator)
#
# Return Value:
#   a boolean indicating whether the fractions are equivalent
#
# Example Use:
#   areFractionsEquivalent((1,2),(3,6))
#     returns True
#   areFractionsEquivalent((1,2),(3,4))
#     returns False
#
# Description:
#   Determines if two fractions are equivalent. If the cross products are
#   equal, then the fractions are equivalent.
#
# Exceptions:
#   If either input is not a valid fraction, then a general Exception is raised
#     with the message: "Invalid fraction"
# -----------------------------------------------------------------------------          
# TO-DO def areFractionsEquivalent(f,g):
def areFractionsEquivalent(f,g):
    #checks to see if the fraction is valid
    if isValidFraction(f) and isValidFraction(g):
        #checks to see if the fractions equal each other
        if f[0]/f[1]==g[0]/g[1]:
            return True
        else:
            return False
    else:
        raise Exception("Invalid Fraction")


        

# -----------------------------------------------------------------------------
# Function: multiplyFractions
#
# Inputs:
#   f : a tuple representation of a fraction (numerator, denominator)
#   g : a tuple representation of a fraction (numerator, denominator)
#
# Return Value:
#   a tuple representation of the product of the fractions
#
# Example Use:
#   multiplyFractions((1,2),(2,3))
#     returns (1, 3)
#
# Description:
#   Multiplies two fractions and returns tuple representation in lowest terms
#   of the product. The product is found as the product of the numerators over
#   the product of the denominators. The product is then reduced to lowest 
#   terms.
#
# Exceptions:
#   If either input is not a valid fraction, then a general Exception is raised
#     with the message: "Invalid fraction"
# -----------------------------------------------------------------------------               
def multiplyFractions(f,g):
    # If the first input is not a valid representation of a fraction, raise an Exception.
    if isValidFraction(f) == False:
        raise Exception("Invalid fraction")
    # If the second input is not a valid representation of a fraction, raise an Exception.
    if isValidFraction(g) == False:
        raise Exception("Invalid fraction")
    # Extract the numerators and denominators.
    nf, df = f
    ng, dg = g
    # The product is the product of the numerators over the product of the denominators.
    # Reduce the result and return it.
    return reduceFraction((nf*ng, df*dg))
        

# -----------------------------------------------------------------------------
# Function: divideFractions
#
# Inputs:
#   f : a tuple representation of a fraction (numerator, denominator)
#   g : a tuple representation of a fraction (numerator, denominator)
#
# Return Value:
#   a tuple representation of the quotient of the fractions
#
# Example Use:
#   divideFractions((1,2),(1,4))
#     returns (2, 1)
#
# Description:
#   Divides two fractions and returns tuple representation in lowest terms
#   of the quotient. The quotient is found as the product of the first fraction
#   and the inverse of the second fraction.
#
# Exceptions:
#   If either input is not a valid fraction, then a general Exception is raised
#     with the message: "Invalid fraction"
#   If the second fraction is equivalent to zero, then a general Exception is
#     raised for division by zero.
# -----------------------------------------------------------------------------          
# TO-DO def divideFractions(f,g):
def divideFractions(f,g):
    #checks to see if the fractions are valid
    if isValidFraction(f) and isValidFraction(g):
        #checks to see if the second fraction doesn't equal 0
        if g[0]==0:
            raise Exception("Division by zero")
        else:
            #calls mutiply function with inverted second fraction to then return divided fraction
            newF = multiplyFractions(f,(g[1],g[0]))
            return reduceFraction(newF)
    else:
        raise Exception("Invalid Fraction")

# -----------------------------------------------------------------------------
# Function: addFractions
#
# Inputs:
#   f : a tuple representation of a fraction (numerator, denominator)
#   g : a tuple representation of a fraction (numerator, denominator)
#
# Return Value:
#   a tuple representation of the sum of the fractions
#
# Example Use:
#   addFractions((1,2),(1,4))
#     returns (3, 4)
#
# Description:
#   Adds two fractions and returns tuple representation in lowest terms
#   of the sum. 
#
# Exceptions:
#   If either input is not a valid fraction, then a general Exception is raised
#   with the message: "Invalid fraction"
# -----------------------------------------------------------------------------         
# TO-DO def addFractions(f,g):
def addFractions(f,g):
    #checks to see if fractions are valid
    if isValidFraction(f) and isValidFraction(g):
        #makes new numerators and denominators based on what the denominator would be if they were multiplied together, and returns reduced fraction
        newNum = (f[0]*g[1])+(g[0]*f[1])
        newDen = f[1]*g[1]
        return reduceFraction((newNum,newDen))
    else:
        raise Exception("Invalid Fraction")

# -----------------------------------------------------------------------------
# Function: subtractFractions
#
# Inputs:
#   f : a tuple representation of a fraction (numerator, denominator)
#   g : a tuple representation of a fraction (numerator, denominator)
#
# Return Value:
#   a tuple representation of the difference of the fractions
#
# Example Use:
#   subtractFractions((1,2),(1,3))
#     returns (1, 6)
#
# Description:
#   Subtracts two fractions and returns a tuple representation in lowest terms
#   of the difference. Finds the difference subtracting the negation of the 
#   second fraction from the first.
#
# Exceptions:
#   If either input is not a valid fraction, then a general Exception is raised
#   with the message: "Invalid fraction"
# -----------------------------------------------------------------------------           
# TO-DO def subtractFractions(f,g):
def subtractFractions(f,g):
    #checks to see if the fraction is valid
    if isValidFraction(f) and isValidFraction(g):
        #returns added fractions after negating one of them
        return addFractions(f,(-g[0],g[1]))
    else:
        raise Exception("Invalid Fraction")

        
