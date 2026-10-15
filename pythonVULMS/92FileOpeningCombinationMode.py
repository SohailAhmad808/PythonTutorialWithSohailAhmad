
    # rb    -Read binary file(in bytes)
    # r+    -Read and write mode.
    # rb+   -Read and write binary file
    # wb    -Write binary file
    # w+    -Write and read, truncates files if it exist
    # wb+   -Write and read binary file, truncate file if exist
    # ab    -Append in binary mode
    # a+    -Append and read
    # ab+   -Append and read binary
    # xb    -Exclusive creation binary, error if file exist
        # x+    -Exclusive creation and reading; error if file exist
        # xb+   -Exclusive creation and reading binary; error if file exist

source=input("Which file do you want to copy?")
destination = source[0:source.find(".")]+"_copy.txt"
# It's juct create the string which specify the two file source which has already exist
# And the destination which has to be created during execution.

f1=open(source,"r")
f2=open(destination,"w") # f2 name file we have creating in our program.

f2.write("This file has been created by reading/writing the entire file at one go \n\n")

contentf1=f1.read()
print(f"{contentf1 =}")
# f2.write(contentf1)
print("Sohail")

f1.seek(0)
for line in f1:
    f2.write(line)
f1.close()
f2.close()
