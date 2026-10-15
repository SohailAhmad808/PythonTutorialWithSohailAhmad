MyFile=open("C:\Project\pythonVULMS\Education01.txt","r")
        #Open for reading only. Assume file is plain text only.

Content_In_File =MyFile.read() 
print(MyFile)
        # Read()    Return the entire content of the file as a string

MyFile.seek(0) #Return pointer to the beginning.


print(f"\n\n{Content_In_File =} \n\n {type(Content_In_File) =} \n {len(Content_In_File) =}\n")
Content_In_File2 =MyFile.readline() 
        # Readline()    Returns one line of a file including \n characters

MyFile.seek(0) #Return pointer to the beginning.


print(f"\n{Content_In_File2 =} \n\n {type(Content_In_File2) =} \n {len(Content_In_File2) =}\n")
Content_In_File3 =MyFile.readlines()
        # Readlines()   Return all line of a file as a list of string.
        #               --> Each one including \n character
print(f"\n{Content_In_File3 =} \n\n {type(Content_In_File3) =} \n {len(Content_In_File3) =}\n")

MyFile.seek(0) #Return pointer to the beginning.


Content_In_File4=MyFile.read(7)
        # Read(n)   Read(max) n character/bytes at a time read from the file.
        #           --> n is any number which indentifies that number of characters to be read from the file.
print(f"\n{Content_In_File4 =} \n\n {type(Content_In_File4) =} \n {len(Content_In_File4) =}\n")

MyFile.seek(0) #Return pointer to the beginning.

        #Intresting fact about Read(n)
Content_In_File5 =MyFile.read(4)
while(len(Content_In_File5) > 0):
    print(Content_In_File5,end='')
    Content_In_File5=MyFile.read(3)

MyFile.seek(0)
#The concept of pointer is clear here.

# Membership operator -- Loop through file line by line.

for Content_In_Files6 in MyFile:
    print(Content_In_Files6,end='')

MyFile.close()

# "w"   Opens a file for writing. Will create file if it does not exist
#   And if exist it will truncate it to 0 bytes --Be carful


# "a"   Appened a file; contunues adding content to an existing file 
#   will create file if it does not exist.

# "x"   Exclusive create file; gives error if file exists
#   Can write to the file but cannot read it.