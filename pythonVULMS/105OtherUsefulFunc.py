
# zip(iterable1,iterable2)
# Takes two or more iterators and returns a zip object with one member from each iterator
# The zip object can be iterated over the length of the zip  object is the
# the shortest iterator passed as parameter.

Mylist=["First","Second","Third","Fourth","Fifth","Sixth","Seventh"]
Mytuple=("Abdul","Ahmad","Ali","Khan","Sohail","Sher")
Mydic={
    1:"House",
    2:"Apartment",
    3:"Flat",
    4:"Room"
}

Myzip = zip(Mylist,Mytuple)
print(f"The zip is given by \n{Myzip =},    {type(Myzip) =}\n")
# To access the element of zip we have to iterate over it
for x in Myzip:
    print(f"{x =}       {type(x) =}         {len(x) =}")


print("\n\n*********************************************************\n\n")
Myzip2= zip(Mylist,Mytuple,Mydic)

 
for k in Myzip2: # It will return in the form of tuple.
    print(f"{k =},      {type(k) =}     {len(k)}")