# -----------------------------------------------------------------------------
# 
# File Name: TestExceptionalFractions.py
#
# Author: Donald Summers, major parts aurthored by Douglas Galarus
#
# Description:  A collection of tests to test the functions in ExceptionalFractions.py
#               This script is set up to call functions sequentially and test them,
#               including cases in which they throw exceptions. For normal cases that
#               do not throw excepts, a simple call is made to the given function.
#               For cases in which exceptions are expected, calls are wrapped in
#               try-except blocks so the exception does not halt execution of the 
#               script. The corresponding error message is printed.
#
# How to use:   python TestExceptionalFractions.py
#
# -----------------------------------------------------------------------------

import ExceptionalFractions as EF

#################################################################################
# Test the gcd() function in this section.
#################################################################################
print("-----------------------------------------------------------------------------")
print("Testing gcd():")
print()

# Typical case
print("Test: gcd(100,64) , Result should be: 4")
print(EF.gcd(100,64))
print()

# Try reversing the values
print("Test: gcd(64,100) , Result should be: 4")
print(EF.gcd(64,100))
print()

# Try relatively prime pair: gcf=1.
print("Test: gcd(49,64) , Result should be: 1")
print(EF.gcd(49,64))
print()

# Try passing zero as a value. Should result in an exception.
print("Test: gcd(0,100) , Result should be Exception, arguments not positive integers.")
try:
    print(EF.gcd(0,100))
except Exception as e:
    print(e)
print()

# Try passing negative number as a value. Should result in an exception.
print("Test: gcd(-100,64) , Result should be Exception, arguments not positive integers.")
try:
    print(EF.gcd(-100,64))
except Exception as e:
    print(e)
print()

# Try passing floats as values. Should result in an exception.
print("Test: gcd(100.0,64.0) , Result should be Exception, arguments not positive integers.")
try:
    print(EF.gcd(100.0,64.0))
except Exception as e:
    print(e)
print()
    

#################################################################################
# Test the makeFraction() function in this section.
#################################################################################

print("-----------------------------------------------------------------------------")

print("Testing makeFraction():")
print()

# Typical case
print("Test: makeFraction(1,2) , Result should be: (1, 2)")
print(EF.makeFraction(1,2))
print()

# Typical case
print("Test: makeFraction(2,1) , Result should be: (2, 1)")
print(EF.makeFraction(2,1))
print()

# Try zero denominator. Should result in an exception.
print("Test: makeFraction(2,0) , Result should be Exception, the denominator cannot be zero.")
try:
    print(EF.makeFraction(2,0))
except Exception as e:
    print(e)
print()

# Try floating point values. Should result in an exception.
print("Test: makeFraction(1.0, 2.0) , Result should be Exception, the numerator and denominator must be integers.")
try:
    print(EF.makeFraction(1.0, 2.0))
except Exception as e:
    print(e)
print()



#################################################################################
# Test the isValidFraction() function in this section.
#################################################################################
# TO-DO: WRITE TEST CODE FOR THIS FUNCTION
print("-----------------------------------------------------------------------------")

print("Testing isValidFraction():")
print()

# Typical case
print("Test: isValidFraction((1,2)) , Result should be: True ")
print(EF.isValidFraction((1,2)))
print()

# Typical case
print("Test: isValidFraction((2,1)) , Result should be: True ")
print(EF.isValidFraction((2,1)))
print()

# Try zero denominator. Should result in false.
print("Test: isValidFraction((2,0)) , Result should be: False")
print(EF.isValidFraction((2,0)))
print()

# Try floating point values. Should result in false.
print("Test: isValidFraction((1.0, 2.0)) , Result should be: False")
print(EF.isValidFraction((1.0, 2.0)))
print()

# Try list object. Should result in false.
print("Test: isValidFraction([1,2]) , Result should be: False")
print(EF.isValidFraction([1,2]))
print()

# Try more than two indexes in tuple. Should result in false.
print("Test: isValidFraction((1,2,3)) , Result should be: False")
print(EF.isValidFraction((1,2,3)))
print()


#################################################################################
# Test the fractionToString() function in this section.
#################################################################################
# TO-DO: WRITE TEST CODE FOR THIS FUNCTION
print("-----------------------------------------------------------------------------")

