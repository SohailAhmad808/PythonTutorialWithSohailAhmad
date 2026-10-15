Mydict = dict([
    (1, "Sohail"),
    (2, "Ahmad"),
    (3, False),
    (4, 23),
    (5, True),
    (6, 343)
])

# We can any they in the dictionary use membership operator.
print(f"{1 in Mydict}")

# find_key=int(input("Please any key in number"))
find_key =3
if find_key in Mydict:
    print(f"The key '2{find_key}' and the value is {Mydict[find_key]}6")
else:
    print(f"The key value {find_key} is not found in the dictionary \n")

# Items are changed according to refrence to there key value
# New items are added by providing a new key.
#The update method:
    #accepts an iterable of key-value pairs.
    #Update existing keys or adds new ones

print(f"\n{Mydict.items()}")

Mydict[7]="Shoaib"
print(f"After add new element {Mydict.items()} \n")

#Heres is beginning of dictionary update.
Dict_Update={
    2: "Khan",
    7: "Shoaib Ahmad",
    8: 777 #This added into the dictionary So we can add new element using update.
}
Mydict.update(Dict_Update)
print(f"After Updating {Mydict.items()} \n")

# Heres is another way to update the dictionary
listUpdate =[[3,True],[5,False]]
print(f"The type of ListUpdate {listUpdate =} \n  {type(listUpdate) =}\n and length is {len(listUpdate) =} \n")
Mydict.update(listUpdate)
#It will also updated by tuples as well.
print(f"After another Update {Mydict.items()}")