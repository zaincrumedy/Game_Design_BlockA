#Zain Crumedy
#9/12/21
import os

os.system('cls')
userInput=input("type something ")
print (userInput)
try:
    int(userInput)
    check=True
except ValueError:
    check=False


# print(check)
if (check):
    #i will be back
    print()
else:
    print(len(userInput))
for i in userInput:
    print(i)

if len(userInput>3):
    print(userInput[3])


# if(type(userInput)==int):
#     print("you gave me an integer")
# else:
#     print("Your input is not an integer")

#     intUser=int(userInput)
# print("This is the integer value of User input", intUser)
# this is about data type
# how strings work



