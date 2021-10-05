#Zain
#9/29

import random,os
os.system('cls')
panimals=["Panda", "Panther", "Parrot", "Peacock", "Penguin", "Pangolin", "Pelican"]
word = random.choices(panimals)
guesses=''
for letters in word:
        if letters in guesses:
            print(letters, end= " ")
        else:
            print('_', end= ' ')

panimals=["Panda", "Panther", "Parrot", "Peacock", "Penguin", "Pangolin", "Pelican"]

print("This is a word game, you have to guess every letter of the word. Your only hint is that the word is an animal and that it starts with the letter p.")
print("You have 10 tries")
name = input("What is your name ")
counter = 0
answer = input(name + ", Do you want to play? ")
while 'y' in answer:
    print(name, " Good luck:)")
    chances = 10
    counter +=1
    word = random.choices(panimals)
    print(word)
    guesses=''
    while chances > 0 :
        newguess=input(name+ "Give me a letter")
        if newguess in word:
            guesses += newguess
            print("you guessed one letter ")
        else:
            chances-=1
            print("sorry, you have", chances, "left")

        for letter in word:
            if letter in guesses:
                print(letter,end= " ")
            else:
                print('_', end =" ")




  
    







