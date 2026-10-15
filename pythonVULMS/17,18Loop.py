i=200
while(i>0):
    if(i>=70 and i <=150):
#       print("Inside the loop")
        i-=7
        continue
    if(i<50):
        break
    print(i)
    i-=7
else:
    print("The loop has ended")
    #Note it will will not execute here because it is associated with loop and here loop where break