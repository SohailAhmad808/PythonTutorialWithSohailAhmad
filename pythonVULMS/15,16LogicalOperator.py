#Logical operators are used to combine conditional statements.
#Conditonal statments are statements that evaluate to either true or false.
#They are used to perform logical operations on boolean values.
#Basically there are only basic logical operator that is AND,OR, and NOT.



print("We want to print the truth table of AND")
a=True
b=True
print("a\tb\ta and b")
print(a,"\t",b,"\t",a and b)
a=True
b=False
print(a,"\t",b,"\t",a and b)
a=False
b=True
print(a,"\t",b,"\t",a and b)
a=False
b=False
print(a,"\t",b,"\t",a and b)
#Basically there are only basic logical operator that is AND,OR, and NOT.
print("We want to print the truth table of OR")
a=True
b=True
print("a\tb\ta or b")
print(a,"\t",b,"\t",a or b)
a=True
b=False
print(a,"\t",b,"\t",a or b)
a=False
b=True
print(a,"\t",b,"\t",a or b)
a=False
b=False
print(a,"\t",b,"\t",a or b)
print("Print the age of a person either child, Teen, Adult, or senoir")
agee = int(input("Please enter the age :"))
if(agee  < 13):
    print("Child")
if(agee >=14 and agee <=19):
    print("Teen age")
if(agee>=20 and agee<=59):
    print("Adult")
if(agee>60):
    print("Senoir")
print("Print the age of a person either child, Teen, Adult, or senoir")
agee = int(input("Please enter the age :"))
if(agee  < 13):
    print("Child")
else:
    if(agee>=24 and agee<=19):
        print("Teen Age")
    else:
        if(agee>=20 and agee<=59):
            print("Adult")
        else:
            print("You are Senoir!")