    # Differen()
        # Method returns a new set with value that are in the calling set only

        #The can work with other iterables as well
        # The method can take multiple arguments.
        #Shorthand is the '-' operator, but works only with sets

    #Difference_Update()
        # ->Change the calling set leaving values ONLY present in the calling set.
        
    #symmetric_difference()
        #Returns a new set with all common values removed.
        #Symmetric_difference_update()
            #->Change the calling set, removing all common values.

set1={1,2,3}
set2={3,4,5}

set3=set1.difference(set2) #Elements that are include in set1 and not include in set2
print(f"The difference between set1 and set2 is \n {set3 =}")

set4=set2.difference(set1) #Elements that are include in set2 and not include in set1
print(f"The difference set2 and set1 is \n {set4 =}")


mylist=[5,6,7,8,9,3]
mytuple=(1,5,7,9,11)

set5=set1.difference(mylist)
print(f"Set1 difference mylist will be : \n {set5 =}")

set6=set1.difference(mylist,mytuple)
print(f"Set1 difference mylist and mylist will be : \n {set6 =}")

set7=set1.symmetric_difference(mylist) #Add all elements which are common in both iterable.
print(f"The symmetric difference set2 and mylist is \n {set7 =}")

#set8=set1.symmetric_difference(mylist,mytuple) It takes only one argument 

set1.difference_update(set2)
print(f"After difference update between set1 and set2 {set1 =}")

set2.symmetric_difference_update(mylist)
print(f"Symmetric difference update between set1 and set2 \n {set2}")