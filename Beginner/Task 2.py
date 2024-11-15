# Write a function that takes two arguments, 145 and 'o' , and uses the `format` function to return a formatted string. Print the result. Try to identify the representation used.

def func(number, argument2):
    string=format(number,argument2)
    return string

number=int(input("Enter Number: "))
argument2=input("Enter character: ")
answer = func(number,argument2)
print(answer)      # Input: 145,"o"    #Output: 221
# Here, "o" represents octal representation of the number, if input is 100 and "o" then output will be 144.

''' In a village, there is a circular pond with a radius of 84 meters.
Calculate the area of the pond using the formula: Circle Area = πr^2.
(Use the value 3.14 for π) Bonus Question: If there is exactly 1.4 liters of water in a square meter, what is the total amount of water in the pond?
Print the answer without any decimal point in it.
Hint: Circle Area = π r^2 Water in the pond = Pond Area Water per Square Meter'''
print()

radius = 84
pi = 3.14

area = pi * (radius ** 2)
print("Radius of the Circular pond is ", int(area), " m^2.")     #Output: 22155 m^2

Water= area * 1.4                 #Output: 31018 Liter
print("Total water in the pond, if 1.4 li in every square meter.", int(Water), "Liter")


'''If you cross a 490 meter long street in 7 minutes, calculate your speed in meters per second.
Print the answer without any decimal point in it.
Hint: Speed = Distance / Time
'''
print()

Street = 490
time_taken_in_sec= 7 * 60

Speed = Street/time_taken_in_sec     #m/per min = meter/min

print('Speed will be ', int(Speed) , "meter/sec.")     #Output: 1 meter/sec (actual: 1.667 meter/sec)