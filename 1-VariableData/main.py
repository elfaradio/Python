
# Farhadul Islam
# CSE 56 IIUC


import keyword
print("Max Verstappen is the best F1 driver of all time!")
a = 28  # integer
b = 3.14  # float
s = "Farhad"  # string
c = 'a'  # character
d = True  # boolean
nn = None  # NoneType

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(nn))

# Identifiers

# Valid identifiers
my_variable = 10
_myVariable = 20
myVariable2 = 30

# Invalid identifiers
# 2myVariable = 40  # cannot start with a number
# my-variable = 50  # cannot contain hyphens
# my variable = 60  # cannot contain spaces
# my@variable = 70  # cannot contain special characters other than underscore

# All Keywords in Python
print("Python Keywords:")
for kw in keyword.kwlist:
    print(kw, end=' ')
print('\n')

# Operators in Python


operators = [
    "Arithmetic Operators: +, -, *, /, //, %, **",
    "Comparison Operators: ==, !=, >, <, >=, <=",
    "Logical Operators: and, or, not",
    "Bitwise Operators: &, |, ^, ~, <<, >>",
    "Assignment Operators: =, +=, -=, *=, /=, //=, %=, **=",
    "Identity Operators: is, is not",
    "Membership Operators: in, not in"

]

x = 2**3  # exponentiation
y = 2*3  # multiplication

# Type Conversion

a = 2
b = 3.5
print(a + b)  # implicit conversion (int to float)
# print("a" + 2)  # TypeError: cannot concatenate str and int
print("a" + str(2))  # explicit conversion (int to str) type casting

# Type Casting


float_num = 3.14
int_num = int(float_num)  # converting float to integer
print(int_num)  # Output: 3

# Input and Output
age = int(input("Enter your age: "))
print(age)
name = input("Enter your name: ")
print(type(name))  # type of name is str..... always str hoi

temp = float(input("Enter temperature in Celsius: "))
temp_fahrenheit = (temp * 9/5) + 32
print(temp_fahrenheit)

farhad = 2

# System 2
