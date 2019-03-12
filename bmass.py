weight = int(input("How much do you weigh (kg)? "))     # weight in kilograms
height = int(input("How tall are you (cm)? ")) / 100    # height in meters
bmi = weight / (height * height)     # body mass index
print("index: " + str(bmi))
if bmi > 30:
    print("Could lose some weight")
else:
    print("No big overweight")
if bmi < 17:
    print("Could gain some weight")
else:
    print("Not abnormally skinny")

# Task: specify some more ranges and give them the appropriate recommendations.

