Mylist=["This is written by\n","Sohail Ahmad\n","CEO\n"]
Myfile = open("C:\Project\pythonVULMS\FileOperation.txt","w+")
# "w"   Opens a file for writing. Will create file if it does not exist
#   And if exist it will truncate it to 0 bytes --Be carful

# The mode "w+" can be both read and writeable.

Myfile.write("Sohail")
#Using write() method we can write into the file as a form of string.
#List and other iterable are not allowed.


Myfile.seek(0)

Content1=Myfile.read()
print(f"\n{Content1 =} \n")
Myfile.close()

Myfile2 = open("C:\Project\pythonVULMS\FileOperation.txt","a")
# "a"   Appened a file; contunues adding content to an existing file 
#   will create file if it does not exist.
Myfile2.write("This has been added to the file\n")
#It will add new line as a string in the file as a form of list.
Myfile2.close()

# Myfile3 = open("Myfile3.txt","x")
# # "x"   Exclusive create file; gives error if file exists
# # It will created once when created we do not run again it because in the second it will counter an error message.
# Myfile3.write("This new file has been created\n")
# Myfile3.close()

mylist2=["This is Sohail\n","From Upper chitral\n","Mulkhow Muzhgole\n","Thank you\n"]

Myfile4= open("Khan.txt","w+")
Myfile4.writelines(mylist2)
Myfile4.seek(0) #Return pointer to 0 indexed.
Content3=Myfile4.read()
#Will create a single string.

#If Content3=Myfile4.readlines() Then it will return a list of string including \n.

print(f"{Content3 =}\n")
Myfile4.close()
