# Write a program to determine the BMI Category based on user input
height=float(input("Enter Height in Meters: "))
weight=float(input("Enter Weight in Kilograms: "))

BMI = weight/height**2

print("Your BMI IS: ",BMI)

if BMI < 18.5:
    print("Underweight")
elif BMI >= 18.5 and BMI < 25:
    print("Normal")
elif BMI >= 25 and BMI < 30:
    print("Overweight")
elif BMI >= 30 : 
    print("Obesity")


#Write a program to determine which country a city belongs to. Given list of cities per country:
Australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
UAE = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

city=input("Enter City Name: ")

if city in Australia:
    print(city," is in Australia")

elif city in UAE:
    print(city, " is in UAE")

elif city in India:
    print(city, "is in India")

else:
    print("Unknown City!!")


# Write a program to check if two cities belong to the same country. Ask the user to enter two cities and print whether they belong to the same country or not.
first=input("Enter the First City: ")
second=input("Enter the Second City: ")

if first in Australia and second in Australia:
    print("Both cities are in Australia.")

elif first in UAE and second in UAE:
    print("Both cities are in UAE.")

elif first in India and second in India:
    print("Both cities are in India.")

else:
    print("They don't belong to the same country.")