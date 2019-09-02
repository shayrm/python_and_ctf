message = "this is message number one"
ch_name = "Jhone"
ch_age = 35

print("hello world, this is " + ch_name + ", how are you today?" )
print("hello to you too")
print("my age is " + str(ch_age))
print("my name is " + ch_name + " and my age is " + ch_name[1].upper() + " " + ch_name.upper() + "the name lenght is: " + str(len(ch_name)))
print("this is the index of 'n' in " + ch_name + " " + str(ch_name.index("n")))
print("this is the index of 'J' in " + ch_name + " " + str(ch_name.index("J")))
print ("will use the replace function --> so one will be replace with: " + message.replace("one", "two"))


### play with numbers
# it is possible to expend our math functions with import
from math import *

print(2 * (3 + 4))
print("print 10 mod 3 is: " + str((10 % 3)))

# and so 

### play with inputs

name = input("Please enter your name: ")
print("hello " + name + ", how are you?")

# calc adding two numbers:
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = int(num1) + int(num2)
print("adding " + num1 + " with " + num2 + " is: " + str(result))