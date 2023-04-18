import random

class Ship():
    'all ship based needs for battleship'
    ycoord=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    xcoord=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26']
    hold = []
    used = []
    def __init__(self,ori1,ori2,direction,hits,length,width):
        'ship base'
        self.ori1=ori1
        self.ori2=ori2
        self.direction=direction
        self.hits=hits
        self.length=length
        self.width=width
    
    def ship_position(self,ptype):
        'makes positions for ships'
        targets = []
        AItargets=[]
        playertargets=[]
        while str(self.ori1)+self.ori2 in self.used:
            self.ori1=random.randrange(1,self.length+1)
            self.ori2=random.randrange(0,self.width)
            for count in range(0,len(self.ycoord)):
                if self.ori2==count:
                    self.ori2=self.ycoord[count]
        if self.direction==0:
            if (self.ycoord.index(self.ori2)+1)-self.hits<0:
                self.ori2=self.ycoord.index(self.ori2)-(self.ycoord.index(self.ori2)+1-self.hits)
                for count in range(0,len(self.ycoord)):
                    if self.ori2==count:
                        self.ori2=self.ycoord[count]
            self.used.append(str(self.ori1)+self.ori2)
            targets.append(str(self.ori1)+self.ori2)
            for count in range(0,len(self.xcoord)+1):
                if count>self.length:
                    break
                if count==self.xcoord.index(str(self.ori1)):
                    for hp in range(1,self.hits):
                        if str(self.ori1)+str(self.ycoord[self.ycoord.index(self.ori2)-hp]) in self.used:
                            self.hold.append(str(self.ori1)+str(self.ycoord[self.ycoord.index(self.ori2)-hp]))
                        else:
                            targets.append(str(self.ori1)+str(self.ycoord[self.ycoord.index(self.ori2)-hp]))
                            self.used.append(str(self.ori1)+str(self.ycoord[self.ycoord.index(self.ori2)-hp]))
        
        if self.direction==1:
            if self.xcoord.index(str(self.ori1))+self.hits>self.length:
                self.ori1=self.ori1-(self.hits+self.xcoord.index(str(self.ori1))-self.length)
            self.used.append(str(self.ori1)+self.ori2)
            targets.append(str(self.ori1)+self.ori2)
            for count in range(0,len(self.ycoord)+1):
                if count>self.width:
                    break
                if count==self.ycoord.index(self.ori2):
                    for hp in range(1,self.hits):
                        if (self.xcoord[self.ori1+hp-1])+self.ori2 in self.used:
                            self.hold.append((self.xcoord[self.ori1+hp-1])+self.ori2)
                        else:
                            targets.append((self.xcoord[self.ori1+hp-1])+self.ori2)
                            self.used.append((self.xcoord[self.ori1+hp-1])+self.ori2)
        
        if self.direction==2:
            if self.ycoord.index(self.ori2)+self.hits>self.width:
                self.ori2=self.ycoord.index(self.ori2)-(self.ycoord.index(self.ori2)+self.hits-self.width)
                for count in range(0,len(self.ycoord)):
                    if self.ori2==count:
                        self.ori2=self.ycoord[count]
            self.used.append(str(self.ori1)+self.ori2)
            targets.append(str(self.ori1)+self.ori2)
            for count in range(0,len(self.xcoord)+1):
                if count>self.length:
                    break
                if count==self.xcoord.index(str(self.ori1)):
                    for hp in range(1,self.hits):
                        if str(self.ori1)+str(self.ycoord[self.ycoord.index(self.ori2)+hp]) in self.used:
                            self.hold.append(str(self.ori1)+str(self.ycoord[self.ycoord.index(self.ori2)+hp]))
                        else:
                            targets.append(str(self.ori1)+str(self.ycoord[self.ycoord.index(self.ori2)+hp]))
                            self.used.append(str(self.ori1)+str(self.ycoord[self.ycoord.index(self.ori2)+hp]))
        
        if self.direction==3:
            if self.xcoord.index(str(self.ori1))-self.hits<0:
                    self.ori1=self.ori1-(self.ori1-self.hits)
            self.used.append(str(self.ori1)+self.ori2)
            targets.append(str(self.ori1)+self.ori2)
            for count in range(0,len(self.ycoord)+1):
                if count>self.width:
                    break
                if count==self.ycoord.index(self.ori2):
                    for hp in range(1,self.hits):
                        if (self.xcoord[self.ori1-hp-1])+self.ori2 in self.used:
                            self.hold.append((self.xcoord[self.ori1-hp-1])+self.ori2)
                        else:
                            targets.append((self.xcoord[self.ori1-hp-1])+self.ori2)
                            self.used.append((self.xcoord[self.ori1-hp-1])+self.ori2)
        if ptype==0:
            AItargets.append(targets)
            return AItargets
        elif ptype==1:
            playertargets.append(targets)
            return playertargets

