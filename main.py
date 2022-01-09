from game import blackJack,poker,speed
def main():
    playCardGame = True
    while playCardGame != False:
        guestChoice = int(input("Welcome to my tavern what do you wish to do? \n1:Play BlackJack \n2:Play Poker \n3:Play Speed \n4:Leave\n"))
        if guestChoice == 1:
            newGame = blackJack()
        elif guestChoice == 2:
            newGame = poker()
        elif guestChoice == 3:
            newGame = speed()
        elif guestChoice == 4:
            print("Thank you for visiting")
            playCardGame = False
        else:
            print("Not a valid response")
  
  
# Using the special variable 
# __name__
if __name__=="__main__":
    main()