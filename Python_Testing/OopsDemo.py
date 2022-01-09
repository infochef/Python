# Classes are user defined blueprint or prototype
# Sum, Multiplication, Addition, Constant
# Methods, Class, Variables, instance variable, constructor etc
# self keyword is mandatory for calling variable names into method
# instance and class variable have whole different purpose
# constructor name should be __init__
# new keyword is not required when you create object

class Calculator:
    num = 100  # Class Variables

    # Default Constructor
    def __init__(self, a, b):  # Syntax to call constructor in python
        self.firstNumber = a  # Instance variable
        self.secondNumber = b
        print('I am called automatically when object is created')

    # if statement starting with "def" is inside class than it is treated as Method and if it is outside the class
    # than it is treated as function. Functions are same as methods
    def getData(self):  # Syntax to create methods in python.
        print('I am now executing as method in class')

    def summation(self):
        return self.firstNumber + self.secondNumber + Calculator.num


obj = Calculator(2, 3)  # Syntax to create objects in python
obj.getData()
print(obj.num)
print(obj.summation())

obj1 = Calculator(4, 5)  # Syntax to create objects in python
obj1.getData()
print(obj1.num)
print(obj1.summation())
