print ("Gym Workout Generator")

print("Enter your name:")
x = input()
print("Hello, " + x)

print('What did you workout yesterday?')
print("1: Legs")
print("2: Back")
print("3: Chest")
print("4: Biceps/Triceps")
print("5: Shoulders")
print("6: Cardio")
inp = int(input("Enter a number: "))

if inp == 1:
    inp = "legs"
elif inp == 2:
    inp = "Back"
elif inp == 3:
    inp = "Chest"
elif inp == 4:
    inp = "Biceps/Triceps"
elif inp ==5:
    inp == "Shoulders"
elif inp == 6:
    inp == "Cardio"
else:
    print("Invalid input!")

import random

Names=('legs','Back','Chest','Biceps/Triceps','Shoulders','Cardio')

group="".join(random.choice(Names))

print('Workout Routine')
print(group)