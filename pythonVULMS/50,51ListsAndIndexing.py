# A list is a collection of items that can be of different data types (Any type of data).
# And very intrensting thing about list is that it is mutable
# Basically list can not found any other programming languages.
#  items are store in square bracket with single quoted and separated by commas.
# Python has four data types that deals with collection of objects (list, tupels, sets, and dictionaries)

alist=[1,"Sohail",True]
blist=list([1,"Sohail",True])#List using constructor insides are elements of lists.
clist=list() #Empty list
print(f"{alist =}")
print(f"{blist =}")
print(f"{clist =}")
print("\n")
mylist=["my Home",True,"khan",1234,"Upper Chitral",False,543,"Mulkhow"]
print(len(mylist))
print("The elements in the list are as follows:")
for i in mylist:
    print(i)
print("\n The elements in the list in another manner:")
for i in range(len(mylist)):
    print(i)
    print(mylist[i])
    
size = 0
while size < len(mylist):
    print(mylist[size])
    size += 1
mylist[2]=False
print("\n After updation the array will become")
print(mylist)
