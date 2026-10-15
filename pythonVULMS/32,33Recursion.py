#Recursion is a programming technique where a function calls itself to solve a problem.
#It is often used to solve problems that can be broken down into smaller, similar subproblems.
def ffactorial(n,result=1):
    if(n==1 or n==0):
        print(result)
    else:
       ffactorial(n-1,n*result)
       
f=ffactorial(4)
print(f)

print("There is another way to factorial for the given function using recursion is given by :")
def factorial(n):
    if(n==1 or n ==0):
        return 1
    else:
        return n * factorial(n-1)

print(factorial(3))

print("\n Now we are going toward the fibonacci series ")
def febonaci(n):
    if(n==0 or n==1):
        return n
    else:
        return febonaci(n-1) + febonaci(n-2)
series=int(input("please enter the fibonaci size"))
for i in range(series):
    print(febonaci(i))

