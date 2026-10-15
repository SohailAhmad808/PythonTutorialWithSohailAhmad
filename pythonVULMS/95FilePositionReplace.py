Myfile1=open("C:\Project\pythonVULMS\Education01.txt","r+")
Searchstr=input("String to search for : ")
Replacestr=input("The given string replace : ")
Content=Myfile1.read()
New_Content = Content.replace(Searchstr,Replacestr)
#After storing the content of file in variable,then using method of string to replace the content.
Myfile1.seek(0)
Myfile1.write(New_Content)
Myfile1.close()

#If the size of the Replacestr size is equal or greater to the size of Search string 
#It will be normal

#Whenever the size not equal then the interpreter add extra garbage value at the end.

#Remember replace the size of Replace content must equal 

Source=input("Please name the file which you want to open :")
Searching_Strig=input("String to be search for : ")
ReplacingString=input("The string replaced with : ")

if len(Searching_Strig) == len(ReplacingString):
    Myfile2=open(Source,"r+")
    FileContent=Myfile2.read()
    Myfile2.seek(0)
    New_File_Content=FileContent.replace(Searching_Strig,ReplacingString)
    Myfile2.write(New_File_Content)
    Myfile2.close()

# Myfile3 =open("","r+")
# Myfile4=open("","r+")
# Stringg=input("enter the string")
# StringReplace=input("Enter the replacing value")
# for i in Myfile4:
#     New_Content1=i.replace(Stringg,StringReplace)
#     Myfile3.write(New_Content)
# Myfile3.close()
# Myfile4.close()