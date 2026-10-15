variable="upper Chitral"
print(variable.ljust(50))
print(variable.rjust(50))
print(variable.center(50))

print(variable.ljust(140,"-"))
print(variable.rjust(140,"-"))
print(variable.center(140,"-"))

Nishmar="     A quick brown fox jump over the lazy dog     "


print("Simple count will be :  ", Nishmar.count("f"))

for i in "abcdefghijklmnopqrstuvwxyz":
    print(i,Nishmar.count(i),"     And the upper will be :    ",i.upper(),Nishmar.count(i.upper()))