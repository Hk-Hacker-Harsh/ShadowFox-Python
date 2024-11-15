'''Using a for loop, simulate rolling a sixsided die multiple times (at least 20
times).
Count and print the following statistics:
How many times you rolled a 6
How many times you rolled a 1
How many times you rolled two 6s in a row'''
print()
import random

times=int(input("Enter No. of Times to Roll Die: "))
rolls=[]
six=0
one=0
cons_six=0
previous_roll=None

for i in range(times):
    roll=random.randint(1,6)
    rolls.append(roll)
    if roll==6:
        six=six+1
    if roll==1:
        one=one+1
    if roll==6 and previous_roll==6:
        cons_six=cons_six+1

    previous_roll=roll

print("Total Rolls: ", times)
print("Total times rolled a Six: ", six)
print("Total times rolled a One: ", one)
print("Total times rolled two Consecutive Six: ", cons_six)

#Imagine you are doing a workout routine, and you have to complete 100 jumping jacks.
def jacks():
    total_jacks=100
    set=10
    completed=0

    while total_jacks > completed:
        conti=input(f"Do {set} Jumping Jacks? Y/N ")
        if conti.lower() == 'y':
            completed = completed + set
            response=input("Are you tired? Y/n ")
            if response.lower()=="y":
                choice=input(f"Do you want to skip remaining {total_jacks-completed} ? Y/N ")
                if  choice == 'y':
                    break
                elif choice == 'n':
                    print("Ramining Jumping Jacks: ", total_jacks-completed)
                else:
                    print('Invalid Response!')
                    break
            elif response.lower()=="n":
                print("Ramining Jumping Jacks: ", total_jacks-completed)

    if completed >= total_jacks:
        print("Congratulation!! You have completed ", completed, " Jumping Jacks")

    else:
        print("You have completed ", completed, " Jumping Jacks")

jacks()