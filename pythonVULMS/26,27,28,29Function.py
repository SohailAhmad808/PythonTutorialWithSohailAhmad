#Code block that perform a defined task.
#Help simplify and organized complex code.
#Ideal for reusing code multiple times.
#Defined using def keyword.
#Can accept one or more arguments.
#Use return to send block  result(s).
#Function only execute when called.
def fineprint():
    print("This is the fineprint that printed at bottom")
for i in range(3):
    print("This is the contract person :",i)
    fineprint()
def compute(a,b,c):
    return 2*a,3*b,4*c
k=compute(3,5,6.5)
print("The output of the compute is :",k," And the type is :",type(k))
#Tuple is the python data type which we learn details in details.
#lets unpack the tuple in above
x,y,z=k
print("a = ",x," b = ",y," b = "," c = ",z)
ah,aj,ak=100,200,300
print(ah,aj,ak)

print("\n Now we writing to solve the payroll system")
def payroll(person,basic):
    houserent=0.45*basic
    utility=.10*basic
    grossPay=basic + houserent + utility
    tax=0.15*grossPay
    netpay=grossPay - tax
    print(person,"\tGross salary = ",grossPay,"\ttax = ",tax,"\tNet pay = ",netpay)
for i in range(1,5):
    name = "person"+str(i)
    basicSallery=i*500
    payroll(name,basicSallery)