import requests
import json

def retrieveMessages(channelID):
    fullMessages=[]
    headers = {
        'authorization':"MjgxOTgwOTU2NTA2NTg3MTM4.GWHhhB.E56LFpMTKxItM7xaNFARUzLWjffNQ71VV4mU5c"
    }
    r = requests.get(f'https://discord.com/api/v9/channels/{channelID}/messages', headers=headers)
    jsonn = json.loads(r.text)
    for value in jsonn:
        fullMessages.append(value['content'])
    return fullMessages

playerCount=12

alivePlayers = [1,2,3,4,5,6,7,8,9,10,11,12]
while playerCount>2:
    playerRequests = []
    messagelist = []
    count = 0
    if 1 in alivePlayers:
        player1 = retrieveMessages('1066546108236574812')
        messagelist.append(player1)
    if 2 in alivePlayers:
        player2 = retrieveMessages('1066545971883954256')
        messagelist.append(player2)
    if 3 in alivePlayers:
        player3 = retrieveMessages('1066545832687566999')
        messagelist.append(player3)
    if 4 in alivePlayers:
        player4 = retrieveMessages('1066545571487305748')
        messagelist.append(player4)
    if 5 in alivePlayers:
        player5 = retrieveMessages('1066545475198668890')
        messagelist.append(player5)
    if 6 in alivePlayers:
        player6 = retrieveMessages('1066545372538876014')
        messagelist.append(player6)
    if 7 in alivePlayers:
        player7 = retrieveMessages('1066545275277160478')
        messagelist.append(player7)
    if 8 in alivePlayers:
        player8 = retrieveMessages('1066544947349696582')
        messagelist.append(player8)
    if 9 in alivePlayers:
        player9 = retrieveMessages('1066544572806733868')
        messagelist.append(player9)
    if 10 in alivePlayers:
        player10 = retrieveMessages('1066544119167598743')
        messagelist.append(player10)
    if 11 in alivePlayers:
        player11 = retrieveMessages('1066543648466030592')
        messagelist.append(player11)
    if 12 in alivePlayers:
        player12 = retrieveMessages('1066543471067926568')
        messagelist.append(player12)
    for playerCounting in range(0,len(messagelist)):
        recount = 1
        for values in range(0,len(messagelist[playerCounting])):
            if "/faction" in messagelist[playerCounting][values]:
                if recount == 1:
                    playerRequests.append(f"{alivePlayers[playerCounting]}: {messagelist[playerCounting][values]}")
                recount += 1
    for x in range(0,len(playerRequests)):
        playerRequests[x] = list(playerRequests[x].split(' '))
        #playerRequests[x].sort()
    factionNumber = len(playerRequests[0][2:])
    #print(playerRequests)

    indiviualFaction = []
    for x in range(0,playerCount):
        indiviualFaction.append(0)

    for x in range(0,len(playerRequests)):
        checking = (playerRequests[x][2:])
        #checking.sort()
        #print(checking)
        for y in range(0,len(checking)):
            lenCount=1
            if len(playerRequests[x][0])>2:
                lenCount=2
            if int(checking[y]) != int(playerRequests[x][0][:lenCount]):
                for z in playerRequests:
                    if str(int(checking[y])) in z[0]:
                        if len(str(int(checking[y])))==2:
                            jersey = []
                            jersey.append(checking[y]+":")
                            jersey.append("/faction")
                            for a in range(0,len(checking)):
                                jersey.append(checking[a])
                            if jersey in playerRequests:
                                index = playerRequests.index(jersey)
                        else:
                            jersey = []
                            jersey.append(checking[y][1:]+":")
                            jersey.append("/faction")
                            for a in range(0,len(checking)):
                                jersey.append(checking[a])
                            if jersey in playerRequests:
                                index = playerRequests.index(jersey)
                if checking == playerRequests[index][2:]:
                    indiviualFaction[x] += 1
    
    saidFactions = []
    
    for x in range(0, len(indiviualFaction)):
        saidIndividualFactions = []
        fullFaction = ""
        if indiviualFaction[x] == factionNumber - 1:
            fullFaction += (str(x+1)+" - ")
            for y in range(2,len(playerRequests[x])):
                fullFaction += (str(playerRequests[x][y])+" ")
                saidIndividualFactions.append(playerRequests[x][y])
            if saidIndividualFactions not in saidFactions:
                print("There was...")
                print("a faction created!")
                print(fullFaction)
                saidFactions.append(saidIndividualFactions)
            #lenCount=1
            #if len(playerRequests[x][0])>2:
                #lenCount = 2
            #print(f"Player {playerRequests[x][0][:lenCount]} was able to get into a faction with: ")
            #for y in range(0, len(playerRequests[x])):
                #if playerRequests[x][y][1] == "/" or playerRequests[x][y][1] == "f" or playerRequests[x][y][1] == ":" or playerRequests[x][y][1] == "a":
                    #pass
                #make seperate ones depending on the len size of playerRequests[x][y]
                #elif int(playerRequests[x][y][:2]) != (x + 1):
                    #if len(playerRequests[x][y])==2:
                        #print(f"Player {playerRequests[x][y]}")
        else:
            print(f"Player {playerRequests[x][0][:lenCount]} did not make a valid faction.")

    elim = input("Which player eliminated? ")
    if int(elim) in alivePlayers:
        alivePlayers.remove(int(elim))
    playerCount = playerCount - 1
    holdUp = input("Ready to continue? ")
    