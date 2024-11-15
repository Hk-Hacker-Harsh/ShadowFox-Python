'''You have a list of superheroes representing the Justice League.
justice_league = ["Superman" ,"Batman" ,"Wonder Woman" ,"Flash" ,"Aquaman" ,"Green Lantern"]'''

justice_league = ["Superman" ,"Batman" ,"Wonder Woman" ,"Flash" ,"Aquaman" ,"Green Lantern"]

#Perform the following tasks:
#Calculate the number of members in the Justice League
no_of_members=len(justice_league)
print(no_of_members)             #Ouput : 6

#Batman recruited Batgirl and Nightwing as new members. Add them to your list.
print()
new_members=["Batgirl", 'Nightwing']
justice_league.extend(new_members)
print(justice_league)             #Ouput: ['Superman', 'Batman', 'Wonder Woman', 'Flash', 'Aquaman', 'Green Lantern', 'Batgirl', 'Nightwing']

#Wonder Woman is now the leader of the Justice League. Move her to the beginning of the list.
print()
order=[2,0,1,3,4,5,6,7]
ordered_list=[]
for i in order:
    ordered_list.append(justice_league[i])

print(ordered_list)    #Output: ['Wonder Woman', 'Superman', 'Batman', 'Flash', 'Aquaman', 'Green Lantern', 'Batgirl', 'Nightwing']

# Aquaman and Flash are having conflicts, and you need to separate them. Choose either "Green Lantern" or "Superman" and move them in between Aquaman and Flash.
print()
order2=[1,2,3,4,0,5,6,7]
ordered_list2=[]
for i in order2:
    ordered_list2.append(justice_league[i])

print(ordered_list2)     #Output:['Batman', 'Wonder Woman', 'Flash', 'Aquaman', 'Superman', 'Green Lantern', 'Batgirl', 'Nightwing']

# The Justice League faced a crisis, and Superman decided to assemble a new team. Replace the existing list with the following new members: "Cyborg", "Shazam", "Hawkgirl", "MartianManhunter", "Green Arrow".
print()
justice_league=["Cyborg", "Shazam", "Hawkgirl", "MartianManhunter", "Green Arrow"]
print(justice_league)      #Output:['Cyborg', 'Shazam', 'Hawkgirl', 'MartianManhunter', 'Green Arrow']


# Sort the Justice League alphabetically. The hero at the 0th index will become the new leader.
print()
justice_league.sort()
print(justice_league)     #Output: ['Cyborg', 'Green Arrow', 'Hawkgirl', 'MartianManhunter', 'Shazam']

print("New Leader will be", justice_league[0])
#The next ledaer of justice league will be "Cyborg".