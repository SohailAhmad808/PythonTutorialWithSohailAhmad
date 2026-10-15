mylist = ["Sohail","Ahmad",531,"Pass","A+",99,True,False,False]
print(f"\n The orginal list is {mylist =}")

mylist.remove(False) #Removing specific value Not index we can only call the value.
#It will remove the first occurence for the list.
print(f"\n The list after removing false {mylist =}")

mylist.pop()
print(f"After pop the list will be {mylist =}")

mylist.pop(1)
print(f"After pop in index 1 {mylist =}")

mylist.clear() #Empty list
print(mylist)

mylist = ["Sohail","Ahmad",531,"Pass","A+",99,True,False,False]

del mylist[1] #python function not list method "del"
print(f"After using del function : {mylist =}")
del mylist
print("\n \n mylist has no longer exist : Due to we use del function over list. \n")
# print(mylist) It will generate an error

# We can also use delete function with slicing.
