mytuple = ("Sohail","Khan",343,True,"Ahmad",False)

mytuple1 = mytuple[2:4]
print(f"{mytuple1 =}")

mytuple2 = mytuple[3:]
print(f"{mytuple2 =}")

mytuple3 = mytuple[ :4]
print(f"{mytuple3 =}")

mytuple4 = mytuple[-3:-1]
print(f"{mytuple4 =}")

mytuple5 = mytuple3 + mytuple4 # cancetenate two tuples 
print(f"{mytuple5 =}")
 
print("\n Converting tuple into list, Modify it and then again converting it into tuple \n")

mylist = list(mytuple)
print(f"{mylist =}", type(mylist))

mylist[3:4]=["Muzhgole","Morder"]
print(f"{mylist =}",type(mylist))

mytuple=tuple(mylist)
print(f"{mytuple =}", type(mytuple))