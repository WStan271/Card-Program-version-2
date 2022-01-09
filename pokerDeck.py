import random
class pokerCard:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    def toString(self):
        print("{} of {}".format(self.suit,self.rank))
    def getSuit(self):
        return self.suit
    def getRank(self):
        return self.rank
    def getCardValue(self):
        if self.getRank() == "Jack":
            return self.getRank()
        elif self.getRank() == "Queen":
            return self.getRank()
        elif self.getRank() == "King":
            return self.getRank()
        elif self.getRank() == "Ace":
            return self.getRank()
        else: 
            return self.getRank()
    def bjCardValue(self):
        if self.getRank() == "Jack":
            return 10
        elif self.getRank() == "Queen":
            return 10
        elif self.getRank() == "King":
            return 10
        elif self.getRank() == "Ace":
            return 11
        else: 
            return int(self.getRank())
    def speedCardValue(self):
        if self.getRank() == "Jack":
            return 11
        elif self.getRank() == "Queen":
            return 12
        elif self.getRank() == "King":
            return 13
        elif self.getRank() == "Ace":
            return 0
        else: 
            return int(self.getRank())
class deck:
    suits = ["Spades","Diamonds","Clubs","Hearts"]
    ranks = [2,3,4,5,6,7,8,9,10,"Jack","Queen","King","Ace"] 
    def __init__(self):
        self.pokerCards = []
        self.createDeck()
    def createDeck(self):
        for s in self.suits:
            for r in range(len(self.ranks)):
                self.pokerCards.append(pokerCard(s,self.ranks[r]))
    def toString(self):
        for c in self.pokerCards:
            c.toString()  
    def shuffle(self):
        """Shuffles the deck """
        for i in range(0,len(self.pokerCards),+1):
            r = random.randint(0,len(self.pokerCards)-1)
            self.pokerCards[i] , self.pokerCards[r] = self.pokerCards[r] , self.pokerCards[i]
    def draw(self):
        """ Gives the last card in the deck """
        return self.pokerCards.pop()
    def returnCard(self,pokerCard):
        """Add any card object to the end of a deck """
        self.pokerCards.append(pokerCard)
    

