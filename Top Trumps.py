import random
import csv
import time

############################################################################################
#Cards class
class Cards():
    def __init__(self,setname,setprice,setRAM,setcs,setyear,setavailable,setsold):
        self.name=setname
        self.price=setprice
        self.RAM=setRAM
        self.clock_speed=setcs
        self.year=setyear
        self.available=setavailable
        self.sold=setsold

class Best(Cards):
    def __init__(self,setname,setprice,setRAM,setcs,setyear,setavailable,setsold):
        super(). __init__(setname,setprice,setRAM,setcs,setyear,setavailable,setsold)

    def change_price(self,setprice):
        self.price=setprice

    def change_RAM(self,setRAM):
        self.RAM=setRAM
        
    def change_cs(self,setcs):
        self.clock_speed=setcs
        
    def change_year(self,setyear):
        self.year=setyear

    def change_available(self,setavailable):
        self.available=setavailable

    def change_sold(self,setsold):
        self.sold=setsold

############################################################################################
#Player game functions
class Player():
    def __init__(self,setname,setturn):
        self.name=setname
        self.deck=[]
        self.turn=setturn

    def create_deck(self,deck,length):
        used_num=[]
        num=0
        for i in range(0,length-1):
            num=random.randint(0,length-2)
            while num in used_num:
                num=random.randint(0,length-2)
            used_num.append(num)
            self.deck.append(deck[num])

    def show_top(self):
        print(self.deck[0].name)
        print("1)Price.......................£"+str(self.deck[0].price))
        print("2)RAM........................."+str(self.deck[0].RAM)+"KB")
        print("3)Clock speed................."+str(self.deck[0].clock_speed)+"MHz")
        print("4)Release year................"+str(self.deck[0].year))
        print("5)Years available............."+str(self.deck[0].available))
        print("6)Units sold(millions)........"+str(self.deck[0].sold))

    def human_turn(self,player):
        print("\n"+"It is your turn.")
        stat=input("Enter the stat(number): ")
        num=["1","2","3","4","5","6"]
        while stat not in num:
            stat=input("Enter the stat(number): ")
        Game.compare(int(stat),player)

    def computer_turn1(self,player):
        print("\n"+"The computer is thinking...")
        time.sleep(1)
        stat=random.randint(1,6)
        Game.compare(stat,player)

    def computer_turn2(self,player):
        print("\n"+"The computer is thinking...")
        time.sleep(1)
        Game.change(player)
        if best_card.price==49.95:
            price=0
        else:
            price=(player.deck[0].price-49.95)/(best_card.price-49.95)
        if best_card.RAM==1:
            RAM=0
        else:
            RAM=(player.deck[0].RAM-1)/(best_card.RAM-1)
        if best_card.clock_speed==0.535:
            clock_speed=0
        else:
            clock_speed=(player.deck[0].clock_speed-0.535)/(best_card.clock_speed-0.535)
        if best_card.year==1977:
            year=0
        else:
            year=(player.deck[0].year-1977)/(best_card.year-1977)
        if best_card.available==2:
            available=0
        else:
            available=(player.deck[0].available-2)/(best_card.available-2)
        if best_card.sold==0.1:
            sold=0
        else:
            sold=(player.deck[0].sold-0.1)/(best_card.sold-0.1)
        values=[price,RAM,clock_speed,year,available,sold]
        stat=0
        for i in range(1,6):
            if values[stat]<values[i]:
                stat=i
        Game.compare(stat+1,player)
        
    def computer_turn3(self,player):
        print("\n"+"The computer is thinking...")
        time.sleep(1)
        price=(player.deck[0].price-49.95)/best_card.price
        RAM=(player.deck[0].RAM-1)/best_card.RAM
        clock_speed=(player.deck[0].clock_speed-0.535)/best_card.clock_speed
        year=(player.deck[0].year-1977)/best_card.year
        available=(player.deck[0].available-2)/best_card.available
        sold=(player.deck[0].sold-0.1)/best_card.sold
        values=[price,RAM,clock_speed,year,available,sold]
        stat=0
        for i in range(1,6):
            if values[stat]<values[i]:
                stat=i
        Game.compare(stat+1,player)

    def win(self,other):
        if self.name!="Computer":
            print("You won!"+"\n")
            print("You gained:")
            print(other.deck[0].name)
            print("1)Price.......................£"+str(other.deck[0].price))
            print("2)RAM........................."+str(other.deck[0].RAM)+"KB")
            print("3)Clock speed................."+str(other.deck[0].clock_speed)+"MHz")
            print("4)Release year................"+str(other.deck[0].year))
            print("5)Years available............."+str(other.deck[0].available))
            print("6)Units sold(millions)........"+str(other.deck[0].sold))
            print("\n")
            if Game.draw_deck!=[]:
                for i in Game.draw_deck:
                    self.deck.append(i)
                print("You also gained:")
                for i in range(0,len(Game.draw_deck)):
                    print(Game.draw_deck[i].name)
                    print("1)Price.......................£"+str(Game.draw_deck[i].price))
                    print("2)RAM........................."+str(Game.draw_deck[i].RAM)+"KB")
                    print("3)Clock speed................."+str(Game.draw_deck[i].clock_speed)+"MHz")
                    print("4)Release year................"+str(Game.draw_deck[i].year))
                    print("5)Years available............."+str(Game.draw_deck[i].available))
                    print("6)Units sold(millions)........"+str(Game.draw_deck[i].sold))
                    print("\n")
        else: 
            print("You lost."+"\n")
            if self.difficulty=="2":
                Game.change(self)
                Game.change(other)
            if Game.draw_deck!=[]:
                for i in Game.draw_deck:
                    self.deck.append(i)
        win_card=self.deck[0]
        lose_card=other.deck[0]
        del other.deck[0]
        del self.deck[0]
        self.deck.append(win_card)
        self.deck.append(lose_card)
        self.turn=True
        other.turn=False
        Game.empty()
        
    def lose(self,other):
        if self.name!="Computer":
            print("You lost."+"\n")
            if other.difficulty=="2":
                Game.change(self)
                Game.change(other)
            if Game.draw_deck!=[]:
                for i in Game.draw_deck:
                    other.deck.append(i)
        else:
            print("You won!"+"\n")
            print("You gained:")
            print(self.deck[0].name)
            print("1)Price.......................£"+str(self.deck[0].price))
            print("2)RAM........................."+str(self.deck[0].RAM)+"KB")
            print("3)Clock speed................."+str(self.deck[0].clock_speed)+"MHz")
            print("4)Release year................"+str(self.deck[0].year))
            print("5)Years available............."+str(self.deck[0].available))
            print("6)Units sold(millions)........"+str(self.deck[0].sold))
            print("\n")
            if Game.draw_deck!=[]:
                for i in Game.draw_deck:
                    other.deck.append(i)
                print("You also gained:")
                for i in range(0,len(Game.draw_deck)):
                    print(Game.draw_deck[i].name)
                    print("1)Price.......................£"+str(Game.draw_deck[i].price))
                    print("2)RAM........................."+str(Game.draw_deck[i].RAM)+"KB")
                    print("3)Clock speed................."+str(Game.draw_deck[i].clock_speed)+"MHz")
                    print("4)Release year................"+str(Game.draw_deck[i].year))
                    print("5)Years available............."+str(Game.draw_deck[i].available))
                    print("6)Units sold(millions)........"+str(Game.draw_deck[i].sold))
                    print("\n")
        win_card=other.deck[0]
        lose_card=self.deck[0]
        del other.deck[0]
        del self.deck[0]
        other.deck.append(win_card)
        other.deck.append(lose_card)
        self.turn=False
        other.turn=True
        Game.empty()

