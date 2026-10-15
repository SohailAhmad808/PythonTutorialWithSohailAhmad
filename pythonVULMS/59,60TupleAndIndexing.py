# Tuple is one four collection type (list,sets,dictionary)
#created with () or tuple()
#Single element needs a comma to seperate it from others
#Can hold mix data type
#Allow duplicate
#The difference between tuple and list is that Tuples are immutables. 
# Once you define an element you can't change them


#The square bracket remember do double duty one for defining list,
# and another for indexing any iterable.

# Ordinary paranthesis (bracket) are used to define a tuple.

mytuple = ("Sohail","Khan",343,True,"Ahmad",False)
mytuple1=([1,True,"Sohail","khan"]) #The list be converted into tuple.
mytuple2 = tuple()
mytuple3 =("khan")
mytuple4=("Sohail",)
#For single element in tuple we must use comma after the element otherwise it will be string.

print(f"{mytuple =}")
print(f"{mytuple =}")
print(f"{mytuple1 =}")
print(f"{mytuple2 =}")
print(f"{mytuple3 =}",type(mytuple3),len(mytuple3))
print(f"{mytuple4 =}",type(mytuple4),len(mytuple4))

#Tuple can also be created from the list using constructor.
print("\n The element in mytuple is given by :")
for i in mytuple:
    print(i)
print("\n Another of accessing the element of mytuple using range function :")
for k in range(len(mytuple)):
    print(mytuple[k])
m=0
while (m<len(mytuple)):
    print(mytuple[m])
    m+=1