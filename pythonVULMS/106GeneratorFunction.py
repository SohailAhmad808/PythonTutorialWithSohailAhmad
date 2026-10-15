
# In python generator is used to create iterator, so that they can be used in loops
# Generator are like function but:
    # Use yield statment to return a value.
    # Returns values on demand only.
    # Do not run all the way but remain paused till next call
# Huge memory and processing savings.

# def function_name()
# some processing
# yield statement

#may also be created through comprehension using()

def sum_upto(n):
    sum=0
    i=0
    while i <=n:
        yield sum
        i+=1
        sum+=i


cumulative_sum = sum_upto(20)
print(f"{type(cumulative_sum)}")
print("\nfirst result using while loop\n")
count=0
while count<10:
    print(f"The first sum of {count =} itegers is : {next(cumulative_sum)}")
    count+=1

# This is another way of using Generator function by using membership operator.
for i in cumulative_sum:
    print(f"{count =} {i =}")
    count+=1