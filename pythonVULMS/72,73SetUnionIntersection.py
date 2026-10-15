
        # Return a new set
        # Can take 1 or more args
        # Args can be a mix of iterables
        # Shorthand is the '|' but only works with set
set1={1,33,53,55,76,"fox","Lion"}
set2={"the","fox",76}
set3={"Tiger","Wolf","Dog","Lion","fox"}
mylist=[12,False]
mytuple=(45,33,"Sohail","khan",76,"Tiger")

set3= set1.union(set2)
print(f"{set1 =}\n{set2 =}\n \n set1 union set2 will be: {set3 =}")

set4=set1.union(set2,set3)
print(f"After union of set2 and set3 :{set4 =}")

set5=set1.union(set2,set3,mylist,mytuple)
print(f"After union of set1,set2,set3,mylist, and mytuple is \n {set5 =} {type(set5)}")

                # Returns a new set with common elements
                # Works with arguments and other iterable
                #Shorthand '&' (Only works with sets)
                #Intersection_Update()
                        # ->Change the calling set

set6=set1.intersection(set2) # Equal to set6 = set2.intersection(set1)
print(f"After intersection set1 and set2  is :\n{set6 =}")

#set7 = mytuple.intersection(set2)              Tuple object has not attribute 'intersection'.

set7 =set3.intersection(mytuple)
print(f"The intersection between set3 and mytuple is \n{set7 =}")

set8 =set3.intersection(mylist,mytuple) #Empty set
print(f"Intersection between set3,mylist, and mytuple \n{set8 =}\n")

set9={1,0,"fox","Apple,","Mango","Sohail","Ahmad"}
set10 = {True,False,"Sohail","Ahmad"}

print(f"{set9 =}\n{set10 =} \n")

set9.intersection_update(set10)
print(f"After intersection update on set9 with set10: \n{set9 =}")