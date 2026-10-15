
# Lambda Functions are small anonymous[No name Function] functions
# Take any number of arguments
# Consist of a single expression only which is return value
    # -->Trick: use a tuple to return mutiple expressions

# Syntax:
            # lambda arguments : expression
            # Where lambda = keyword

# Lambda expression can include conditional statement.
        # e.g simple data classification function:
        # lambda x:"Positive"if x>0 else "Zero" if x==0 else "Negative"

# Can be used in combination with other Python functions

Result = lambda x: "Positive" if x>0 else "Zero" if x ==0 else "Negative"

print(f"{Result(0) =}\n{Result(1) =}\n{Result(-3) =}")

Myfunction2 = lambda x: x**2 + 3*x +10
# Using lambda function with list comprehension populating list.
li=[Myfunction2(k) for k in range(5)]
print(f"{li =}")

Myfunction3 = lambda a,b,c : (a**2 + b**3, (a-b)**2,a*b*c) # it will return a tuple

My_tuple = Myfunction3(1,2,3)
print(f"{My_tuple =}")

# Unpacking the tuple

d,e,f =My_tuple

print(f"\n{d =}   {e =}   {f =}")