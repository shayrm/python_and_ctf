# how to handle exception 
number = int(input("Enter a Number: "))
print(number)


try:
    number = int(input("Enter a Number: "))
    print(number)
except:
    print("invalid input, please enter a number!")


# it is possible to do try and "except" differnt condition
# it is good to get the specific error!
try:
    number = int(input("Enter a Number: "))
    print(number)

except ValueError as err:
    print("ValueError :: invalid input, please enter a number!")
    print("The error is: ")
    print("=================")
    print(err)
    print("=================")
except TypeError as err:
    print("TypeError:: invalid input, please enter a number!")
    #print("The error is: " + err)
