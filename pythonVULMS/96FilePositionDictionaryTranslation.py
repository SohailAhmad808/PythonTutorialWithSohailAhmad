Mydict={
    "Unknown":"Khannnn",
    "Wardon":"Senoir",
    "Hostel":"Housse",
    "upper":"lower"
}
for key, value in Mydict.items():
    print(f"{key =}      {value =}")
Myfile1=open("C:\Project\pythonVULMS\SohailAhmad.txt","r+")
Mycontent=Myfile1.read()

for key,value in Mydict.items():
    Mycontent=Mycontent.replace(key,value)

Myfile1.seek(0)

Myfile1.write(Mycontent)

Myfile1.close()