# Zain Crumedy
# 09/07/21
#  We are going to learn how to use a loop

 star=int(input("How many stars? "))
 line=star
 stars2 = star
 space=0
 for I in range (line):
     for counter in range (star):
         print("*", end=" ")
         star-=1
     for J in range (space):
         print(" ", end= " ")    
         space += 2
         #star+=1 is adding the 
     #add loop for spaces
     for counter in range(stars2): #you can use a number or a variable
         print("*", end=" ")
         #print(counter+1, end=" ")
     print() #print a return creating a new line
     stars2 +=1 #shortcut for star=star-1
 print("Thank you")
