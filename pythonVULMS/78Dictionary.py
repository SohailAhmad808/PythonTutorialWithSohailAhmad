# In python, a dicionary is a collection of items but pair of key and value.
# It is ordered, changeable, annd not allow duplicates keys.
# In dictionaries, the keys are unique and immutable, and the values can repeat.
# The dictionary can be created using curly braces {} or the dict() constructor.
# Dictionaries can indexed by keys, not by positions like lists or tuples.
# The differenc vs list is that in list we use index to access the elements,
# but in dictionary we use keys to access the elements.

first_dict = {
    "Name": "Sohail Ahmad",
    "Age": 23,
    "City": "Chitral",
    "Country": "Pakistan",
    "Occupation": "Nothing",
    "Drinking": False
}

print(f"\n{first_dict =} \n{type(first_dict) =} \n{len(first_dict) = }\n")

Second_dict = dict()
print(f"{Second_dict =}\n{type(Second_dict) =}\n {len(Second_dict) = }\n")

third_dict = {}
print(f"{third_dict =} \n{type(third_dict) =}\n{len(third_dict) = } \n")
