tststr="A quick the brown fox jumps over the lazy dog"
print(tststr.replace("dog","ostrich"))#It will replace the first occurrence
print(tststr.replace("o",""))#It will remove all occurrences of 'o'
print(tststr.replace("o","",1))#It will replace only the first occurrence of 'o'
#Note it will not change the original string, it will return a new string with the replacements.
tststr1="A quick brown fox \t jumps over the \t lazy dog"
print(tststr1.expandtabs(3))#It will replace the tab with 3 spaces

#Partitioning is a method that splits a string into three parts based on a separator.
#The partition method recieves an argument which is seprator and returns a 
#tuple containing three parts: the part before the separator, the separator itself, 
#and the part after the separator.

#if not found, it returns the original string and two empty strings.

print(tststr.partition("fox"))#It will return a tuple with three parts

print("A tuple is a data structure that can hold multiple values. And tuples are immutable.")

print(tststr.partition("Sohail Ahmad"))#Will return the original and two empty strings.

print(tststr.rpartition("the"))#Check from the right to left.