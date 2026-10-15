# Tuple packing means whenever we have define/create a tuple it is like taking a few element and 
#packing into a single unit or capsule known as tuple.
# 
# On the flip side unpacking means accessing the indivisual elements of a tuple one by one 
# in a order known as unpacking.

fruittuple=("Apple","Apricot","Banana","Orange","Kiwi","Watermelon")

t1,t2,t3,t4,t5,t6 = fruittuple
print(f"{t1 =},\n{t2 =},\n{t3=},\n{t4=},\n{t5=},\n{t6=}")
print("\n The another method is given by : \n")
r1,r2,r3, *r4 =fruittuple
#Note all note created in sequential except *r4.
#The remaining element in r4 form a list.
print(f"{r1 =}{type(r1)},\n {r2 =},{type(r2)},\n    {r3 =}{type(r3)},\n    {r4}{type(r4)}")

r1,r2, *r3,r4 =fruittuple
print(f"{r1 =},\n{r2 =},\n{r3 =},\n{r4 =}")

l1,l2,l3=r3

print(f"{l1 =},\n{l2 =},\n{l3 =},\n")
#WE can do the unpacking with single line of code with list.

str1,str2,str3,str4=l3
print(f"{str1 =}\n{str2 =}\n{str3 =}\n{str4 =}")

