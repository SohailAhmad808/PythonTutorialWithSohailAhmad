print("We are trying to solve a quadratic equation")
print("ax^2 + bx + c")
a=float(input("Please enter coefficient of x**2  : "))
b=float(input("Please enter the coefficient of x : "))
c=float(input("Please enter the constant term : "))
print("the values you entered are as follows ",a,b,c)

disc=b*b - 4.0*a*c

x1=(-b+disc**0.5)/2*a
x2=(-b - disc**0.5)/2*a

print("x1 = ",x1,"x2 = ",x2)