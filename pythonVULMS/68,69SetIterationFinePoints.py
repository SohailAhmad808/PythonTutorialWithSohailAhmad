#We don not directly access specific item by position
#We can add and delete element in the set, but can't modified.

        #We use membership operator to find the specific element in the set
        #We can iterate the set using for in loop

myset =set({1,2,3,"Dog","Cat",34,"Ahmad","Owl",11,False})

for x in myset:
    print(x)
print("\n Here is the end of loop \n")
print("Is 1 exist in myset or not :",1 in myset)

if "Cat" in myset and "Dog" in myset:
    print("We have find cat and dog.")

                #In set no duplicate are allowed if defined will be ignored.
                        #The set will discart the duplicate values.
                #True == 1 and False == 0 Treated identically
                        #Membership test can be done with either!

myset2={True,False,1,0,"Sohail","Ahmad","Sohail",0,1}
print(f"{myset2 =}")