import enum
from pokerDeck import deck,pokerCard

class player:
    def __init__(self,name):
        self.name = name
        self.hand = []
        self.score = [0,0,0]
    def addWin(self):
        self.score[0] += 1
    def addLoss(self):
        self.score[1] += 1
    def addTie(self):
        self.score[2] += 1
    def getName(self):
        return self.name
    def getScore(self):
        print("="*20)
        print("Player: {} \nWin count: {} \nLoss Count: {} \nTie Count: {}".format(self.name,self.score[0],self.score[1],self.score[2]))
    def playerDraw(self,pokerDeck):
        """Remove??"""
        """Add the card on top of the deck to player hand """
        self.hand.append(pokerDeck.draw())
    def showHand(self):
        for c in self.hand:
            c.toString()
    def bjScore(self):
        score = 0
        aces = 0
        for i in self.hand:
            score += i.bjCardValue()
            if i.bjCardValue() == "Ace":
                aces += 1
        while aces > 0 and score > 21:  
            score -= 10                
            aces -= 1
        return score        
    def pokerScore(self):
        score = 0
        for i in self.hand:
            score += i.bjCardValue()
        return score
class dealer(player):
    def __init__(self):
        self.name = "Dealer"
        self.hand = []
        self.score = [0,0,0]
    def deal(self,pokerDeck,playerHand):
        """Give a target player the top card from the deck """
        playerHand.append(pokerDeck.draw())
    def showHand(self):
        return self.hand[0].toString()   
class playerAction(enum.Enum):
    hit = 1
    stand = 2
class pickACardAction(enum.Enum):
    first  = 1
    second = 2
    third = 3
    fourth = 4
    fifth = 5

    
   


