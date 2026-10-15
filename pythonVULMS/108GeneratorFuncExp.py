# SWAP

x=30
y=40
print(f"Before swapping :{x =} and {y =}")
TEMP=x
x=y
y=TEMP
print(f"After swapping :{x =} and {y =}")

x,y=y,x
print(f"Using shortcut method swapping {x =} and {y =}")

# Febonaci Generator

def fib_gen():
    first,second=0,1
    while True: # Infinit loop continous generating febonaci based on you code.
        yield first
        first,second=second,first+second
fibResult=fib_gen()
print(f"{type(fibResult) =} and {fibResult =}")
for i in range(10):
    print(f"{i =} and Fibonaci {next(fibResult) }")

Mycount=0
for m in fibResult:
    print(m)
    Mycount+=1
    if Mycount>=3:
        break
