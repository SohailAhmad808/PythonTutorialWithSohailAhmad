print("Sohail Ahmad")
print("""String is like an array of characters but because the nature of string.
we can do indexing in it""")
str1="Sohail Ahmad"
strlen=len(str1)
print("The String is :",str1," an the lenght is :",strlen)

print("The value in each index in given by :")
for i in range(strlen):
    print(str1[i])
print("\n Now we have to find the consonant sound alphabet in the above string :")
for c in str1:
    if c not in "aeiou":
        print(c)

#str1[5]='z'        We can't do this because an string is immuatable.
str2=str1[0:5]+'b'
print(str2)
str2=str2+str1[6:len(str1)]
print(str2)