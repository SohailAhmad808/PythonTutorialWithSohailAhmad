fruitlist = ["banana","Apple","Cherry","Mango","Apricot","Mulbery","Watermelon"]

fruitlist1=fruitlist 
#It don't create two seprate list in memory it just create refrence to fruitlist
#Fruitlist1 and fruitlis are two refrences of same memory location.

# It is also called shallow copy means only create a refrence

#We need to deep copy which means two differenct memory location are used for same group of items.

           # Alternatives are:
                # copy()      it's a method.
                #list()         constructor method based on any iterable
                #[:]            Using slice operator which fools the direct copy.
fruitlist[0]="Sohail"
print(f"{fruitlist =}")
print(f"{fruitlist1 =}") #Because it's a shallow copy.

fruitlist2 = fruitlist.copy()
fruitlist[0]="Watermelon"
print(f"{fruitlist =}")
print(f"{fruitlist2 =}")

fruitlist3 = list(fruitlist)
fruitlist3[0] = "Khan"
print(f"{fruitlist3 =}")
print(f"{fruitlist =}")

fruitlist4 =fruitlist[:]
fruitlist4[0] = "Sohail Ahmad"
print(f"{fruitlist4 =}")
print(f"{fruitlist =}")


