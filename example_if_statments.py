# play with the 'if' statment 
is_male = True

# check if is_male is true or false
def check_male(cond, name):
    if cond:
        print("yes, you are a male, your name is: " + name)
    else:
         print("No, you are not male, your name is: " + name)

def check_name(name):
    if name == "Shay":
        return True
    else:
        return False


name = input("Please enter your name: \n")
result = check_name(name)
check_male(result, name)

