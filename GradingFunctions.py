######################
#
# GradingFunctions.py
#
# Author: Donald Summers
#
# Description: Lab Assignment 9, Grading Functions
#
# Makes some functions that are used for grading
#
# Example use: python GradingFunctions.py
#
######################

#establishes grade ranges and letter grades
cutoffs = [100, 93, 90, 87, 83, 80, 77, 73, 70, 67, 63, 60, 0] 
letterGrades = ['A','A-','B+','B','B-','C+','C','C-','D+','D','D-','F']

def printGradingScale():
######################
#
# printGradingScale()
# 
# No arguements
#
# Returns nothing
#
# Prints out the grading scale in a easy to read format
#
# Example use: printGradingScale()
#
######################
    #starts formatted output
    print("Percent Range Letter Grade")
    print("------------- ------------")
    print("   93 to 100% A")
    #goes through the list and formats them to the output
    for x in range(1,len(letterGrades)-1):
        print("  ",str(cutoffs[x+1]),"to <"+str(cutoffs[x])+"%",letterGrades[x])
    print("    Below 60% F")

def getGradeByScore(score):
######################
#
# getGradeByScore(score)
# 
# score: takes in a decimal value from 0 to 1, inclusive, representing a grade
#
# Returns a string of the letter score
#
# Takes in a decimal point that represents a score, and returns out the letter grade associated with it
#
# Example use: letterGrade = getGradeByScore(.9)
#              print(letterGrade)
#              "A-"
######################
    #makes an empty string to hold grade later
    grade=""
    #goes through list to see where it matches
    for x in range(len(cutoffs)-1):
        if cutoffs[x+1] <= int(score*100) < cutoffs[x]:
            grade=letterGrades[x]
    return grade


def getGradeByScores(scores):
######################
#
# getGradeByScores(scores)
# 
# scores: takes in a list of decimal value from 0 to 1, inclusive, representing grades
#
# Returns a string of the letter score
#
# Takes in a list of decimal point that represents a score,averages them, and returns out the letter grade associated with it
#
# Example use: letterGrade = getGradeByScores([.95,.8,.85])
#              print(letterGrade)
#              "B"
######################
    #makes a 0 interger veriable to add scores to later
    overallScore=0
    #goes through score list and adds to overallScore
    for x in range(len(scores)):
        overallScore += scores[x]
    #gets average score
    overallScore = overallScore/len(scores)
    return getGradeByScore(overallScore)

def getGradeByPoints(pointsEarned, pointsPossible):
######################
#
# getGradeByPoints(pointsEarned, pointsPossible)
# 
# pointsEarned: takes in a list of non-negative integers that represent how many points were earned
#
# pointsPossible: takes in a list of non-negative integers that represent how many points total could have been earned
#
# Returns a string of the letter score
#
# Takes in two lists that repsent points earned and points total respectively, calculates the scores, avergaes them, and then
# returns a letter grade
#
# Example use: letterGrade = getGradeByPoints([8,9,15],[10,10,20])
#              print(letterGrade)
#              "B-"
######################
    #makes a 0 interger veriable to add scores to later
    overallScore=0
    #goes through points lists, makes a score, and adds to overall score
    for x in range(len(pointsEarned)):
        overallScore += pointsEarned[x]/pointsPossible[x]
    #gets average score
    overallScore = overallScore/len(pointsEarned)
    return getGradeByScore(overallScore)

def getGradeRange(strGrade):
######################
#
# getGradeRange(strGrade)
# 
# strGrade: takes in a string representing a letter grade
#
# Returns a tuple representing the range of scores for the requesting letter grade
#
# Takes in a string that represents a letter grade, and returns a tuple that represents the range of scores for the requested
# letter grade
#
# Example use: tupleScoreRange = getGradeRange("B+")
#              print(tupleScoreRange)
#              (87,90)
######################
    #looks through list to get the range of values for grade in a tuple
    for x in range(len(letterGrades)):
        if strGrade == letterGrades[x]:
            gradeTuple=(cutoffs[x+1],cutoffs[x])
    return gradeTuple