#Zain Crumedy
#9/15/21

#we are going to learn how to use random numbers
#make a guess number game

import os
import random

os.system('cls')
random.seed(20)
#this loop was to play with random numbers
# for i in range(10):
#     randy = random.randint(3,5)
#     print(randy)
#     randy2= random.random()
#     randy2 *=100
#     print(int(randy2))

#arrays in python are called lists
fruits=["apple", "banana", "berries", "orange", "grape"]
myFruit= random.choice(fruits)
print(myFruit)
