def Myfunction(a,b=2,c=3):
    return a*1,b*2,c*3

i=Myfunction(b=3,c=2,a=1)
k,l,m=i

print(f"{i =}\n")

print(f"{k =}   {l =}   {m =}")

def Myfunction2(a,b=2,c=3):
    return a*1,b*2,c*3

ii=Myfunction2(8)
print(f"\n{ii =}")
kk,mm,nn=ii
print(f"{kk =}  {mm =}  {nn =}")
