#Create a variable named pi and store the value 22/7 in it.
pi = 22/7

#Now check the data type of this variable.
print(type(pi))    #Output: float


# Create a variable called for and assign it a value 4.
'''for = 4

print(for)''' #Output: SyntaxError: invalid syntax

# See what happens and find out the reason behind the behavior that you see.
'''It will give an invalid syntax error, because for is a keyword in python and we cannot use a keyword as variable.'''


#Store the principal amount, rate of interest, and time in different variables and then calculate the Simple Interest for 3 years. Formula: Simple Interest = P x R x T / 100
P = 100000
R = 10
T = 3

Simple_Interest=P*R*T/100

print(Simple_Interest)  #Output: 30000