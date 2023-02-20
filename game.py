import random

RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()


class Deck:
    def __init__(self, deck, emdeck, fhalf, shalf):
        # deck(RANKS), emdeck(empty deck where will shuffeled cards), fhalf/shalf(1,2 half)
        self.deck = deck
        self.emdeck = emdeck
        self.fhalf = fhalf
        self.shalf = shalf
    def randeck(self):
        # add all 52 cards in one deck
        self.emdeck.extend(self.deck*4)
        # random deck
        random.shuffle(self.emdeck)
        return self.emdeck
    def halfo(self):
        # slice deck on the half 
        self.fhalf.extend(self.emdeck[slice(26)])
        return self.fhalf
    def halft(self):
        # slice deck on the other half 
        self.shalf.extend(self.emdeck[slice(26,52)])
        return self.shalf
    
class Hand:
    def __init__(self,p1,p2,cards):
        self.p1 = p1
        self.p2 = p2
        self.cards = cards

    #cards del and adding to end of array
    def addpl1(self):
        self.p1.extend(self.p1[:self.cards+1])
        self.p1.extend(self.p2[:self.cards+1])
        del self.p1[:self.cards+1]
        del self.p2[:self.cards+1]
        self.cards -= self.cards 

        return self.p1
    def addpl2(self):
        self.p2.extend(self.p2[:self.cards+1])
        self.p2.extend(self.p1[:self.cards+1])
        del self.p2[:self.cards+1]
        del self.p1[:self.cards+1]
        self.cards -= self.cards 

        return self.p2
    
class Player:
    def __init__(self,nick1,nick2):
        self.nick1 = nick1
        self.nick2 = nick2
    def cardcheck1(self):
        pass
    def cardcheck2(self):
        pass

print("Welcome to War, let's begin...")

cards1 = []
player = []
player0 = []
crd = 0
p1_wins = 0
p2_wins = 0
war = 0
rounds = 0

cards = Deck(RANKS, cards1, player,player0)
print("Full deck: ", cards.randeck())
checker = Hand(cards.halfo(),cards.halft(),crd)
player1 = cards.fhalf
player2 = cards.shalf
print("1PL: ", player1)
print("2PL: ", player2, "\n")
# loops until one of player have cards
while len(player1) > 0 and len(player2) > 0:
    rounds +=1
    crd -= crd
    index1 = RANKS.index(player1[crd])
    index2 = RANKS.index(player2[crd])
    if index1 > index2:
        player1 = checker.addpl1()
        print("Player1: ",player1)
        print("Player2: ",player2, "\n")
    elif index2 > index1:
        player2 = checker.addpl2()
        print("Player1: ", player1)
        print("Player2: ", player2, "\n")
    elif index1 == index2:
        # loop until players have a same cards on desk
        while index1 == index2:
            war+=1
            crd += 1
            # stop the loop if one of players have a last card and that card a same as in other player
            if crd >= len(player1):
                print("Player2 won!")
                print("War was ",war," times")
                print("Total rounds", rounds+1)
                quit()
            elif crd >= len(player2):
                print("Player1 won!")
                print("War was ",war," times")
                print("Total rounds", rounds+1)
                quit()
            else:
                checker =  Hand(player1,player2,crd)
                index1 = RANKS.index(player1[crd])
                index2 = RANKS.index(player2[crd])
                if index1 > index2:
                    player1 = checker.addpl1()
                    print("Player1: ", player1)
                    print("Player2: ", player2, "\n")
                    crd -= crd
                elif index2 > index1:
                    player2 = checker.addpl2()
                    print("Player1: ", player1)
                    print("Player2: ", player2, "\n")
                    crd -= crd
if len(player1) == 0:
    print("Player2 won!")
    print("War was ",war," times")
    print("Total rounds", rounds+1)
    quit()
else:
    print("Player1 won!")
    print("War was ",war," times")
    print("Total rounds", rounds+1)
    quit()
    
