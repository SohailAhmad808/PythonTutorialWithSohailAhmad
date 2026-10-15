set1=set({12,32,"Sohail","Ahmad",False})
set2={32,34,55,67}
print(f"{set1}")

set1.add("Khan") #add method is used only one element to add in the set.
print(f"After using add method {set1 =}")

set1.update(set2)
print(f"After updating set1 {set1 =} \n")

set1.update({"Muzhgole","Chitral"})
print(f"After updating element by manually {set1 =} \n")

set3 =set()
mytuple=("Zebra","Hourse","Boffallo","Monkey")
mylist=["Peacock","ostrich","Bird","penguine"]

set3.update(mytuple,mylist) #We can add list and tuple to a set at a time.

print(f"The new set is given by : {set3 =} \n")

        #We can remove elements by 
          #remove(), discard(),pop() methods
        
        # Emptying a set 
          # clear() method

        #Deleting a set from memory:
          #del function
        
set4={"Sohail",34,43,55,"Khan",12,"Ahmad",45,76,"Upper"}
print(f"The set4 will be : {set4 =} \n")

set4.remove(55) #It will give an error when value the given value are not found in set.
#Throws a keyError.
print(f"After removing 55 {set4 =} \n")

set4.discard("Ahmad") #No error if value not found.
print(f"After discard 'Ahmad' From the set {set4 =} \n")

a=set4.pop() #A random element is removed and returned
print(f"The removed is '{a}' and remaining set is \n {set4} \n")

set4.clear() 
#Note all clear method remove all the element and the set still exist with empty value.
print(f"After using clear method the set will be {set4 =}")

del set4 
#The set has no longer exist because we permenently delete from the memory
