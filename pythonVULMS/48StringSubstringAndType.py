#Checking substring in a string using membership operator, It will return only True or False value.
tststr=" A quick brown fox jumps over the lazy dog."
print("Is 'fox' are include in the tststr :","fox" in tststr)  # True
print("Is 'fox' is not include in  tststr :","fox" not in tststr)  # False


tststr1= tststr[4:9] # slicing the string from index 4 to 9 and here 9 is not included.
print("The sliced string is :",tststr1)  # 'quick'

print("The length of the sliced string is :",len(tststr1))  # 5

tststr2= tststr[1:10:2] # slicing the string from index 1 to 10 with step 2
print("The sliced string with step 2 is :",tststr2)  # 'ui'

print("Slicing the string from index 4 to the end :",tststr[4:])  
# 'quick brown fox jumps over the lazy dog.'
print("Slicing the string from start to index 9 :",tststr[:9])  # ' A quick b'

print(tststr[-9:-1]) # 'lazy dog'

print("\n Now we are trying to find the type of the string using different methods.")

print("\n \n ",tststr,"\n \n")

print("The type of tststr is :",type(tststr)) #Will return the type of string.
print("If all are alphanumeric", tststr.isalnum()) #False, because of space.
print("If all are alphabetic", tststr.isalpha()) #False, because of space.
print("If all are digits", tststr.isdigit()) #False, because if contains aphabetic characters.
print("If all are lower case", tststr.islower()) #False, because it contains upper case characters.
print("If all are upper case", tststr.isupper()) #False, because it contains lower case characters.
print("if all are numeric", tststr.isnumeric()) #False, because it contains alphabetic characters.

#Difference between numeric and digit is that numeric can contain decimal points,
#whereas digit can only contain whole numbers.

print("If all are identifiers", tststr.isidentifier()) #False, because it contains spaces.
print("If all are printable", tststr.isprintable()) 
#True, because it contains printable characters.
#It will be false when it contains non-printable characters like \n, \t, etc.