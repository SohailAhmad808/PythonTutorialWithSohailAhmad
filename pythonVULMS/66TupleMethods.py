mytuple=(1,3,4,5,5,5,6,7,55,76,56,44,5,88,23)
print(f"The number 5 occures in tuple {mytuple.count(5)} times") 
#count method always need one argument to call.
print(f"The first occurence of 5 in index {mytuple.index(5)}")
#It return the first occurence of the item '5'

#print(f"{mytuple.index(77)}")
#If the element are not found in the tuple in will throw an exception
del mytuple
#print(mytuple)     Will encounter an error.