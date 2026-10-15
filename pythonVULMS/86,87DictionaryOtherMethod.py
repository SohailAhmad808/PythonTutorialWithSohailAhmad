
    # fromkey(list/tuple, value)
    # Method of dict() class
    # Create a new dictionary with keys specified in list/tuple.
    # If a value specified, the same value is given to all keys

Key_list = ["Brand","Model","Year"]

mydictionary=dict.fromkeys(Key_list) #Here the key_List become the key and value none to all
print(f"{mydictionary.items() =} \n")

mydictionary=dict.fromkeys(Key_list,"Fromd") # It will asign all the value of dictionary to 'Fromd'
print(f"{mydictionary.items() =} \n")

mydictionary["Model"]="Mustang"
mydictionary["Year"]=1959

print(f"{mydictionary.items() =} \n")

    # setdefault(key,value)
    # Return values of item with specified key(value is ignored)
    # If key does not exist, it is created & the value assigned
    # If the value is not provided, the key is created with 'None' as the value.
value = mydictionary.setdefault("Model")
print(f"{value =} \n")

value1 = mydictionary.setdefault("Model","Fairlane")
print(f"{value1 =} \n")
#The set default method return the value assocaited with 'model', ignoring the value in the calling statement.

value2=mydictionary.setdefault("Cartype","Saloon")
print(f"If the key not exist it will create a new key {value2 =} \n")
print(f"{mydictionary.items() =}\n")


print(f"{mydictionary.keys() =}\n")
print(f"{mydictionary.values() =}\n")

value3=mydictionary.keys()
value4=mydictionary.values()
value5=mydictionary.items()

print(f"{value3 =} , {type(value3) =}, and {len(value3) =} \n")
print(f"{value4 =} , {type(value4) =}, and {len(value4) =} \n")
print(f"{value5 =} \n , {type(value5) =}, and    {len(value5) =} \n")


# In simply say that Dictionary views such as Dictionary.value(), Dictionary.items(), and Dictionary.keys() are dynamic 
# updating to reflect changes in the keys or values.
