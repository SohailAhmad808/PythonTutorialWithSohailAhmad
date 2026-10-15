Source = input("Which binary file do you want to enter :")
Destination = Source[0:Source.find(".")]+"_copy"+Source[Source.find("."):len(Source)]
f1=open(Source,"rb")
f2=open(Destination,"wb")

Content=f1.read()
f1.seek(0)

# f2.write(Content)
    #Another way to do this 

chunk_size=100
chunk=f1.read(chunk_size)
while len(chunk_size)>0:
    f2.write(chunk)
    f1.read(chunk_size)

f1.close()
f2.close()