class Robot(Player):
    def __init__(self,setname,setturn,setdif):
        super().__init__(setname,setturn)
        self.difficulty=setdif

############################################################################################
#Main game functions
class Main():
    def __init__(self,setP1,setP2):
        self.P1=setP1
        self.P2=setP2
        self.draw_deck=[]

    def P_create(self,deck,length):
        self.P1.create_deck(deck,length)
        shuffled=self.P1.deck
        self.P1.deck=[]
        self.P1.deck=shuffled[:int((length-1)/2)]
        self.P2.deck=shuffled[int((length-1)/2):]

    def empty(self):
        self.draw_deck=[]
        
    def tie(self):
        print("You tied."+"\n")
        card1=self.P1.deck[0]
        card2=self.P2.deck[0]
        del self.P1.deck[0]
        del self.P2.deck[0]
        self.draw_deck.append(card1)
        self.draw_deck.append(card2)

    def show(self):
        if self.P1.name!="Computer":
            self.P1.show_top()
        else:
            self.P2.show_top()

    def player_turn(self,player):
        if player.name=="Computer":
            if player.difficulty=="1":
                player.computer_turn1(player)
            elif player.difficulty=="2":
                player.computer_turn2(player)
            else:
                player.computer_turn3(player)
        else:
            player.human_turn(player)

    def compare(self,stat,player):
        if player==P1:
            other=P2
        else:
            other=P1
        if stat==1:
            if player.name=="Computer":
                print("The computer chose price")
                print("Your value was",other.deck[0].price)
                print("The computer's value was",player.deck[0].price)
            else:
                print("Your value was",player.deck[0].price)
                print("The computer's value was",other.deck[0].price)                
            if player.deck[0].price>other.deck[0].price:
                player.win(other)
            elif player.deck[0].price==other.deck[0].price:
                Game.tie()
            else:
                player.lose(other)
        elif stat==2:
            if player.name=="Computer":
                print("The computer chose RAM")
                print("Your value was",other.deck[0].RAM)
                print("The computer's value was",player.deck[0].RAM)
            else:
                print("Your value was",player.deck[0].RAM)
                print("The computer's value was",other.deck[0].RAM) 
            if player.deck[0].RAM>other.deck[0].RAM:
                 player.win(other)
            elif player.deck[0].RAM==other.deck[0].RAM:
                Game.tie()
            else:
                player.lose(other)
        elif stat==3:
            if player.name=="Computer":
                print("The computer chose Clock speed")
                print("Your value was",other.deck[0].clock_speed)
                print("The computer's value was",player.deck[0].clock_speed)
            else:
                print("Your value was",player.deck[0].clock_speed)
                print("The computer's value was",other.deck[0].clock_speed) 
            if player.deck[0].clock_speed>other.deck[0].clock_speed:
                 player.win(other)
            elif player.deck[0].clock_speed==other.deck[0].clock_speed:
                Game.tie()
            else:
                player.lose(other)               
        elif stat==4:
            if player.name=="Computer":
                print("The computer chose Release year")
                print("Your value was",other.deck[0].year)
                print("The computer's value was",player.deck[0].year)
            else:
                print("Your value was",player.deck[0].year)
                print("The computer's value was",other.deck[0].year) 
            if player.deck[0].year>other.deck[0].year:
                 player.win(other)
            elif player.deck[0].year==other.deck[0].year:
                Game.tie()
            else:
                player.lose(other)
        elif stat==5:
            if player.name=="Computer":
                print("The computer chose Years available")
                print("Your value was",other.deck[0].available)
                print("The computer's value was",player.deck[0].available)
            else:
                print("Your value was",player.deck[0].available)
                print("The computer's value was",other.deck[0].available) 
            if player.deck[0].available>other.deck[0].available:
                 player.win(other)
            elif player.deck[0].available==other.deck[0].available:
                Game.tie()
            else:
                player.lose(other)
        elif stat==6:
            if player.name=="Computer":
                print("The computer chose Units sold(millions)")
                print("Your value was",other.deck[0].sold)
                print("The computer's value was",player.deck[0].sold)
            else:
                print("Your value was",player.deck[0].sold)
                print("The computer's value was",other.deck[0].sold) 
            if player.deck[0].sold>other.deck[0].sold:
                player.win(other)
            elif player.deck[0].sold==other.deck[0].sold:
                Game.tie()
            else:
                player.lose(other)

    def change(self,player):
        if player.deck[0].price>best_card.price:
            best_card.change_price(player.deck[0].price)
        if player.deck[0].RAM>best_card.RAM:
            best_card.change_RAM(player.deck[0].RAM)
        if player.deck[0].clock_speed>best_card.clock_speed:
            best_card.change_cs(player.deck[0].price)
        if player.deck[0].year>best_card.year:
            best_card.change_year(player.deck[0].year)
        if player.deck[0].available>best_card.available:
            best_card.change_available(player.deck[0].available)
        if player.deck[0].sold>best_card.sold:
            best_card.change_sold(player.deck[0].sold)
                
