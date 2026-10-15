# In computer science, a file is a collection of data or information stored on a computer, 
# identified by a filename. It can contain text, images, programs, or any other type of data.

# In Python, a file usually refers to a text or binary document that you can 
# read from or write to using Python’s built-in file handling functions 
# (like open(), read(), write()). 
# Files are used to store data permanently outside of the program’s memory.

    #Files are broadly classify as
     # -> Text file 
        # (stored in raw bytes, not directly readable as text. Used for images,videos)
     # -> Binary file
     #  (Strored data as readable characters(letter,numbers) using a character encoding like UTF-8)
#Primary function performed on the file are
    # Opening   #Reading    #Writing    #Closing

FileHandling = open("C:\Project\pythonVULMS\Myfile.txt")
#When we attach the mode the python consider it only for reading.
#If the file in the same directry then called with simple otherwise will associate with full path.
FileData=FileHandling.read()
print(f"\n {FileHandling =}\n")
print(FileData)

#Whenever we open a file then we have must close it because the resources deallocated.
#When we not deallocate the file there will chance of damage and override of the files.
FileHandling.close()
# str = "Sohail"
# print(str)
            # It not a good programming we override buit in string type(Keyword)
# k = str(input("Sohail"))