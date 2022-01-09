from abc import ABC, abstractmethod
from pokerDeck import deck,pokerCard
from player import player,dealer,playerAction
from modules.player import pickACardAction

class game(ABC):
    def __init__(self):
        pass
    @abstractmethod
    def setUpGame(self):
        pass
    @abstractmethod
    def startGame(self):
        pass
    def playerAction(self):
        pass
    @abstractmethod
    def endGame(self):
        pass
class blackJack(game):
    def __init__(self):
        #self.playerCount = int((input("Number of players?")))
        self.bjDealer = dealer()
        self.playerCount = 2
        self.players = []
        self.playerScores = []
        self.dealerScore = 0
        self.bjDeck = deck()
        self.isGameActive = True
        #set up player names and their score
        for i in range(self.playerCount):
            self.players.append(player(input("\nEnter username:\n")))
            self.playerScores.append(0)
        self.setUpGame()
        self.startGame()
    # overriding abstract method
    def setUpGame(self):
        self.bjDeck.shuffle()  
        #deal two cards to dealer
        self.bjDealer.deal(self.bjDeck,self.bjDealer.hand)
        self.bjDealer.deal(self.bjDeck,self.bjDealer.hand)
        print("\n{}'s hand:".format(self.bjDealer.getName()))
        self.bjDealer.showHand()
        print("One facedown card")
        for i in range(self.playerCount):
            #deal two cards to each player
            self.bjDealer.deal(self.bjDeck,self.players[i].hand)
            self.bjDealer.deal(self.bjDeck,self.players[i].hand)
            print("\n{}'s hand:".format(self.players[i].getName()))
            self.players[i].showHand()
    # overriding abstract method
    def startGame(self):
        while self.isGameActive == True:
            for i in range(self.playerCount):
                print("\nYour turn {}".format(self.players[i].getName()))
                playerMove = int(input("\nHit(1) or Stand(2) \n"))
                if  playerMove == playerAction.hit.value:
                    print("You choose hit\n")
                    self.bjDealer.deal(self.bjDeck,self.players[i].hand)
                    self.players[i].showHand()
                    self.playerScores[i] = self.players[i].bjScore()
                    print("\n{}'s score:{}".format(self.players[i].getName(),self.playerScores[i]))
                    if self.playerScores[i]>21:
                        print("\n{} has busted".format(self.players[i].getName()))
                        self.players[i].addLoss()
                elif playerMove == playerAction.stand.value:
                    print("\n{} is standing".format(self.players[i].getName()))
                    #If dealer score is 16 or under they must draw another card         
            print("All players are done")
            print("Dealers flips hidden card:")
            self.bjDealer.showHand() 
            self.dealerScore = self.bjDealer.bjScore()
            if self.dealerScore <= 16: 
                print("Dealer score is under 17 and must draw\n")
                self.bjDealer.deal(self.bjDeck,self.bjDealer.hand)
                print("Dealer hand is now:")   
                self.bjDealer.showHand()
                self.dealerScore = self.bjDealer.bjScore() 
                print("\nDealer's final score:{}".format(self.dealerScore)) 
            
            for i in range(self.playerCount):
                self.playerScores[i] = self.players[i].bjScore()
                if self.playerScores[i] == self.dealerScore:
                    self.players[i].addTie()
                    self.bjDealer.addTie()
                    print("\n{} has tied with the dealer".format(self.players[i].getName()))
                elif self.dealerScore>21:
                    self.bjDealer.addLoss()
                    print("\Dealer has busted")
                elif self.playerScores > self.dealerScore:
                    self.players[i].addWin()
                    print("\n{} wins".format(self.players[i].getName()))
                elif self.playerScores < self.dealerScore:
                    self.bjDealer.addWin()
                    print("\nDealer wins")
                print("Final Player Scores:\n")  
                print("\n{}'s score:{}".format(self.players[i].getName(),self.playerScores[i]))
        self.endGame()
    # overriding abstract method
    def endGame(self):
        print("\nThank you for playing")
        self.isGameActive = False