############################################################################################
#Initialise cards
card_file=open("computers.csv","r")
card_data=csv.reader(card_file)
deck=list(card_data)
card_file.close
del deck[0]
length=len(deck)
for i in range(0,length-1):
    deck[i]=Cards(deck[i][0],float(deck[i][1]),int(deck[i][2]),float(deck[i][3]),int(deck[i][4]),int(deck[i][5]),float(deck[i][6]))

############################################################################################
play=True
print("WELCOME TO TOP TRUMPS")
while play==True:
    print("Level 3 is the hardest")
    dif=input("Enter the difficulty (1-3): ")
    if dif=="2":
        best_card=Best("Best",0,0,0,0,0,0)
    elif dif=="3":
        best_card=Cards("Best",1995-49.95,512-1,7.83-0.535,1987-1977,16-2,17.5-0.1)
    num=random.randint(1,2)
    if num==1:
        P1=Player("Human",True)
        P2=Robot("Computer",False,dif)
        print("You are player 1"+"\n")
    else:
        P1=Robot("Computer",True,dif)
        P2=Player("Human",False)
        print("You are player 2"+"\n")
    Game=Main(P1,P2)
    Game.P_create(deck,length)
    rounds=True
    while rounds==True:
        if P1.name!="Computer":
            print("You have",len(P1.deck),"cards")
            print("The computer has",len(P2.deck),"cards")
        else:
            print("You have",len(P2.deck),"cards")
            print("The computer has",len(P1.deck),"cards")
        print("Your current card is:"+"\n")
        Game.show()
        if P1.turn==True:
            print("\n"+"It is player 1's turn"+"\n")
            Game.player_turn(P1)
        else:
            print("\n"+"It is player 2's turn"+"\n")
            Game.player_turn(P2)

        con=input("\n"+"Press enter to continue "+"\n")
        if len(P1.deck)==0 or len(P2.deck)==0:
            rounds=False
    if len(P1.deck)==0:
        if P1.name!="Computer":
            print("You lost Top Trumps")
        else:
            print("You won Top Trumps")
    else:
        if P2.name!="Computer":
            print("You lost Top Trumps")
        else:
            print("You won Top Trumps")
    again=input("Do you want to play again(Yes/No)? ")
    if again.lower()=="no":
        play=False
        
        
