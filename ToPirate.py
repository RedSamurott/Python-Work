######################
#
# ToPirate.py
#
# Author: Donald Summers
#
# Description: Lab Assignment 8, ToPirate translator
#
# Translate simple english words into Pirate using dictionary
#
# Example use: python ToPirate.py
#
######################

#Establishes the dictionary of English to Pirate
pirateTranslator={"hello":"avast","excuse":"arrr","sir":"matey","boy":"matey","man":"matey","madam":"proud beauty",
                  "officer":"foul blaggart","the":"th'","my":"me","your":"yer","is":"be","are":"be","restroom":"head",
                  "restaurant":"galley","hotel":"fleabag inn"}

#Starts the program with instructions and an introduction
print("Welcome to the English to Pirate translation service!\n")
print("When prompted, please enter a sentence in English and it will be translated")
print("to Pirate. Beware: the pirate translator’s vocabulary is limited, so try not")
print("to upset the pirate translator by using fancy words.")

#Establishes a forever loop to continually ask for a new English sentence
while True:
    #sets up two kinds of sentence, an empty one for the pirate translation, and the input for English
    pirateSentence=""
    englishSentence=input("Please enter an English sentence:\n")
    
    #breaks out of the loop and moves towards the end of the program
    if "quit" in englishSentence.lower():
        break

    #takes the input and makes it a list to then compare against the keys of the English-To-Pirate dictionary and change list
    #to have the pirate translation
    englishSentence=englishSentence.split(" ")
    for wordCount in range(len(englishSentence)):
        for translateKeys in pirateTranslator:
            englishSentence[wordCount]=englishSentence[wordCount].lower()
            if englishSentence[wordCount] == translateKeys:
                englishSentence[wordCount]=pirateTranslator[translateKeys]

    #capatilizes the first word in the sentence
    englishSentence[0]=englishSentence[0].capitalize()

    #puts all the words in the list into the empty string from ealrier to print out later
    for englishWordcount in englishSentence:
        pirateSentence+=englishWordcount+" "

    #prints out the translation
    print("Pirate Translation:")
    print(pirateSentence)

#exiting message
print("Thank ye, matey. Ahoy!")