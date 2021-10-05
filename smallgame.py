import os
import random

os.system('cls')


game = 1
welcome = 1
counter = 1
print("This is a random number guessing game, you have 10 tries to get the number right. I will give you hints if the number is higher or lower. Good luck!")

# answer = input("Do you want to play?")
# while('y' in answer):
#     print ("Hello! ")
print ("Welcome ")
answer = input("Do you want to play a game?")
while('y' in answer):
    welcome = 1
    
    randy= random.randint(1,100)
    while(welcome == 1 and counter != 11):
        counter +=1
       
        userInput=input("Guess the number ")

        try:
            userInput=int(userInput)
            check = True 
        except ValueError:
            check=False 

        if(check):

            if (randy==userInput):
                print("You win!!")
                welcome=0
  
            else:
                print("try again")
                game +=1
                if (randy<userInput):
                    print(" high")

                else:
                    (randy>userInput)
                    print("low")
            if (counter == 10):
                print ("You lost")
                welcome = 0

    if (welcome == 0):
        answer=input("Would you like to play again?")
        # answer!=input("Thank you")
        counter = 1

    else:
    
        welcome = 0

    


        



# if(randy- i >1):
#     print("too high, guess again")

# else:
#     (i - randy>1)
#     print("too high, guess again")
