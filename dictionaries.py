# set a dictionary with a key: value pair
# convert three latter month to full name

monthConvertion = {
    "Jan": "Jaunary",
    "Feb": "February",
    "Mar": "March",
    "Apr": "Appril"
}

print(monthConvertion["Jan"])
# can use the .get function, which could get a default value
# the default value could be set when the key is invalide
default_value = "Invalid option"
print(monthConvertion.get("Apr", default_value))
print(monthConvertion.get("888", default_value))
print(monthConvertion["Feb"]) 