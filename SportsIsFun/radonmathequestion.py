import random
import math
a=True
while a==True:
    operation1 = random.randint(1, 4)
    n1 = random.randint(1, 10)
    n2 = random.randint(1, 10)
    if operation1 == '4' and n2 == 0:
        n2 = random.randint(1, 10)
    
    
    if operation1==1:
        answer=n1+n2
        operation="+"
    elif operation1==2:
        answer=n1-n2
        operation="-"
    elif operation1==3:
        answer=n1*n2
        operation="*"     
    elif operation1==4:
        answer=n1/n2
        operation="/" 
    equation = f"{n1} {operation} {n2}"    
             
    print("~~ answer the quetion below (near to the whole number)~~")     
    print("Random Equation:", equation,"=")
    panswer=input()
    if answer==panswer:
        print("Correct")
    else:
        print("Wrong")    
    x=input("do you want to play again?(1 for yes,0 for no):")
    if x==1:
        a=True
    else:
        a=False    
    