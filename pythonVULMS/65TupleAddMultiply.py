mytuple=(1,2,3)
mytuple2=(4,5,6)
print(f"{mytuple =}\n{mytuple2 =}")

mytuple3=mytuple+mytuple2
mytuple4=2*mytuple
print(f"After add tuple1 to tuple2 {mytuple3 =}")
print(f"After multiplying 2 with tuple1 {mytuple4 =} \n")

mylist=[1,2,3]
mylist2=[4,5,6]
mylist3=mylist+mylist2
mylist4=2*mylist2
print(f"{mylist =}\n{mylist2 =}")
print(f"After adding mylist with mylist2 {mylist3 =}")
print(f"After multiplying 2 with mylist2 {mylist2 =} \n")

str1="Sohail"
str2="Ahmad"
str3=str1+str2
str4=2*str2
print(f"{str1 =}\n{str2}")
print(f"After adding str1 and str2 {str3 =}")
print(f"After multiplying 2 with str2 {str2 =}")