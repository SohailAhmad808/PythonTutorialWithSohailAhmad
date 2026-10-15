#List comprehension is a shortcut for creating list based on condition.

 # newlist = [ [expression] + [for] + [item] + [in] + [iterable] + [if] + [condition] => [True] ]

    #It is very powerful construct
fruitlist = ["banana","Apple","Cherry","Mango","Apricot","Mulbery","Watermelon"]
fruitlist1=[]
for x in fruitlist:
    if "o" not in x:
        fruitlist1.append(x)
print(fruitlist1)

fruitlist2 = [x for x in fruitlist if "o" not in x] 
#Main idea is to notice is expression that expression will stores in the new list.

fruitlist2 = [x+x for x in fruitlist1]
print(fruitlist2)

fruitlist3 = ["Sohail" for x in fruitlist2]
print(f"{fruitlist3 =}")

mylist = [x for x in range(100) if x%7 == 0]
print(f"{mylist =}")

mylist1 = [x if x%3==0 else 0 for x in range(100,200,2) if x%8 == 0]
print(f"{mylist1 =}")

