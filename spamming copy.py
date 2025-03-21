import requests
import time
import json
import random

#time.sleep(60)

header = {
    'authorization': '' # header goes here
}

def retrieveMessages(channel):
    fullMessages=[]
    headers = {
        'authorization':"" # header goes here
    }
    r = requests.get(f'https://discord.com/api/v9/channels/{channel}/messages', headers=headers)
    jsonn = json.loads(r.text)
    for value in jsonn:
        fullMessages.append(value)
    return fullMessages

#a=retrieveMessages(1182801469003530352)
#print(a)
#a=retrieveMessages(channelList[x])
    #if a[0] == "***Are You Still Running?***":
    '''if x <=153:
        content = f"?{str(x)}153179224491615"
    elif 153 < x <=179:
        content = f"?153{str(x)}179224491615"
    elif 179 < x <=224:
        content = f"?153179{str(x)}224491615"
    elif 224 < x <=491:
        content = f"?153179224{str(x)}491615"
    elif 491 < x <=615:
        content = f"?153179224491{str(x)}615"
    elif 615 < x:
        content = f"?153179224491615{str(x)}"'''
#x = 324
channelList = 1298029708449157224
#alphabet = "abcdefghijklmnopqrstuvwxyz"
#possibleMessages = ["**[ A Gas Can has appeared in the chat! ]**", "**[ A -1 Gas Can has appeared in the chat! ]**", "**[ Two Gas Cans have appeared in the chat! ]**", "**[ A Gas Can has appeared in the chat! ]**", "**[ A Gas Can has appeared in the chat! ]**", "**[ A Gas Can has appeared in the chat! ]**", "**[ A Gas Can has appeared in the chat! ]**"]
message = ""
#possiblePlayer = ['abisnaily', 'pizzamaker888', 'tobinithy', 'ashertheone', 'posty_malone', 'musicneverdies']
x=0
a = retrieveMessages(638399801473499156)
print(a[1])
'''while True:
    #a = retrieveMessages(1317579845823369256)
    payload = {
        'content': f"{str(x)}"
    }
    z = requests.post(f'https://discord.com/api/v9/channels/{channelList}/messages', data=payload, headers=header)
    time.sleep(3)
    #time.sleep(2.1)'''

'''def commonLetters(inputString):
    string = str(inputString)
    letters = set(string)
    if " " in letters:         # If you want to count spaces too, ignore this if-statement
        letters.remove(" ")
    max_count = 0
    freq_letter = []
    for letter in letters:
        count = 0
        for char in string:
            if char == letter:
                count += 1
        if count == max_count:
            max_count = count
            freq_letter.append(letter)
        if count > max_count:
            max_count = count
            freq_letter.clear()
            freq_letter.append(letter)
    return freq_letter, max_count'''

#b = [x for x in a[0]]
#print(b)