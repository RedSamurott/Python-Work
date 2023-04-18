numberList = []
listPrime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
for x in range(1,101):
    numberList.append(str(x))

for x in range(len(numberList)):
    length = len(numberList[x])
    prime = False
    extraChar = 0
    if int(numberList[x]) in listPrime:
        prime = True
    if int(numberList[x][:length]) % 5 == 0:
        numberList[x] += "Pikachu"
    if int(numberList[x][:length]) % 6 == 0:
        numberList[x] += ":rice_ball:"
    if int(numberList[x][:length]) % 7 == 0:
        extraChar = 2
        numberList[x] = f"**{numberList[x][:length]}**{numberList[x][length:]}"
    if "3" in numberList[x]:
        numberList[x] = f"{numberList[x][:extraChar]}*{numberList[x][extraChar:length+extraChar]}*{numberList[x][length+extraChar:]}"
    if prime == True:
        numberList[x] = f"TM{numberList[x]}"
    
for x in numberList:
    print(x)
