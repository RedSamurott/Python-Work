######################
#
# Matrix.py
#
# Author: Donald Summers
#
# Description: Lab Assignment 6 Part 2, Matrix
#
# Creates a list of lists, or matrix, of 25 random calues from 0-150, inclusive and decimals allowed
#
# Example use: python Matrix.py
#
# Code sampled from Doug Galarus
######################
import random

#sets empty martix
matrix=[]

#creates messy matrix
for outsideCounter in range(5):
    row=[]
    for insideCounter in range(5):
        row.append(150*random.random())
    matrix.append(row)

#shows a completely empty martix
print("All Zeros:\n")
print("0 0 0 0 0\n"*5)

#shows the messy matrix
print("Messy Output:\n")
for outeritemCounter in range(len(matrix)):
    for inneritemCounter in range(len(matrix[outeritemCounter])):
        print(str(matrix[outeritemCounter][inneritemCounter])+" ",end="")
    print("\n")

#shows a clean version of the messy matrix
print("Clean Output:\n")
for outeritemCounter in range(len(matrix)):
    for inneritemCounter in range(len(matrix[outeritemCounter])):
        print(f"{matrix[outeritemCounter][inneritemCounter]:>8.2f}",end="")
    print("\n")