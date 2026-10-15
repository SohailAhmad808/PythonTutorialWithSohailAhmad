mylist = ["Sohail",True,"Ahmad",434,False,False,54,"Khan"]

mylist[1:3]=[False,"ahmad"]
print(mylist)

mylist[0:1]=["Sohail","Ahmad"]
print(mylist)

mylist[2:4] = [False]
print(mylist)

print("Now we are now deleting elements in a list right now a: ")

mylist.insert(8,True) #Insert value at index 2 the value is "True"
print(mylist)

mylist.insert(1,"Lol") # It will insert "Lol in index 1"
print(mylist)

mylist.append("Chitral") #Add element at the end of list
print(mylist)

mylist2=["Library","Kahani"]
mylist.extend(mylist2) #Add mylist2 on mylist
print(mylist)

mylist.extend("This") #
print(mylist)

mylist.extend(["Exntended"])
print(mylist)

mylist.extend([("Sohail")])  #I think It will consider as tuple
print(mylist)

mylist.extend((1,3,44))
print(mylist)
