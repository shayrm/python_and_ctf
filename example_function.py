# play with functions
# define the function with 'def' and ident
# and then call the function

def say_hello(name):
    # the code that goes inside the function is idented
    print("hello " + name + " !!!")

enter_name = input("What is your name? ")
say_hello(enter_name)

# define function and return a value

def cube(number):
    return number * number * number

enter_num = input("please enter a number: ")
result = cube(int(enter_num))
print("The cube of the enter number is: " + str(result))