class Player():
    'all player/AI input here'
    pshots=[]
    aishots=[]
    previousshot = []
    ycoord=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    xcoord=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26']

    def __init__(self, length, width):
        'needed variables'
        self.length=length
        self.width=width
    
    def taken_AI(self):
        'returns AI shots'
        return self.aishots
    
    def taken_Player(self):
        'returns Player shots'
        return self.pshots
    
    def guess(self):
        'takes in the player guess'
        x=input('What is your x-coordinate(Number)?')
        while x not in self.xcoord:
            print('This coordinate is not within parameters')
            x=input('Reenter your x-coordinate(Number).')
        y=input('What is your y-coordinate(Letter)?')
        y=y.upper()
        while y not in self.ycoord:
                print('This coordinate is not within parameters')
                y=input('Reenter your y-coordinate(Letter).')
        while x+y in self.pshots:
            print('You have already taken this shot.')
            x=input('Reenter your x-coordinate(Number).')
            while x not in self.xcoord:
                print('This coordinate is not within parameters')
                x=input('Reenter your x-coordinate(Number).')
            y=input('Reenter your y-coordinate(Letter).')
            y=y.upper()
            while y not in self.ycoord:
                print('This coordinate is not within parameters')
                y=input('Reenter your y-coordinate(Letter).')
        self.pshots.append(x+y)
        return x+y

    def AI_normal(self):
        'AI taking a shot at random'
        x=random.randrange(1,self.length+1)
        y=random.randrange(0,self.width)
        for z in range(0,len(self.ycoord)):
            if y==z:
                y=self.ycoord[z]
        while str(x)+y in self.aishots:
            x=random.randrange(1,self.length+1)
            y=random.randrange(0,self.width)
            for z in range(0,len(self.ycoord)):
                if y==z:
                    y=self.ycoord[z]
        self.aishots.append(str(x)+y)
        if len(self.previousshot)>0:
            self.previousshot.pop(0)
            self.previousshot.append(str(x)+y)
        else:
            self.previousshot.append(str(x)+y)
        return str(x)+y
    
    def AI_hunt(self,preshot,hunt):
        'for when the AI gets a shot correct, they will choose a better target than random'
        shotsavail=[]
        shot = ''
        for count in range(0,self.length):
            for count1 in range(0,self.width):
                shotsavail.append(str(self.xcoord[count])+self.ycoord[count1])
        if hunt == '':
            hunt=random.randrange(0,4)
        if hunt==0:
            for count in range(0,len(shotsavail)-1):    
                if preshot==shotsavail[count]:
                    if preshot[1]<shotsavail[count-1][1]:
                        n=Player(self.length,self.width)
                        shot=n.AI_hunt(preshot,2)
                    else:
                        shot=shotsavail[count-1]
        if hunt==1:
            for count in range(0,len(shotsavail)-1):    
                if preshot==shotsavail[count]:
                    if preshot[0]==str(self.length):
                        n=Player(self.length,self.width)
                        shot=n.AI_hunt(preshot,3)
                    else:
                        shot=shotsavail[count+self.width]
        if hunt==2:
            for count in range(0,len(shotsavail)-1):    
                if preshot==shotsavail[count]:
                    if preshot[1]>shotsavail[count+1][1]:
                        n=Player(self.length,self.width)
                        shot=n.AI_hunt(preshot,0)
                    else:
                        shot=shotsavail[count+1]
        if hunt==3:
            for count in range(0,len(shotsavail)-1):    
                if preshot==shotsavail[count]:
                    if preshot[0]=='1':
                        n=Player(self.length,self.width)
                        shot=n.AI_hunt(preshot,1)
                    else: 
                        shot=shotsavail[count-self.width]
        if shot in self.aishots:
            n=Player(self.length,self.width)
            shot=n.AI_normal()
        return shot


