Mydict={
    1: "Sohail",
    2: "Ahmad",
    3: False,
    4: 23,
    5:True,
    6: 343
}
            # OR
# Mydict = dict([
#     (1, "Sohail"),
#     (2, "Ahmad"),
#     (3, False),
#     (4, 23),
#     (5, True),
#     (6, 343)
# ])
print(f"{Mydict[1] =}\n")
#We can access the same thing using get method.

print(f"{Mydict.get(2) =}\n")

#We can access the value of key using the keys method.
print(f"{Mydict.keys() =}\n")

# Similarly, we can access the values of the dictionary using the values method.
print(f"{Mydict.values() =}\n")
# All key: value pairs can be obtained as a list of tuples using item method.
print(f"{Mydict.items() =}")
