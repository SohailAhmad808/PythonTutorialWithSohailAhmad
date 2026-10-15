#Find the weight of metal required to make an annular ring with inner and outer radii 2cm and 5cm.
#The metal sheet has a grammage of 10gms/cms.
#Assume pi=3.14
print("The area of larger circle")
A1=3.14*5*5
print(A1)
print("The area of smaller circle")
A2=3.14*2*2
print(A2)
print("The area of metal sheet to make the ring")
A3=A1-A2
print(A3)
A4=A3*10
print("The weight of the Metal sheet is :",A4,"Grams")
