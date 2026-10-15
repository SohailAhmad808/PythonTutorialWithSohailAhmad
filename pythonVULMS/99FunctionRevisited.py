
# The important aspect of function calling is that you don't know the number 
# of argument pass to the function.

# In simply the number of arguments are changing from argument to argument.

# Passing a variable number of arguments to functions:
    # Used when not sure how many arguments will be passed
# Syntax:
    # def func_name(*args):
        #func_body
# Args are recieved as tuple by the function
# All tuple method are availabele to process the args.

def Myfunction(*args):
    print(f"\n This function recieves a {type(args)} consisting of the value : {args} which are  {len(args)} in number")
Myfunction("Sohail","Ahmad",2,3,4,5)

def add(*Myargs):
    print(f"{type(Myargs) =}  {Myargs =}    {len(Myargs) =}")
add(3,4,5,"Sohail",True)
