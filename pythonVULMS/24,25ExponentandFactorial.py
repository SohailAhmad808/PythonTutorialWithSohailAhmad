base=int(input("Please enter the base"))
power=int(input("Please enter the exponent"))
result=1
Temp=power
while( Temp > 0):
    result*=base
    Temp-=1
print("\n ",base," raised to the power ",power,"is ",result)

factNum=int(input("Please enter the number for factorial in this case"))
temp=factNum
result2=1
while(temp > 0):
    result2*=temp
    temp-=1
print("The factorial of ",factNum, " is given by",result2)

c=int(input("Enter another number for factorial"))
factorial=1
for i in range(1,c+1):
    factorial*=i
print("The result of another factorial is :",factorial)