
#File handling requires precise management it resources
# Open files must be closed
# Exception occure may happen when reading or writting files.
# Clean technique, use context:
    # with open(file, mode) as handler
        # file.action()(read,write etc)

# No need to close the file. Exiting the block will close it.
# Even if exception happens, file will be properly CLOSED.

with open("C:\Project\pythonVULMS\Khan.txt","r+") as Myfile1:
    Content=Myfile1.read() #The file will closed here

# The with keyword is used to create a context manager, which sets up a context for a 
# block of code and ensures resources are properly cleaned up after execution, 
# even if an error occurs
with open("ContextProgramming.txt","w") as Myfile2:
    Myfile2.write(Content)
print(f"{Content =}")

# The important think is that the file will closed atomatically.

# The as keyword assigns the object created by the context manager to a variable, 
# allowing you to reference it within the with block. 
# It provides a convenient alias for the resource being managed.

with open("Khan.txt","r") as Myfile3, open("C:\Project\pythonVULMS\FileOperation.txt","r") as Myfile4:
    Content1=Myfile3.read()
    Content2=Myfile4.read()
    print(f"\n{Content1 =}\n\n{Content2 =}\n")

# Another important point is that when the file is closed then all the operation
# copy into the hard disk otherwise it will stored at buffer.

