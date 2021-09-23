import os
import random

os.system('cls')

for i in range(100):
    randy= random.randint(1,100)
    #print(randy)

print("This is a random number guessing game, you have 10 tries to get the number right. I will give you hints if the number is higher or lower. Good luck!")


for i in range(1,11):
    userInput=input("Guess the number ")
    try:
        userInput=int(userInput)
        check = True 
    except ValueError:
        check=False 

    if (randy==userInput):
        print("You win!!")
        
    else:
        print("try again")

    if (randy<userInput):
        print("too high")

    else:
        (randy>userInput)
        print("too low")
        

# if(randy- i >1):
#     print("too high, guess again")

# else:
#     (i - randy>1)
#     print("too high, guess again")
