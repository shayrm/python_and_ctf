# Create a program that asks the user to enter their name and their age. 
# Print out a message addressed to them that tells them the year that they will turn 100 years old.

#import datetime
import datetime

def calculate_year(age):
    #get the current year
    current_year = datetime.datetime.now()
    years_to_100 = 100 - age
    return (current_year.year + years_to_100)


name = input("Please input your name: \n")
age = int(input("Please specify your age: \n"))
year_at_100 = calculate_year(age)
print("Hello " + name + ", you will turn 100 on the year: " + str(year_at_100))