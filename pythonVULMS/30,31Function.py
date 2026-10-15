
# Function in Python
# Function is a block of code that only runs when it is called.
# You can pass data, known as parameters, into a function.
# A function can return data as a result.
# Function is a reusable piece of code that can be called multiple times in a program.
# Function is defined using the keyword 'def' followed by the function name and parentheses.
# parameter is a variable in the function definition, 
# while argument is the value that is passed to the function when it is called.
#we can use with different order of parameter of a function using assigning value to the 
# argument of a funtion by usig assigning operator
def myfunction(a,b,c):
    return 7*a,7*b,7*c
i=myfunction(c=2,a=3,b=4)
j,k,l=i
print(j,k,l)


print("\n Function with default argument")
print("Some time a function expect 3 parameter but we are intrested only 1 of them")

def compute(a=2,b=3,c=4):
    #it is must when we assign any one of the variable then we have initialize all of it's right side element, 
    #otherwise it will get an error.
    return 2*a,3*b,4*c
print(compute(b=7))
print("It will return all the value of parameter and we assign only own choice parameter to the function")
#Other value parameter in function prototype are return automatically it's known as default values.
#And the calling parameter will overwritten to the specific number or anything that you provided.


#def compute(a=3,b=4,c)     Error

#def compute(a,b=4,c=7)     It works fine.