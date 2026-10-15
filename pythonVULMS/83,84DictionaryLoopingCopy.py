Mydictionary=dict([
    (1,"Sohail"),
    (2,"Ahmad"),
    (3,"Khan"),
    (4,454),
    (5,True),
    (6,False),
    (7, "Jonejo")
])
for i in Mydictionary:
    print(f"{i} = {Mydictionary[i]}")
        #Another way to do the same thing
# for k in Mydictionary.keys():
#     print(k)

for l in Mydictionary.values(): #It's only print the values of the dictionary.
    print(l) 

for m in Mydictionary.items(): #It will return a tuple of key: value pair.
    print(m)

# Now we are going toward copying of dictionary.

Mydictionary2 = Mydictionary #It's a shallow copy

Mydictionary3 = Mydictionary.copy() #Deep copy

Mydictionary4 =dict(Mydictionary) #It's alos Deep copy