
    # copy()    returns a copy of a set (deep copy)
    # isdisjoint()    whether two sets have common elements.
    # issubset()    whether one set a subset of the another set.
    # issuperset()  whether on set is a subset of the other.
    # isfrozenset() constructor for a frozen set.
            # -> Frozen set are those type of set whenever creater are fixed we have not permission
            # to remove or add any member to that set.

set1={1,2,3,4}
set2=set1 #(shaloo copy)
print(f"\n\nThe {set1}")
set1.add(100)
print(f"After adding element 100 to {set1 =} \n")

set3=set1.copy()
set1.add(200)
print(f"{set3 =}")
print(f"And {set1 =}")
set4={2,4,5,6,7,8}
print(f"Is {set1} disjoint with {set4} =  {set1.isdisjoint(set4)}")
set5={10,20,25,9}
print(f"Is {set1} disjoint with {set5} = {set1.isdisjoint(set5)}")

# set1 is subset of set2
print(f"Is {set1 =} subset of {set2 =} = {set1.issubset(set2)}")
print(f"Is {set2 =} subset of {set1 =} = {set2.issubset(set1)}")
print(f"Is {set1 =} subset of {set5 =} = {set1.issubset(set5)}")
# set1 is superset of set2
print(f"Is {set1 =} superset of {set5 =} = {set1.issuperset(set5)}")
# set5 is superset of set1
print(f"Is {set5 =} superset of {set1 =} = {set5.issuperset(set1)}")

# set1 is frozenset.
set6={"Sohail","Ahmad",343,False,True,"khan"}
fset=frozenset(set6)
print(f"{fset =}")

print(frozenset({1,3,4,6,55})) #Frozenset are create through frozen keyword.