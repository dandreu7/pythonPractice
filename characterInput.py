# 1) Character Input:
# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old.
# Note: for this exercise, the expectation is that you explicitly write out the year
# (and therefore be out of date the next year).

class characterInput:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Calculate when the user will turn 100 years old and return the year
    def turn100(self):
        newAge = 100 - self.age
        year100 = 2024 + newAge
        return year100



print("Please enter your name and age")
userName = input("Name: ")
userAge = input("Age: ")
userAge = int(userAge)
user = characterInput(userName, userAge)
print(f"{userName} you will turn 100 in the year {user.turn100()}")