class Game():
    'all basic needs for Battleship game'
    ycoord=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    xcoord=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26']
    pxshot=[]
    pyshot=[]
    aixshot=[]
    aiyshot=[]

    def board(self,length,width,shots,boats,ptype):
        'creates the visual board'
        if width>26 or length>26:
            return 'The board is too big, go back out to the code and make it smaller, between 25 by 25 and 5 by 5, please.'
        elif width<5 or length<5:
            return 'The board is too small, go back out to the code and make it bigger, between 25 by 25 and 5 by 5, please.'
        print('\033[0;36m ')
        t='_'*(length*3+1)
        r='0  '
        board=[]
        hold=[]
        holdrow=''
        if ptype==0:
            if len(self.pxshot)>0:
                for count in range(len(self.pxshot)):
                    self.pxshot.pop(0)
                    self.pyshot.pop(0)
            for count in range(len(shots)):
                if shots[count][1]=='A' or shots[count][1]=='B' or shots[count][1]=='C' or shots[count][1]=='D' or shots[count][1]=='E' or shots[count][1]=='F' or shots[count][1]=='G' or shots[count][1]=='H' or shots[count][1]=='I' or shots[count][1]=='J' or shots[count][1]=='K' or shots[count][1]=='L' or shots[count][1]=='M' or shots[count][1]=='N' or shots[count][1]=='O' or shots[count][1]=='P' or shots[count][1]=='Q' or shots[count][1]=='R' or shots[count][1]=='S' or shots[count][1]=='T' or shots[count][1]=='U' or shots[count][1]=='V' or shots[count][1]=='W' or shots[count][1]=='X' or shots[count][1]=='Y' or shots[count][1]=='Z':
                    self.pxshot.append(shots[count][0])
                    self.pyshot.append(shots[count][1])
                else:
                    self.pxshot.append(shots[count][0]+shots[count][1])
                    self.pyshot.append(shots[count][2])
            for x in range(length*width):
                for count in range(len(self.pxshot)-1):
                    if len(self.pxshot)==1:
                        break
                    else:
                        while int(self.pxshot[count])<int(self.pxshot[count+1]):
                            self.pxshot.append(self.pxshot[count])
                            self.pxshot.pop(count)
                            self.pyshot.append(self.pyshot[count])
                            self.pyshot.pop(count)
                    
                    
        if ptype==1:
            if len(self.aixshot)>0:
                for count in range(len(self.aixshot)):
                    self.aixshot.pop(0)
                    self.aiyshot.pop(0)
            for count in range(len(shots)):
                if shots[count][1]=='A' or shots[count][1]=='B' or shots[count][1]=='C' or shots[count][1]=='D' or shots[count][1]=='E' or shots[count][1]=='F' or shots[count][1]=='G' or shots[count][1]=='H' or shots[count][1]=='I' or shots[count][1]=='J' or shots[count][1]=='K' or shots[count][1]=='L' or shots[count][1]=='M' or shots[count][1]=='N' or shots[count][1]=='O' or shots[count][1]=='P' or shots[count][1]=='Q' or shots[count][1]=='R' or shots[count][1]=='S' or shots[count][1]=='T' or shots[count][1]=='U' or shots[count][1]=='V' or shots[count][1]=='W' or shots[count][1]=='X' or shots[count][1]=='Y' or shots[count][1]=='Z':
                    self.aixshot.append(shots[count][0])
                    self.aiyshot.append(shots[count][1])
                else:
                    self.aixshot.append(shots[count][0]+shots[count][1])
                    self.aiyshot.append(shots[count][2])
            for x in range(length*width):
                for count in range(len(self.aixshot)-1):
                    if len(self.aixshot)==1:
                        break
                    else:
                        while int(self.aixshot[count])<int(self.aixshot[count+1]):
                            self.aixshot.append(self.aixshot[count])
                            self.aixshot.pop(count)
                            self.aiyshot.append(self.aiyshot[count])
                            self.aiyshot.pop(count)
                
        print('  ', end='')
        for x in range(0,len(self.xcoord)-(26-length)):
            if x<9:
                print(self.xcoord[x]+'  ', end='')
            else:
                print(self.xcoord[x]+' ', end='')
        print()
        print(' '+t)

        for x in range(0,width):
            board.append(r*length)
        
        for x in range(0,width):
            if len(self.pxshot)==0:
                print(self.ycoord[x]+' '+board[x])
            elif len(self.pxshot)>0:
                if ptype==0:
                    for counter in range(len(self.pyshot)):
                        for counters in range(len(self.xcoord)):
                            if counters>length:
                                break
                            if self.ycoord[x]==self.pyshot[counter]:
                                if self.xcoord[counters]==self.pxshot[counter]:
                                    for z in range(0,len(board[x])):
                                        hold.append(board[x][z])
                                    for z in range(len(boats)):
                                        if self.pxshot[counter]+self.pyshot[counter]==boats[z]:
                                            hold[counters*3]='\033[0;31m0'+'\033[0;36m'
                                            break
                                        else:
                                            hold[counters*3]='\033[0;37m0'+'\033[0;36m'
                                    for ele in hold:
                                        holdrow+=ele
                                    board[x]=holdrow
                                    holdrow=''
                                    for m in range(len(hold)):
                                        hold.pop(0)
                                    break
                if ptype==1:
                    for counter in range(len(self.aiyshot)):
                        for counters in range(len(self.xcoord)):
                            if counters>length:
                                break
                            if self.ycoord[x]==self.aiyshot[counter]:
                                if self.xcoord[counters]==self.aixshot[counter]:
                                    for z in range(0,len(board[x])): 
                                        hold.append(board[x][z])
                                    for z in range(len(boats)):
                                        if self.aixshot[counter]+self.aiyshot[counter]==boats[z]:
                                            hold[counters*3]='\033[0;31m0'+'\033[0;36m'
                                            break
                                        else:
                                            hold[counters*3]='\033[0;37m0'+'\033[0;36m'
                                    for ele in hold:
                                        holdrow+=ele
                                    board[x]=holdrow
                                    holdrow=''
                                    for m in range(len(hold)):
                                        hold.pop(0)
                                    break
                print(self.ycoord[x]+' '+board[x])

    def create_ships(self,length,width,shipnumber,ptype):
        'creates the enemy ships on their board'
        total=[]
        targets=[]
        ori1=random.randrange(1,length+1)
        ori2=random.randrange(0,width)
        for count in range(0,len(self.ycoord)):
            if ori2==count:
                ori2=self.ycoord[count]
        direct=random.randrange(0,4)
        hits=random.randrange(2,6)
        total.append(hits)
        if sum(total)>length*width:
            return 'The total number of spaces occupied by ships is too much. Either lower the number of ships or increase the board size.'
        ships=Ship(ori1,ori2,direct,hits,length,width)
        if ptype==0:
            targets.append(ships.ship_position(0))
        elif ptype==1:
            targets.append(ships.ship_position(1))
        return targets
        

    def main(self):
        'main program and runs the game'
        a=10 #Replace number with a integer; this will affect the x-max of the board
        b=10 #Replace number a integer; this will affect the y-max of the board
        c=5 #Replace number with a integer; this will affect the number of ships
        #IF you don't want to replace '' with integers, go to every place a, b, or c is 
        #mentioned in thie method and put an integer in place of a, b, and c, and keep
        #it consistent.
        game=Game()
        player=Player(a,b)
        turn=0
        yourtargets=[]
        AItargets=[]
        change=0
        for x in range(0,c):
            yourtargets.append(game.create_ships(a,b,c,0))
        for x in range(0,c):
            AItargets.append(game.create_ships(a,b,c,1))
        placeholder=AItargets[0]
        placeholder=placeholder[0]
        AItargets=placeholder[0]
        placeholder=yourtargets[0]
        placeholder=placeholder[0]
        yourtargets=placeholder[0]
        endp=0
        endai=0
        while len(yourtargets)>0 or len(AItargets)>0:
            PlayerShots=player.taken_Player()
            AIShots=player.taken_AI()
            print('Your Shots/Enemy Board:')
            game.board(a,b,PlayerShots,yourtargets,0)
            print('Your Board:')
            game.board(a,b,AIShots,AItargets,1)
            player.guess()
            for count in range(0,len(AItargets)):
                if c == AItargets[count]:
                    change=1
            if change == 0:
                c=player.AI_normal()
            elif change == 1:
                c=player.AI_hunt(AIShots[-1],0)
            for x in range(len(PlayerShots)):
                for y in range(len(yourtargets)):
                    if PlayerShots[x]==yourtargets[y]:
                        endp+=1
            for x in range(len(AIShots)):
                for y in range(len(AItargets)):
                    if AIShots[x]==AItargets[y]:
                        endai+=1
            if endp>len(yourtargets):
                print('Player won.')
                break
            if endai>len(AItargets):
                print('AI won')
            
            turn+=1
            if turn>a*b:
                print("Somehow, the program didnt work when all the ships were destroyed, so now you are here. I'm sorry it didn't work for you.")
                break
            print('Turn:'+str(turn))

if __name__ == "__main__":
    Game().main()