import random

print ("welcome to the guessing game.".upper())
name = input("enter your name \n".upper())
guessnumber = int(random.randint(1,25))


def startgame():
    guesstake= 0
    chances = 6
    for i in range(1,7):
        
        
        print("remmeber, you have only {} chances left".format(chances).upper())
        inputnumber = int(input("{} please enter your guess from 1 to 25 here \n".format(name).upper()))
        guesstake += 1
        chances -= 1
        if inputnumber == guessnumber:
            print("congrats you won".upper())
            break
        elif inputnumber < guessnumber:
            print("oops the entered number is too low.".upper())
        elif inputnumber > guessnumber:
            print("oops the entered number is too high.".upper())
        if i == 6:
            print("sorry you couldn't win. \nThanks for playing ".upper())
    
    

    print("you have taken {} chances".format(guesstake).upper())   

        
startgame()


    
