n=int(input("Please enter any integer to sum all number to that number"))
sum=0
for i in range(1,n+1):
    sum=sum+i
print("The sum of ",n,"number is ",sum)
print("\n Now we are checking the divisibility of any number with a specific number :")
a=int(input("Enter starting number"))
b=int(input("Pleae enter the ending number"))
c=int(input("Enter the number to divide by"))
count=0
for i in range( a, b + 1 ):
    if( i % c == 0):
        count += 1
print("There are ",count,"number between ",a," and ",b," that are exactly divisible by ",c)