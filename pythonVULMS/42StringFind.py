tststr="   A quick brown fox jump over the lazy dog    "
look="o"
n=tststr.find(look,0,30)
if(n==-1):
    print("The value not in the string :")
else:
    print(look," occure in position of ",n)
k=tststr.index(look,0,30)
#If index not able to find the element in string it will throw an exception 
#We will understand it later.
print(look,"The element in index ",k)
h=tststr.rfind(look)
if(h==-1):
    print("The value not in the string :")
else:
    print(look," occure in position of ",h)
#The only difference is that it will trying to find the element from right to left.
print("There is another method called lfind it will search from left to right.")