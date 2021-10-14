#Zain
#10/7/2021
# we are going to learn how to:
# open() a file
# write to a file 'w'
# reado from a file 'r'
# append to a file 'a'
# close() close a file

import os, time
os.system('cls')
#to create a file you must declare an object so we can ipen a file
#When you open a file you need to use 'w'
myFile = open('score.txt', 'w')
myFile.write("Hello there, my name is Maria \t what is yours?")
myFile.close()
#Always close a file when you are done using it
myFile = open('score.txt', 'w')
myFile.write("and now we will play a game")
myFile.close()
#read and print the file
fileMy=open('score.txt', 'r')
print(fileMy.read())
score=450
anotherFile=open('score.txx', 'a')
anotherFile.write("The highest Score: \t" + str(score))
