playerInput = input("Is their grump human? ") 
if playerInput == "Yes": #can be Bolivia, Defiant, Nicole, Reggie, Takeda, Kimishima, Blaze, Emp, Sugar, Twelve, Minegishi, Yabuki
    #if Andy thinks Martinet is a human grump, and you're stuck, come up here
    playerInput = input("Is their grump's hair a part of the monochromatic color scheme ")
    if playerInput == "Yes": # can be Bolivia, Defiant, Reggie, Kimishima, Emp, Yabuki
        playerInput = input("Does their name on the board have an E in it? ")
        if playerInput == "Yes": #Can be Reggie, Defiant, Emp
            playerInput = input("Is your person a player in SSS S32: Blazing Blade? ")
            if playerInput == "Yes": #Can be Defiant, Emp
                playerInput = input("Is your person Defiant? ")
                if playerInput == "Yes": #Can be Defiant
                    print("Done")
                else: #can be Emp
                    print("Is your person Emp? ")
            else: #can be Reggie
                print("Is your person Reggie? ") 
        else: #can be Bolivia, Kimishima, Yabuki
            playerInput = input("Is your person a player in SSS S32: Blazing Blade? ")
            if playerInput == "No": #Can be Kimishima, Yabkui
                playerInput = input("Is your person Kimishima? ")
                if playerInput == "Yes": #Can be Kimishima
                    print("Done")
                else: #can be Sugar
                    print("Is your person Yabuki? ")
            else: #can be Bolivia
                print("Is your person Bolivia? ") 
    else: #can be Nicole, Takeda, Blaze, Sugar, Twelve, Minegishi (Martinet if Andy thinks Martinet is human)
        playerInput = input("Does their name on the board have an A in it? ")
        if playerInput == "Yes": #can be Takeda, Blaze, Sugar (Martinet if Andy thinks Martinet is human)
            playerInput = input("Is your person a player in SSS S32: Blazing Blade? ")
            if playerInput == "Yes": #Can be Blaze, Sugar
                playerInput = input("Is your person Blaze? ")
                if playerInput == "Yes": #Can be Blaze
                    print("Done")
                else: #can be Sugar
                    print("Is your person Sugar? ")
            else: #can be Takeda (Martinet if Andy thinks Martinet is human)
                print("Is your person Takeda? ") 
        else: # can be Nicole, Twelve, Minegishi
            playerInput = input("Is your person a player in SSS S32: Blazing Blade? ")
            if playerInput == "Yes": #Can be Nicole, Twelve
                playerInput = input("Is your person Twelve? ")
                if playerInput == "Yes": #Can be Twelve
                    print("Done")
                else: #can be Nicole
                    print("Is your person Nicole? ")
            else: #can be Minegishi
                print("Is your person Mingishi? ")
else: #can be Andy, Seamus, Sun, Bill, Kentaro, Martinet, Dean, Lezaria, Monkey, Johnathan, Jonah, March, ShinGen, Beppu
    playerInput = input("Does their name on the board have an E in it? ")
    if playerInput == "Yes": #Can be Seamus, Kentaro, Martinet, Dean, Lezaria, Monkey, ShinGen, Beppu
        playerInput = input("Does their name on the board begin with a letter within the first 12 letter of the alphabet? ")
        if playerInput == "Yes": #Can be Kentaro, Dean, Lezaria, Beppu
            playerInput = input("Does their name on the board have a consonant as the second to last letter in it? ")
            if playerInput == "Yes": #Can be Kentaro, Beppu
                playerInput = input("Is your person Kentaro? ")
                if playerInput == "Yes": #Can be Kentaro
                    print("Done")
                else: #can be Beppu
                    print("Is your person Beppu? ")
            else: #can be Dean, Lezaria
                playerInput = input("Is your person Dean? ")
                if playerInput == "Yes": #can be Dean
                    print("Is your person Dean?")
                else: #can be Lezaria
                    print("Is your person Lezaria?")
        else: #can be Seamus, Martinet, Monkey, ShinGen
            playerInput = input("Does their name on the board have start with a S? ")
            if playerInput == "Yes": #can be Seamus, ShinGen
                playerInput = input("Is your person ShinGen")
                if playerInput == "Yes": #can be ShinGen
                    print("Done")
                else: #can be Seamus
                    print("Is your person Seamus? ")
            else: #can be Monkey, Martinet
                playerInput = input("Is your person Monkey? ")
                if playerInput == "Yes": #can be Monkey
                    print("Is your person Monkey? ")
                else: #can be Martinet
                    print("Is your person Martinet? ")
    else: # can be Andy, Sun, Bill, Big Dog, Johnathan, Jonah, March
        playerInput = input("Does their name on the board have an A in it? ")
        if playerInput == "Yes": #can be Andy, Johnathan, Jonah, March
            playerInput = input("Did your person get eliminated in the first two tribals of SSS S32? ")
            if playerInput == "Yes": #can be Johnathan, Jonah
                playerInput = input("Is your person Johnathan? ")
                if playerInput == "Yes": #can be Johnathan
                    print("Done")
                else: #can be Jonah
                    print("Is your person Jonah? ")
            else: #can be Andy, March
                playerInput = input("Is your person Andy? ")
                if playerInput == "Yes": #can be Andy
                    print("Done")
                else: #can be March
                    print("Is your person March? ")
        else: # can be Sun, Bill, Big Dog
            playerInput = input("Does their name on the board begin with a B? ")
            if playerInput == "Yes": # can be Bill, Big Dog
                playerInput = input("Is your person Big Dog? ")
                if playerInput == "Yes":
                    print("Done")
                else:
                    print("Is your person Bill? ")
            else: # can be Sun
                print("Is your person Sun?")
