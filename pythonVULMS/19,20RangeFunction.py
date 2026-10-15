#A range is a built-in function in Python that generates a sequence of numbers.
#It is commonly used in for loops to iterate over a sequence of numbers.
#The range function can take one, two, or three arguments: start, stop, and step.
#In Python, in is an operator used to check for membership. 
#It tests whether a value exists in a sequence or collection, and returns either True or False
#Membership operator are used to check whether a value exist inside a sequence or collection, such
#list, tuple, dictionary, set etc.
x=range(11)
print(x,type(x))
guess=int(input("Please enter any integer"))
if(guess in x):
    print("The membership operator return",guess in x)
    print("The value is in the range")
else:
    print("The value is not in the range")
print("Now we are using access the element in the range using for loop and membership operator")
for i in range(4):
    print(i,type(i))
print("\n")
for i in range(7,10):
    print(i)
print("\n")
for i in range(78,100,8):
    print(i)
print("\n")
#just like for loop the break, continue, and else statement are fully functional here.