class poker(game):
    def __init__(self):
        self.playerCount = 2
        self.players = []
        self.playerScores = []
        self.pokerDealer = dealer()
        self.studPokerDeck = deck()
        self.isGameActive = True
        self.setUpGame()
        self.startGame()
        
        for i in range(self.playerCount):
            self.players.append(player(input("\nEnter username:\n")))
            self.playerScores.append(0)
    # overriding abstract method
    def setUpGame(self):
        self.studPokerDeck.shuffle() 
        for i in range(self.playerCount):
            #deal five cards to each player
            for c in range(5):
                self.pokerDealer.deal(self.studPokerDeck,self.players[i].hand)
                self.player.hand
    # overriding abstract method
    def startGame(self):
        while self.isGameActive == True:
               
            
    # overriding abstract method
    def endGame(self):
        print("\nThank you for playing")
        self.isGameActive = False
    def sort(self):
        pass
    def checkHand(self):
        pass
    def isRoyalFlush(self):  
        pass
    def isStraightFlush(self):  
        pass
    def isFourKind(self):
        pass
    def isFullHouse(self):
        pass
    def isFlush(self):
        pass
    def isStraight(self):
        pass
    def isThreeKind(self):
        pass
    def isTwoPair(self):
        self.isPair()
        pass
    def isPair(self):
        pass
    def highCard(self):
        pass
class speed(game):
    def __init__(self):
        self.playerCount = 2
        self.players = []
        self.speedDealer = dealer()
        self.playerScores = []
        self.speedDeck = deck()
        self.setUpGame()
        self.startGame()
        
        for i in range(self.playerCount):
            self.players.append(player(input("\nEnter username:\n")))
            self.playerScores.append(0)
    # overriding abstract method
    def setUpGame(self):
        self.speedDeck.shuffle() 
        self.bjDealer.deal(self.speedDeck,self.bjDealer.hand)
        for i in range(self.playerCount):
            #deal ten cards to each player
            for c in range(10):
                self.speedDealer.deal(self.speedDeck,self.players[i].hand)
                
    # overriding abstract method
    def startGame(self):
        while self.isGameActive == True:
            for i in range(self.playerCount):
                print("\nYour turn {}".format(self.players[i].getName()))        
                self.players[i].showHand()
                playerMove = int(input("\nPick a card from your hand 1-5 \n"))
                if  playerMove == pickACardAction.first.value:
                    self.hand[0].returnCard(self.speedDealer.hand())
                    ValidMove()
                elif  playerMove == pickACardAction.second.value:   
                    self.hand[1].returnCard(self.speedDealer.hand())
                    ValidMove()
                elif  playerMove == pickACardAction.third.value:   
                    self.hand[2].returnCard(self.speedDealer.hand())
                    ValidMove()
                elif  playerMove == pickACardAction.fourth.value:   
                    self.hand[3].returnCard(self.speedDealer.hand())
                    ValidMove()
                elif  playerMove == pickACardAction.fifth.value:   
                    self.hand[4].returnCard(self.speedDealer.hand())
                    ValidMove()
                else:
                    print("Not a valid action")
                    continue
                if(len(self.player.hand) == 0):
                    print("Player:{} is first to get 0 cards in hand they win".format(self.players[i].getName()))
                    self.player.addWin()
                    self.isGameActive = False
    # overriding abstract method
    def endGame(self):
        print("\nThank you for playing")
        self.isGameActive = False
    def ValidMove(self):
       temp = len(self.speedDeck)
       if (self.speedDeck[temp-2] - self.speedDeck[temp-1]) != 1 or -1 or 13 or -13:
           print("Not a valid move")
           print("You take an extra card from the deck")
           self.player.pickUpCard()
       else:
           print("ValidMove")
    def pickUpCard(self):
        self.speedDealer.deal(self.speedDeck,self.player.hand)

