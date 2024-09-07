# 2) Odd Or Even:
# Ask the user for a number. Depending on whether the number is even or odd,
# print out an appropriate message to the user.
class OddOrEven:

    def __init__(self, number):
        self.number = number

    def calc(self):
        if self.number % 2 == 0:
            return print(f"{self.number} is an even number")
        else:
            return print(f"{self.number} is an odd number")



newNum = OddOrEven(int(input("Please enter a number: ")))
newNum.calc()