#Zain Crumedy
#Arithmetic operators
# = - * / %-called mod

import os
os.system('cls')

# num= int(input("Give me a number"))
# rem=num%10
# #conditional
# if(rem ==0 ):
#     print(" The number is even")
# #when asking use == instead of = which is asigning 
# else:
#     print("The number is odd")

num = int(input("Give me a 2 digit number "))
rem=num%10
print
if(rem ==0 ):
    print (rem)
else:
    print (rem)

num = int(input("Give me a 3 digit number "))
rem=num%100
print
if(rem ==0 ):
    print (rem)
else:
    print (rem)

num = int(input("Give me a 4 digit number "))
rem=num%1000
print
if(rem ==0 ):
    print (rem)
else:
    print (rem)




a = int(input("enter first number "))
b = int(input("enter second number "))

sum = a + b
print(sum)

c = int(input("give me a big number "))
d = int(input("give me a smaller number "))

sum = c - d 
print(sum)

e = int(input("give me a number between 50 and 100 "))
f = int(input("give me a number between 100 and 150 "))

sum = e * f
print(sum)

g = int(input("give me a number between 50 and 100 "))
h = int(input("give me a number between 100 and 150 "))

sum = g / h
print(sum)
