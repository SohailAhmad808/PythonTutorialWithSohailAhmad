Test="A quiCk brOWn FOX Jump over ThE laZy Dog"
Test1="     A quiCk brOWn FOX Jump over ThE laZy Dog        "
print("This is capitalize text :",Test.capitalize())
print("This is casefold text :",Test.casefold())#It will convert other then 
#english language character
print("This is lower text :",Test.lower())
print("This is title text :",Test.title())
print("This is upper text :",Test.upper())
print("This is swapecase :",Test.swapcase())


print("\n \n")
print("The String is :",Test1,"\nand the lenght is :",len(Test1))
Test2=Test1.lstrip()
print("After  string is :",Test2,"\nand the lenght is :",len(Test2))
Test3=Test1.rstrip()
print("After right trim",Test3.rstrip(),"\nand the size will be :",len(Test3))
Test4=Test1.strip()
print("After both side stripping :",Test4,"\nand the size will be :",len(Test4))

print(Test1.lstrip(" A")) #It will also trim the character that are put inside 
#paranthesis.