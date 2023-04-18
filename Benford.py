# -----------------------------------------------------------------------------
# 
# File Name: Bedford.py
#
# Author: Donald Summers
#
# Description:  Takes data from a system argument and calculates the distribution
#				according to the Benford law
#
# How to use:   Either import the file into another python file as "import Benford
#				as Benford" or run it in the command line with 2 system arguments,
#				one that takes a number n that represents the nth digit of numbers
#				in a data set provided in the second system argument
#
# Example use:  python Beford.py 0 TestData.txt
#
# -----------------------------------------------------------------------------
import sys


# ----------------------------------------------------------------------------
#
# Benford class - implements functionality for testing the Benford law
#
# ----------------------------------------------------------------------------
class Benford:

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
    #   a = Bendford()
    #
    # Description:
    #   Initializes the class for use through the main function or in other programs
    # -----------------------------------------------------------------------------
    def __init__(self):
        pass

    # -----------------------------------------------------------------------------
    # Instance Method: countDigits
    #
    # Inputs:
    #   num: an integer
    #
    # Return Value:
    #   an integer of how many digits are in the integer 
    #
    # Example Use:
    #
    #   a = Benford()
    #   a.countDigits(123)
    #
    #     returns '3'
    #
    # Description:
    #   Returns the number of digits in the number num.
    # -----------------------------------------------------------------------------
    def countDigits(self, num):
        return len(str(num))

    # -----------------------------------------------------------------------------
    # Instance Method: nthDigitBack
    #
    # Inputs:
    #   n, num: integers
    #
    # Return Value:
    #   an integer of the nth digit back in an integer
    #
    # Example Use:
    #
    #   a = Benford()
    #   a.nthDigitBack(1, 123)
    #
    #     returns '2'
    #
    # Description:
    #   Returns the digit at the nth position from the right
    #   in the number num.
    # -----------------------------------------------------------------------------
    def nthDigitBack(self, n, num):
        if -n-1<-len(str(num)):
            return -1
        else:
            return int(str(num)[-n-1])

    # -----------------------------------------------------------------------------
    # Instance Method: nthDigit
    #
    # Inputs:
    #   n, num: integers
    #
    # Return Value:
    #   an integer of the nth digit in an integer
    #
    # Example Use:
    #
    #   a = Benford()
    #   a.nthDigit(1, 123)
    #
    #     returns '2'
    #
    # Description:
    #   Returns the digit at the nth position from the left
    #   in the number num.
    # -----------------------------------------------------------------------------
    def nthDigit(self, n, num):
        if n>=len(str(num)):
            return -1
        else:
            numberLength = self.countDigits(num)
            return self.nthDigitBack(numberLength-n-1, num)

    # -----------------------------------------------------------------------------
    # Instance Method: nthDigitTally1
    #
    # Inputs:
    #   n, num: integers
    #   tally: a list
    #
    # Return Value:
    #   a list that composes the freuqency/distirbution of numbers in an integer
    #
    # Example Use:
    #
    #   a = Benford()
    #   a.nthDigitTally1(1, 123, [0,0,0,0,0,0,0,0,0,0])
    #
    #     returns '[0,0,1,0,0,0,0,0,0,0]'
    #
    # Description:
    #   Updates and returns the tally list with a new count
    #   based on the corresponding digit n in the number num.
    # -----------------------------------------------------------------------------
    def nthDigitTally1(self, n, num, tally):
        numberToIncrement = self.nthDigit(n, num)
        tally[int(numberToIncrement)] += 1
        return tally

    # -----------------------------------------------------------------------------
    # Instance Method: nthDigitTally
    #
    # Inputs:
    #   n, num: integers
    #
    # Return Value:
    #   a list that composes the freuqency/distirbution of numbers in an integer
    #
    # Example Use:
    #
    #   a = Benford()
    #   a.nthDigitTally(1, 123)
    #
    #     returns '[0,0,1,0,0,0,0,0,0,0]'
    #
    # Description:
    #   Returns a tally list of all digits in the nth position.
    # -----------------------------------------------------------------------------
    def nthDigitTally(self, n, nums):
        newTally = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for x in nums:
            newTally = self.nthDigitTally1(n, x, newTally)
        return newTally
    
    # -----------------------------------------------------------------------------
    # Instance Method: readMysteriousNumbers
    #
    # Inputs:
    #   fName: a string that reprsents a file name
    #
    # Return Value:
    #   a list that has all the actual data values from a file
    #
    # Example Use:
    #
    #   a = Benford()
    #   a.readMysteriousNumbers("TestData.txt")
    #
    #     returns '[12176, 5476, 543, 3490, 24892, 28619, 2595, 603, 2527, 1465, 1858]
    #
    # Description:
    #   Opens a file and reads all the numbers into a list.
    #   Assumes the first number is the count of subsequent numbers
    #   in the file and does not include that number in the list.
    # -----------------------------------------------------------------------------
    def readMysteriousNumbers(self, fName):
        fName = open(fName,'rt')
        dataList = []
        while True:
            line = fName.readlines()
            if not line:
                break
            dataList += line
        fName.close()
        for x in range(0,len(dataList)):
            dataList[x] = dataList[x].strip()
        return dataList[1:]
        
# -----------------------------------------------------------------------------
# Function: main
#
# Inputs:
#   none
#
# Return Value:
#   none
#
# Example Use:
#   if __name__ == "__main__":
#       main()
#
# Description:
#   Takes the Benford class and has it run through a file with data in it to 
#   calculate the distribution of numbers in it and prints it out in a nice format
# -----------------------------------------------------------------------------    
def main():
    data = Benford()
    dataList = data.readMysteriousNumbers(sys.argv[2])
    distribution= data.nthDigitTally(int(sys.argv[1]),dataList)
    for x in range(0,len(distribution)):
        print(f"{x}s: {distribution[x]}")

if __name__ == "__main__":
    main()
    
