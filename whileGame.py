#leaning while loop

#control the main game
#instructions of the game
answer = input("Do you want to play a game?")
while('y' in answer):
    print ("Welcome ")
    num = input("Give me a number")
    #try and except
    while (num>10):
        print(num)
        num +=5
    print ("this is your number ", num) 
    num = input("Give me a number")