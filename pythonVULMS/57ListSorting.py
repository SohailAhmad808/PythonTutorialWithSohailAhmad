# List can be sorted using
        # sort()
        # sort(reverse = True)
        # sort( key = function )

# This sort to be happen in list has the list has to be uniform mean that they have same datatype.
# If we use sort method when all item all not in same data type it will generate an error message.
fruitlist = ["banana","apple","Cherry","Mango","Apricot","Mulbery","Watermelon"]
fruitlist.sort()
print(f"{fruitlist =}")

fruitlist.sort(reverse=True)
print(f"{fruitlist =}")

fruitlist.sort(key=str.lower)
print(f"{fruitlist =}")

mynum = [23,54,22,54,-33,-44,43,-2,-8,56]
mynum.sort()
print(f"{mynum =}")

mynum.sort(reverse = True)
print(f"{mynum =}")

mynum.sort(key = abs) 
# The term abs represent absulut value of any number, and it gives always positive number.
print(f"{mynum =}")

def myfunc(n):
    return 500 - abs(n)
mynum.sort(key = myfunc)
print(f"{mynum =}")