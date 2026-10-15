print("Time taken to generate a list :")
xlist=[x**3 for x in range(20)]
print(f"\nList generated :{xlist =}")

xgen=(k**3 for k in range(15))
print(f"\nThe generator is : {xgen =}\n")

count=0
print("Now: It's a generator function we have to looping through it:\n")
for count in range(10):
    print(f"{count =}**3 is {next(xgen) =}")
print("\n")
# To access the remainin ones as follows: 
for f in xgen:
    print(f"{count =} is {f =}")