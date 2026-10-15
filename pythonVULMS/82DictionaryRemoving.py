Mydictionary=dict([
    (1,"Sohail"),
    (2,"Ahmad"),
    (3,"Khan"),
    (4,454),
    (5,True),
    (6,False),
    (7, "Jonejo")
])
print(f"{Mydictionary.items()}")
pop_value= Mydictionary.pop(4,"Not found") 
#It will return an error when we don't provide a default value.
# In here the 6 is the item that will remove from the dictionary and Not found is the default value.
print(f"The element is remove {pop_value = } ")

pop_value2 = Mydictionary.popitem()
#Pop is basically a method it will remove last key: value whenever we don't provide any value.
print(f"{pop_value2 = }")

del Mydictionary[1]
print(f"After deleting key of value 1 \n{Mydictionary.items()}")

Mydictionary.clear()
print(f"After clearing the dictionary :\n{Mydictionary.items()}")

del Mydictionary
#The dictionary has no longer exist, It will permenently removed from the memory.
