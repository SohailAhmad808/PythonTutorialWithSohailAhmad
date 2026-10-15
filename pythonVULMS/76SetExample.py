students = ["Sohail","Ali","Ahmad","Tariq","Sana","Abida","Ayesha","Hina","irfan","Shoaib","Khan"]
Mess_Members = ["Sohail","Sana","Hina","Shoaib"]
Gym_Members = ["Sohail","Ali","Ahmad","Tariq","Sana"]

print(f"\n {students =} \n {Mess_Members =} \n {Gym_Members =} \n")

# Find all members who are Mess members and Gym members

#Mess_Members_and_Gym_Member = set(students).intersection(Mess_Members,Gym_Members)
Mess_Members_and_Gym_Member = set(Mess_Members).intersection(Gym_Members)
#Mess_Members_and_Gym_Member = set(Mess_Members) & set(Gym_Members)
print(f"{Mess_Members_and_Gym_Member = }\n")



# Find all students who are not Mess member nor Gym member

Not_Mess_Gym = set(students).difference(Mess_Members,Gym_Members)
print(f"{Not_Mess_Gym =} \n")

# Find all students who are Mess member and not gym member

Mess_Not_Gym = set(Mess_Members) - set(Gym_Members)
# Mess_Not_Gym = set(Mess_Members).difference(Gym_Members)
# Mess_Not_Gym = set(students).intersection(Mess_Members).difference(Gym_Members)
print(f"{Mess_Not_Gym =}")


