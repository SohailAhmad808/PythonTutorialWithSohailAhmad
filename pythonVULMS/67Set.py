
    #One of 4 collection type (with list,tuple,dictionary)
#Set is datastructure that can store any type of data with not linear order. Using some method and function we can deal with set. 
# But it is notice that we can't access are item using some specific index.
#Created using set() or {}
    #but {} creates a dictionary, not an empty set
#Hold mix data types.
#Unordered,Unindexed,Immutable
#In set not can not create empty set using brasses. We you do it become dictionary
#We use set() constructor to create a empty set as well.

        #No duplicate are allowed in set.

set1={1,2,43,3,53,5,23}
print(f"{set1 =}")

set2={"Sohail","Ahmad",100,-6,-78,333,1,343,"Ahmaaad"}
print(f"{set2 =}")

set3=set()
print(f"An empty set created using the constructor :{set3 =}")

mylist = ["Sohail",False,423,"Ahmad",True,98,"Khan"]
print(f"{mylist =} {type(mylist)}")
set3=set(mylist)
print(f"After{set3 =}{type(set3)}")