#The sep.join() method is used to join the elements of and iterable (like a list or tuple) 
# into a single string, with a specified separator between each element.

tstlist=["A","quick","brown","fox","jumps","over","the","lazy","dog"]
tstlist1=" ".join(tstlist)#It will join the list elements with a space.
print(tstlist1)

tstlist2=('A','quick','brown','fox','jumps','over','the','lazy','dog.')
tstlist3=" ".join(tstlist2)#It will join the tuple elements with a space.
print(tstlist3)

#f-string are those strings that are prefixed with 'f' or 'F' and allow you to embed espressions
#inside string literals, using curly braces {}.

#In programming languages, a literal is a fixed value written directly in the code. 
# Examples include numbers (5, 3.14), strings ("hello"), 
# booleans (True, False), and more.

num=200
num2=1234
fnum=123.45
testlist=["list element",101,True]
mytuple=(1,3,4)
print(f"my list contians a number :{num}, a string : {testlist} and a tuple : {mytuple}")#This will print the values of num,
#testlist, and mytuple inside th string.


print(f"my list contians a number :{num=}, a string : {testlist=} and a tuple : {mytuple=}")
#This will print the variable names and therir values inside th string.

print(f"An f string with width=10 {num:10}")#This will print the value of numm with a width of 10 characters.
print(f"An f string with width=10 {num2:10}")#This will print the value of num2 with a width of 10 characters.
print(f"An f string with width=10 with four decimal places {fnum:10.4f}")
#This will print the value of fnum with a width of 10 characters and 4 decimal places.

print(f"An f string with width=10 align left {num:<10}")#left aligned
print(f"An f string with width=10 align right{num:>10}")#right aligned and it's default
print(f"An f string with width=10 {num:^10}")#It will center align the value of num in a field of width 10 characters.


print(f"String having width=10 align right and padded {num:*>10} ")
#As usual aligned right and padded with * character.

print(f"string having width=10 align left and padded with staric {num:*<10}")