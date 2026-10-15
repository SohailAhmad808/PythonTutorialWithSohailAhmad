#When we are handling then the python has maintaining the file position.
# We can ask about the file position and we direct the position.
    # To know the positon we have to call method the .tell()
    # To go to specific position we have to call method .seek()

Myfile1 = open("C:\Project\pythonVULMS\Sohail.txt","r")
Myfile2 =open("Sohail_Ahmad.txt","w")

chunk_size=10
chunk=Myfile1.read(chunk_size)
while len(chunk) > 0 and Myfile1.tell()<50:
    print(f"Position in the input and output files are:     {Myfile1.tell() =} {Myfile2.tell() =}")
    Myfile2.write(chunk)
    chunk=Myfile1.read(chunk_size)

Myfile2.write("\n*********************************************\n")

Myfile1.seek(0)

print(f"The output file is at positionj :  {Myfile2.tell() =}")
print(f"Repositionig the file {Myfile2.tell()-10 =}")

Myfile2.seek(Myfile2.tell()-10)

chunk = Myfile1.read(chunk_size)

while len(chunk) >0:
    print(f"The position in the input and output are : {Myfile1.tell() =} {Myfile2.tell()}")
    Myfile2.write(chunk)
    chunk =Myfile1.read(chunk_size)

Myfile1.close()
Myfile2.close()