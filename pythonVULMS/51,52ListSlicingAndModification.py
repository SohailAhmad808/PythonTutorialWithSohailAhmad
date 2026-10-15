mylist = ["Sohail",133,"Ahmad",False,544,"Upper","Khan",8989,True,False]

print("Sohail" in mylist)
print("Ahmad" not in mylist)

mylist1 = mylist[1:4]
print(f"{mylist1 =}")

mylist2 = mylist[ :6]
print(f"{mylist2 =}")

print("\n After modification in list :")

mylist[:0]=["upper"]
print(f"{mylist =}")

mylist[2:3]=["Darling","Afaq"]
print(f"{mylist =}")

mylist[:2]=["Sohail"]
print(f"{mylist =}")
