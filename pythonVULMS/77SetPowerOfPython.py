str1="""The capital of France is Paris.
    The capital of Japan is Tokyo.
    The capital of Germany is Berlin.
    The capital of Italy is Rome.
    The capital of spain is Madrid.
    The capital of the United kingdom is London.
    The capital of Turkey is Ankara.
    The capital of Sri Lanka is Colombo.
    The capital of Korea is Seoul. """
print(f"{str1 =}  Sohail")

# print("""This is Sohail
#       Ahmad Khan
#       Ahmad Khan
#       Ahmad Khan""") 
#When ever derectly printing a string, it will show the string tha 
#We write in differnt lines print as it is.
#While we stor multi-line string in a variable, and when print it the next line show '\n' on the screen.

str2= str1.lower()
print(f"{str2 =} \n")

list1 = str2.split() #Convert the string into a list and lists are mutable.
print(f"{list1 =}")

set1=set(list1) # The set will remove all the repeating elements in the list.
print(f"{set1 =}")

# list2=list(set1)
# list2.sort()
# print(list2)
            #The code is the shorcut of all the above statement.
# print(f"The distinct word in the paragraph are {set(str1.lower().split())}")
print(f"The distinct words in the paragraph are {sorted(set(str1.lower().split()))}")
