
# filter() 
# Return an iterator where the items are filtered through a function to test if the item is accepted 
# (True) or (False)

        # filter_Obj = filter(test_function, iterable)
# Test_fuction could be a lambda function.

def test_young(age):
    if (age < 30):
        return True
    else:
        return False
def test_middle(age):
    if (age >= 30 and age <=60):
        return True
    else:
        False
def old(age):
    if(age > 60):
        return True
    else:
        False
Mylist = [10,20,30,40,50,60,70,80,90]

print(f"{Mylist =}")

Young_Once = filter(test_young,Mylist)
Middle_Once = filter(test_middle,Mylist)
Old_Once = filter(old,Mylist)

print(f"\n{list(Young_Once) =}")
print(f"\n{list(Middle_Once) =}")
print(f"\n{list(Old_Once) =}")

Young_Once1= filter(lambda x:True if  x<30 else False,Mylist)
Middle_Once1 = filter(lambda x:True if x >=30 and x<60 else False,Mylist)
Old_Once1 = filter(lambda x: True if x > 60 else False,Mylist)

print(f"\n\n Using Lambda function the values of 'YOUNG', 'MIDDLE' and 'OLD' are\n ")
print(f"{list(Young_Once1) =}\n{list(Middle_Once1) =}\n{list(Old_Once1) =}")