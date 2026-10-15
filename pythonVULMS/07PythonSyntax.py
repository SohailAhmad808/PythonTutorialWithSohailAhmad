#python syntax is very simple as compared to other programming languages.
#Point to be noted python is case sensitive language
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
print("The below is code are used with if statement for showing the output")
print("We use a colon immidiate the if condition and the block of the code used in if statement are indented by simply the tab")
if(A4>100):
    print("The weight of the outer disc ",A1)
    print("The area of the inner disc is",A2)
print("The weight of the remaining metal ring is ",A4,"Grams")
print("Now we are going towards about the comments in python")
print("The comment are inline as well as outline")