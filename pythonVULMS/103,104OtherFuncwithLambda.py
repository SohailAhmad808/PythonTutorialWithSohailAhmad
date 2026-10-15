 
# map()
# Execute a specific function for each item in an iterable
    # map_obj = map(func,iterable)
# Function could be a lambda function

def myfunction(x):
    return len(x)
Mylist = ["Mango","Orange","Applee","Watermelon","cherry","bananana"]
print("\nUsing function with map:")
print(f"The list is given by \n{Mylist =}")
print(f"The number of character in each list are :")
The_Length=map(myfunction,Mylist)
print(The_Length)
print(f"{list(The_Length) =}")

        # OR
print(f"\n This is another way to find the lenght of the list\n")
print(f"{list(map(myfunction,Mylist))}")

# Now by using lambda function to do this:

print(f"\nNow using with lambda function : \n\n{list(map(lambda x: len(x),Mylist)) =}")

# Sorted()
# Return a sorted list of all the specific iterable object
# The sorting key may be provided as a function
# Sorting can ascending or descending
# Default: String are sorted alphabetically, numbers numerically

    #Syntax
        # Sorted_obj= sorted(iterable,key=key,reverse=reverse)
                # (key and reverse are optional)
            #Key could a lambda function.
print('\nnow we are going towards sorting :')

Mylist.sort()
print(f"\n{Mylist =}\n")
Mylist.sort(key=str.lower)
print(f"{Mylist =}\n")
Mylist.sort(key=str.lower,reverse=True)
print(f"{Mylist =}\n")

print('\n all are we do this using a sort() method now doing the same thing with function name as sorted')

New_list=sorted(Mylist)
print(f'{New_list =}\n')

New_list2=sorted(Mylist,key=str.lower)
print(f'{New_list2 =}\n')

New_list3=sorted(Mylist,key=str.lower,reverse=True)
print(f'{New_list3 =}')

New_list4=sorted(Mylist,key=len) # Sort it according to the size.
print(f'{New_list4 =}')

def sort_key2(x):
    return x[0]
Mylist5=[(18,"Zulfiqar"),(50,"Abdul"),(60,"Babar")]
New_list5=sorted(Mylist5,key=sort_key2)
# It work on the principal of checking for each element the sort_key2 pass the that value to function sort_key2
#Then the function return the first value of a tuple of a list
# On the base of that value the sorted function sort the list which containing the tuple.

print(f"\n\n{Mylist5 =}\n{type(Mylist5) =}\n {len(Mylist5) =}\n")
print(f"{New_list5 =}")

    # Now: using the lambda function for sorting
New_list6 = sorted(Mylist5,key= lambda x: x[0])
print(f'\nthis is sorting with x[0] :  \n{New_list6 =}\n')
New_list7 = sorted(Mylist5,key=lambda x: x[1],reverse=True)
print(f"this is sorting using key on the basis of x[1] and reverse = true :  \n{New_list7 =}\n")