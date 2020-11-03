from random import *

class Card():
    def __init__(self,number):
        if int((number-1)/13)==0:
            self.shape="diamond"
            if (number-1)%13==0:
                self.number="A"
            elif (number-1)%13==1:
                self.number="2"
            elif (number-1)%13==2:
                self.number="3"
            elif (number-1)%13==3:
                self.number="4"
            elif (number-1)%13==4:
                self.number="5"
            elif (number-1)%13==5:
                self.number="6"
            elif (number-1)%13==6:
                self.number="7"
            elif (number-1)%13==7:
                self.number="8"
            elif (number-1)%13==8:
                self.number="9"
            elif (number-1)%13==9:
                self.number="10"
            elif (number-1)%13==10:
                self.number="J"
            elif (number-1)%13==11:
                self.number="Q"
            elif (number-1)%13==12:
                self.number="K"

        
        if int((number-1)/13)==1:
            self.shape="heart"
            if (number-1)%13==0:
                self.number="A"
            elif (number-1)%13==1:
                self.number="2"
            elif (number-1)%13==2:
                self.number="3"
            elif (number-1)%13==3:
                self.number="4"
            elif (number-1)%13==4:
                self.number="5"
            elif (number-1)%13==5:
                self.number="6"
            elif (number-1)%13==6:
                self.number="7"
            elif (number-1)%13==7:
                self.number="8"
            elif (number-1)%13==8:
                self.number="9"
            elif (number-1)%13==9:
                self.number="10"
            elif (number-1)%13==10:
                self.number="J"
            elif (number-1)%13==11:
                self.number="Q"
            elif (number-1)%13==12:
                self.number="K"
        
        if int((number-1)/13)==2:
            self.shape="spade"
            if (number-1)%13==0:
                self.number="A"
            elif (number-1)%13==1:
                self.number="2"
            elif (number-1)%13==2:
                self.number="3"
            elif (number-1)%13==3:
                self.number="4"
            elif (number-1)%13==4:
                self.number="5"
            elif (number-1)%13==5:
                self.number="6"
            elif (number-1)%13==6:
                self.number="7"
            elif (number-1)%13==7:
                self.number="8"
            elif (number-1)%13==8:
                self.number="9"
            elif (number-1)%13==9:
                self.number="10"
            elif (number-1)%13==10:
                self.number="J"
            elif (number-1)%13==11:
                self.number="Q"
            elif (number-1)%13==12:
                self.number="K"
        
        if int((number-1)/13)==3:
            self.shape="clova"
            if (number-1)%13==0:
                self.number="A"
            elif (number-1)%13==1:
                self.number="2"
            elif (number-1)%13==2:
                self.number="3"
            elif (number-1)%13==3:
                self.number="4"
            elif (number-1)%13==4:
                self.number="5"
            elif (number-1)%13==5:
                self.number="6"
            elif (number-1)%13==6:
                self.number="7"
            elif (number-1)%13==7:
                self.number="8"
            elif (number-1)%13==8:
                self.number="9"
            elif (number-1)%13==9:
                self.number="10"
            elif (number-1)%13==10:
                self.number="J"
            elif (number-1)%13==11:
                self.number="Q"
            elif (number-1)%13==12:
                self.number="K"

    def return_shape(self):
        print(self.shape,end="")

    def return_number(self):
        print(self.number)



class Deck():
    def __init__(self):
         self.deck=[]
    
    def deck_generation(self):

        tmp_list=[]
        tmp=0
        flag=0
        while len(tmp_list)<52 :
            tmp=randint(1,52)
            for i in range(len(tmp_list)):
                if tmp_list[i]==tmp:
                    flag=1
                    break

            
            if flag==1 :
                 flag=0
                 continue
            else :
                 tmp_list.append(tmp)

        for i in range(52):
            self.deck.append(Card(tmp_list[i]))
        



class Player():
   def __init__(self):
       self.HiddenCardList=[]
       self.OpenCardList=[]
       self.batting=0
   
   def AddOpenCardList(self, number):
       self.OpenCardList.append(number)
   
   def AddHiddenCardList(self,number):
       self.HiddenCardList.append(number)

   def AddingBattingMoney(self,number):
       print(number)
       self.batting=self.batting+number



#게임을 운영하는 주 클래스
#카드의 data representation은 1~52의 숫지로 한다.()
class Poker():
    def __init__(self, PlayerNumber):
        self.Deck=Deck()
        self.Deck.deck_generation()
        self.Playerlist=[]
        for i in range(PlayerNumber):
            self.Playerlist.append(Player())
        self.top=51

   

    def distribute_Card(self):
        for i in range(len(self.Playerlist)):
            
            self.Deck.deck[self.top].return_shape()
            self.Deck.deck[self.top].return_number()
            
            
            z=input()
            value=int(z)
            if(value==0) : 
                self.Playerlist[i].HiddenCardList.append(self.Deck.deck[self.top])
            else:
                self.Playerlist[i].OpenCardList.append(self.Deck.deck[self.top])
            self.top=self.top-1

    def BattingORDYing(self):
        dying=[]
        dyingconst=0
        for i in range(len(self.Playerlist)):
            print('배팅할것이가 죽을것인가.')
            z=input()
            value=int(z)

            if(value==0):
                dying.append(i)
            else:
                print('얼마를 배팅할 것인가')
                y=input()
                x=int(y)
                self.Playerlist[i].batting=self.Playerlist[i].batting+x


        for i in range(len(dying)):
            del self.Playerlist[dying[i]-i]
    

    def PlayingGame(self):
        
        for i in range(7):
            self.DistributingCard()
            self.BattingORDYing()


z=Poker(6)
z.PlayingGame()