print("Testing fractionToString():")
print()

# Typical case
print("Test: fractionToString((1,2)) , Result should be: 1/2 ")
print(EF.fractionToString((1,2)))
print()

# Typical case
print("Test: fractionToString((2,1)) , Result should be: 2/1 ")
print(EF.fractionToString((2,1)))
print()

# Try faulty fraction. Should result in an exception.
print("Test: fractionToString((2,0)) , Result should be Exception, Invalid Fraction")
try:
    print(EF.fractionToString((2,0)))
except Exception as e:
    print(e)
print()


#################################################################################
# Test the fractionToDecimal() function in this section.
#################################################################################
# TO-DO: WRITE TEST CODE FOR THIS FUNCTION
print("-----------------------------------------------------------------------------")

print("Testing fractionToDecimal():")
print()

# Typical case
print("Test: fractionToDecimal((1,3)) , Result should be: 0.33333333333 ")
print(EF.fractionToDecimal((1,3)))
print()

# Typical case
print("Test: fractionToDecimal((2,4)) , Result should be: 0.5")
print(EF.fractionToDecimal((2,4)))
print()

# Try faulty fraction. Should result in an exception.
print("Test: fractionToDecimal((2,0)) , Result should be Exception, Invalid Fraction")
try:
    print(EF.fractionToDecimal((2,0)))
except Exception as e:
    print(e)
print()


#################################################################################
# Test the reduceFraction() function in this section.
#################################################################################
# TO-DO: WRITE TEST CODE FOR THIS FUNCTION
print("-----------------------------------------------------------------------------")

print("Testing reduceFraction():")
print()

# Typical case
print("Test: reduceFraction((6,9)) , Result should be: (2,3) ")
print(EF.reduceFraction((6,9)))
print()

# Typical case
print("Test: reduceFraction((2,4)) , Result should be: (1,2)")
print(EF.reduceFraction((2,4)))
print()

# Try faulty fraction. Should result in an exception.
print("Test: reduceFraction((2,0)) , Result should be Exception, Invalid Fraction")
try:
    print(EF.reduceFraction((2,0)))
except Exception as e:
    print(e)
print()



#################################################################################
# Test the invertFraction() function in this section.
#################################################################################
# TO-DO: WRITE TEST CODE FOR THIS FUNCTION
print("-----------------------------------------------------------------------------")

print("Testing invertFraction():")
print()

# Typical case
print("Test: invertFraction((6,9)) , Result should be: (9,6) ")
print(EF.invertFraction((6,9)))
print()

# Typical case
print("Test: invertFraction((2,4)) , Result should be: (4,2)")
print(EF.invertFraction((2,4)))
print()

# Try faulty fraction. Should result in an exception.
print("Test: invertFraction((2,0)) , Result should be Exception, Invalid Fraction")
try:
    print(EF.invertFraction((2,0)))
except Exception as e:
    print(e)
print()


# Try 0 in the numerator. Should result in an exception.
print("Test: invertFraction((0,2)) , Result should be Exception, Divide by Zero")
try:
    print(EF.invertFraction((0,2)))
except Exception as e:
    print(e)
print()


#################################################################################
# Test the negateFraction() function in this section.
#################################################################################
# TO-DO: WRITE TEST CODE FOR THIS FUNCTION
print("-----------------------------------------------------------------------------")

print("Testing negateFraction():")
print()

# Typical case
print("Test: negateFraction((6,9)) , Result should be: (-6,9) ")
print(EF.negateFraction((6,9)))
print()

# Typical case
print("Test: negateFraction((2,-4)) , Result should be: (2,4)")
print(EF.negateFraction((2,-4)))
print()

# Try faulty fraction. Should result in an exception.
print("Test: negateFraction((2,0)) , Result should be Exception, Invalid Fraction")
try:
    print(EF.negateFraction((2,0)))
except Exception as e:
    print(e)
print()


#################################################################################
# Test the areFractionsEquivalent() function in this section.
#################################################################################
# TO-DO: WRITE TEST CODE FOR THIS FUNCTION
print("-----------------------------------------------------------------------------")

print("Testing areFractionsEquivalent():")
print()

