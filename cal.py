num1=int(input("enter the first number="))
num2=int(input("enter the second number="))
operator=input("choose  + , - , * , / = ")
if(operator=='+'):
    total=num1+num2
    print("total= "+ str(total))

elif(operator=='-'):
    total=num1-num2
    print("total="+ str(total))    

elif(operator=='*'):
    total=num1-num2
    print("total=",total)

elif(operator=='/'):
    total=num1/num2
    print("total=",total)
else:
    print("invalid input")
