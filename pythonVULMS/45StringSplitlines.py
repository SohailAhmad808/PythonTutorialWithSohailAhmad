print("Sohail Ahmad".splitlines())#Default behavior is to split at line breaks.
tststr="A quick brown \n fox jumps over \n the lazy dog"


#List is a data structure that can hold multiple values. And lists are muatable(can be changed).


tststr1=tststr.splitlines()#it will split at line breaks.
print(tststr1)

tststr2=tststr.splitlines(True)#It will keep the line breaks in the output.
print(tststr2)

tststr3=tststr.splitlines(keepends=True)#It will keep the line breaks in the output.
print(tststr3)

tststr4=tststr.split()
print(f"{tststr4 =}")

tststr5=tststr.split("jumps")#It will eliminate the word "jumps" and split the string at that point.
print(tststr5)

print(tststr.split("o"))

print(tststr.split("o",2))#It will split the string at the first two occurrences of "o".
#Note it will not change the original string, it will return a new list with the splits.