# Typical case
print("Test: areFractionsEquivalent((6,9),(2,3)) , Result should be: True ")
print(EF.areFractionsEquivalent((6,9),(2,3)))
print()

# Typical case
print("Test: areFractionsEquivalent((2,4),(1,3)) , Result should be: False ")
print(EF.areFractionsEquivalent((2,4),(1,3)))
print()

# Try faulty fraction. Should result in an exception.
print("Test: areFractionsEquivalent((2,0),(3,4)) , Result should be Exception, Invalid Fraction")
try:
    print(EF.areFractionsEquivalent((2,0),(3,4)))
except Exception as e:
    print(e)
print()


#################################################################################
# Test the multiplyFractions() function in this section.
#################################################################################
# TO-DO: WRITE TEST CODE FOR THIS FUNCTION
print("-----------------------------------------------------------------------------")

print("Testing multiplyFractions():")
print()

# Typical case
print("Test: multiplyFractions((6,9),(2,3)) , Result should be: (4,9) ")
print(EF.multiplyFractions((6,9),(2,3)))
print()

# Typical case
print("Test: multiplyFractions((2,4),(1,3)) , Result should be: (1,6) ")
print(EF.multiplyFractions((2,4),(1,3)))
print()

# Try faulty fraction. Should result in an exception.
print("Test: multiplyFractions((2,0),(3,4)) , Result should be Exception, Invalid Fraction")
try:
    print(EF.multiplyFractions((2,0),(3,4)))
except Exception as e:
    print(e)
print()


#################################################################################
# Test the divideFractions() function in this section.
#################################################################################
# TO-DO: WRITE TEST CODE FOR THIS FUNCTION
print("-----------------------------------------------------------------------------")

print("Testing divideFractions():")
print()

# Typical case
print("Test: divideFractions((6,9),(2,3)) , Result should be: (1,1) ")
print(EF.divideFractions((6,9),(2,3)))
print()

# Typical case
print("Test: divideFractions((2,4),(1,3)) , Result should be: (3,2) ")
print(EF.divideFractions((2,4),(1,3)))
print()

# Try faulty fraction. Should result in an exception.
print("Test: divideFractions((2,0),(3,4)) , Result should be Exception, Invalid Fraction")
try:
    print(EF.divideFractions((2,0),(3,4)))
except Exception as e:
    print(e)
print()

# Try dividing by zero. Should result in an exception.
print("Test: divideFractions((3,4),(0,2)) , Result should be Exception, Division by zero")
try:
    print(EF.divideFractions((3,4),(0,3)))
except Exception as e:
    print(e)
print()

#################################################################################
# Test the addFractions() function in this section.
#################################################################################
# TO-DO: WRITE TEST CODE FOR THIS FUNCTION
print("-----------------------------------------------------------------------------")

print("Testing addFractions():")
print()

# Typical case
print("Test: addFractions((6,9),(2,3)) , Result should be: (4,3) ")
print(EF.addFractions((6,9),(2,3)))
print()

# Typical case
print("Test: addFractions((2,4),(1,3)) , Result should be: (5,6) ")
print(EF.addFractions((2,4),(1,3)))
print()

# Try faulty fraction. Should result in an exception.
print("Test: addFractions((2,0),(3,4)) , Result should be Exception, Invalid Fraction")
try:
    print(EF.addFractions((2,0),(3,4)))
except Exception as e:
    print(e)
print()

#################################################################################
# Test the subtractFractions() function in this section.
#################################################################################
# TO-DO: WRITE TEST CODE FOR THIS FUNCTION
print("-----------------------------------------------------------------------------")

print("Testing subtractFractions():")
print()

# Typical case
print("Test: subtractFractions((6,9),(2,3)) , Result should be: (0,1) ")
print(EF.subtractFractions((6,9),(2,3)))
print()

# Typical case
print("Test: subtractFractions((2,4),(1,6)) , Result should be: (1,6) ")
print(EF.subtractFractions((2,4),(1,3)))
print()

# Try faulty fraction. Should result in an exception.
print("Test: subtractFractions((2,0),(3,4)) , Result should be Exception, Invalid Fraction")
try:
    print(EF.subtractFractions((2,0),(3,4)))
except Exception as e:
    print(e)
print()
