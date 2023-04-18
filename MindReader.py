# -----------------------------------------------------------------------------
# 
# File Name: MindReader.py
#
# Author: Donald Summers
#
# Description:  A little game where a player tries to outsmart a computer trying
#               to guess what the player will put in next using a OOP approach
#               and a dictionary to store the player's previous guesses that the
#               computer uses to predict what the player's next guess is.
#
# How to use:   Run the main file in the terminal/prompt or import the file over
#
# Example use:  python MindReader.py
#
# -----------------------------------------------------------------------------
import random

# ----------------------------------------------------------------------------
#
# mindReader class - impliments functionality for the Mind Reader game, including
#                    containing the dictionary that the computer uses to guess,
#                    player input, and computer guessing
#
# ----------------------------------------------------------------------------
class mindReader():

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
    #   a = mindReader()
    #
    # Description:
    #   Initializes the class for use in the Mind Reader game
    # -----------------------------------------------------------------------------
    def __init__(self):
        self.mindReaderDict = {}
        self.previousFourGuesses = []
        self.currentFourGuesses = ""
    
    # -----------------------------------------------------------------------------
    # Method: playerInput
    #
    # Inputs:
    #   self : reference to the object
    #
    # Return Value:
    #   a string of the player's input in uppercase(to not cause problems)
    #
    # Example Use:
    #   a = mindReader()
    #   a.playerInput()
    #
    # Description:
    #   gets the player's input, and makes sure it is an "H" or "T"
    # -----------------------------------------------------------------------------
    def playerInput(self):
        validGuesses = ("H","T")
        playerGuess = input("Please enter H for heads or T for tails: ").upper()
        while playerGuess not in validGuesses:
            print("Please put in 'H' or 'T' please.")
            playerGuess = input("Please enter H for heads or T for tails: ").upper()
        return playerGuess

    # -----------------------------------------------------------------------------
    # Method: addToDict
    #
    # Inputs:
    #   self: reference to the object
    #   guess: the player's guess
    #
    # Return Value:
    #   addToDict does not return a value
    #
    # Example Use:
    #   a = mindReader()
    #   playerGuess = a.playerInput()
    #   a.addToDict(playerGuess)
    #
    # Description:
    #   adds the previous 4 guess as a key in the dictionary as long as 4 guesses
    #   have been made, and assigns a list value that will be used for the computer
    #   to guess what the player will pick next
    # -----------------------------------------------------------------------------
    def addToDict(self,guess):
        self.previousFourGuesses.append(guess)
        if len(self.previousFourGuesses) != 4:
            pass
        else:
            self.currentFourGuesses = "".join(self.previousFourGuesses)
            if self.currentFourGuesses in self.mindReaderDict:
                pass
            else:
                self.mindReaderDict[self.currentFourGuesses] = [0,0]
            self.previousFourGuesses.pop(0)

    # -----------------------------------------------------------------------------
    # Method: computerGuess
    #
    # Inputs:
    #   self : reference to the object
    #
    # Return Value:
    #   computerGuess does not return a value
    #
    # Example Use:
    #   a = mindReader()
    #   a.computerGuess()
    #
    # Description:
    #   takes the dictionary made throughout the game to guess what the player will
    #   pick next based on the previous 4 guesses. As long as the previous 4 guesses
    #   is in the dictionary, it will look in the dictionary and look at the list
    #   and whichever is higher(Index 0 for "H", Index 1 for "T") will pick that.
    #   If no key values pair exists, it randomly chooses.
    # -----------------------------------------------------------------------------
    def computerGuess(self):
        if self.currentFourGuesses == "":
            choice = random.choice(["H","T"])
            return choice
        else:
            if self.mindReaderDict[self.currentFourGuesses][0] > self.mindReaderDict[self.currentFourGuesses][1]:
                return "H"
            elif self.mindReaderDict[self.currentFourGuesses][1] > self.mindReaderDict[self.currentFourGuesses][0]:
                return "T"
            else:
                choice = random.choice(["H","T"])
                return choice
    
    # -----------------------------------------------------------------------------
    # Method: updateDictionary
    #
    # Inputs:
    #   self: reference to the object
    #   guess: a player's guess
    #
    # Return Value:
    #   updateDictionary does not return a value
    #
    # Example Use:
    #   a = mindReader()
    #   playerGuess = a.playerInput()
    #   a.updateDictionary(playerGuess)
    #
    # Description:
    #   takes the player's input and updates the value according to the previous 4
    #   guesses as a key as long as the key exists
    # -----------------------------------------------------------------------------
    def updateDictionary(self, guess):
        if self.currentFourGuesses == "":
            pass
        else:
            if guess == "H":
                self.mindReaderDict[self.currentFourGuesses][0] += 1
            elif guess == "T":
                self.mindReaderDict[self.currentFourGuesses][1] += 1

#if the program is called in the terminal/prompt, it will run this code        
if __name__ == "__main__":  
    #intializes the class and two important variables for keeping score
    a = mindReader()
    scorePlayer = 0
    scoreComputer = 0
    #prints the instructions and goal of the game
    print("         MIND READER GAME          ")
    print("-----------------------------------")
    print(" Welcome to the Mind Reader Game!  ")
    print("You are trying your best to outplay")
    print("the computer's predictions of your ")
    print("guesses. You are guessing based off")
    print("the Heads(H) or Tails(T) of a coin.")
    print("If the computer guesses your guess,")
    print("the computer scores. If your guess ")
    print(" is different than the computer's, ")
    print(" then you get a point. First to 25 ")
    print("               wins                ")
    print("-----------------------------------")
    print("            GOOD LUCK              ")
    #while loop to keep the game running until the target score is reached
    while scoreComputer<25 and scorePlayer<25:
        print("Your Turn.")
        #takes player input and gets the computer's guess as to what the player inputted
        playerGuess = a.playerInput()
        computerGuess = a.computerGuess()

        #updates the dictionary to make sure the guesses from the computer can accurately out manuever what a player puts in
        a.updateDictionary(playerGuess)
        a.addToDict(playerGuess)
        
        #shows what each participant put in and adds to the score accordingly
        print(f"The computer predicted {computerGuess} and the player chose {playerGuess}. ")
        if playerGuess==computerGuess:
            print("One point for the computer!")
            scoreComputer += 1
        else:
            print("One points for the player!")
            scorePlayer += 1
        
        #prints the score out
        print(f"Computer: {scoreComputer} , Player: {scorePlayer}")
        print(" ")
    #depending on which side wins, displays a message congratulating the winner
    if scorePlayer == 25:
        print("Player WINS!!!")
    elif scoreComputer == 25:
        print("Computer WINS!!!")