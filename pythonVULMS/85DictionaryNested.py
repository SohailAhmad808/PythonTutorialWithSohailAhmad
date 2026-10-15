# Dictionaries contains other dictionaries and so on known as 'Nested Dictionaries'
# It's useful when organizational data of similar type e.g (employees)
#item can access using stacked key indexing -[][]

# student1 ={"name":"Sohail","age":22,"grade":"A"}
# student2 ={"name":"Owais","age":23,"grade":"B"}
# student3 ={"name":"Naila","age":25,"grade":"C"}

#     # Creating a nested dictionary, using key:value pairs where each value is itself a dictionary.
# my_class ={
#     "std1": student1,
#     "std2": student2,
#     "std3": student3
# }
my_class ={
    "std1" : {"name": "Sohail","age":22,"grade" : "A"},
    "std2" : {"name": "Owais","age":23,"grade": "B"},
    "std3" : {"name": "Naila","age":25,"grade":"C"}
}

print(f"The Nested dictionary is : {my_class =} \n")

# We are trying to access the element of nested dictionary

print(my_class["std1"]["name"])
print(f"{my_class["std1"]["name"] = }")

# Going toward the nested dictionary

for i in my_class:
    print(f"\n'{i}'")
    for k in my_class[i]:
        print(f"{k} : {my_class[i][k]}")


# FName={"First":"Sohail","Middle":"Ahmad","Last":"Khan"}
# FName2={"First":"Abbas","Middle":"Iraq","Last":"chi"}
# FName3={"First":"Sheikh","Middle":"Idress","Last":"Ahmad"}

# Address1={"HouseNo":"2","Street":"Blue Street","Mohalla":"Gulber-II","City":"Lahore"}
# Address2 ={"HouseNo":"1-A","Street":"Green Street","Mohalla":"Gulberk","City":"Islamabad"}
# Address3 ={"HouseNo":"4-D","Street":"4-Street","Mohalla":"Mastuj","City":"Chitral"}

# House1={
#     "Name1":FName,
#     "ad1":Address1
# }

# House2 ={
#     "Name2":FName2,
#     "Ad2":Address2
# }
# House3={
#     "Name3":FName3,
#     "Ad3":Address3
# }

# Neighborhood={
#     "houseNo1":House1,
#     "houseNo2":House2,
#     "houseNo3":House3
# }



Neighborhood={
    "houseNo1":{
        "Name":{"First":"Sohail","Middle":"Ahmad","Last":"Khan"},
        "Address":{"HouseNo":"2","Street":"Blue-Street","Mohalla":"Gulber-II","City":"Lahore"}
    },
    "houseNo2":{
        "Name":{"First":"Abbas","Middle":"Iraq","Last":"Chi"},
        "Address":{"HouseNo":"1-A","Street":"Green Street","Mohalla":"Gulberk","City":"Islamabad"}
    },
    "houseNo3":{
        "Name":{"First":"Sheikh","Middle":"Idress","Last":"Ahmad"},
        "Address":{"HouseNo":"4-D","Street":"4 Street","Mohalla":"Mastuj","City":"Chitral"}
    }
}
print(f"{Neighborhood.items() =}")

for i in Neighborhood:
    print(f"\n{i}")
    for k in Neighborhood[i]:
        print(f"\n{k}")
        for l in Neighborhood[i][k]:
            print(f"{Neighborhood[i][k][l]}")