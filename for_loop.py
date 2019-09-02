# play with for loop
friends = ["Keren", "Shira", "Niv", "Daniel"]

for friend in friends:
    print("my firend name is: " + friend)

print("-----------------------------")
print("another loop but with range")

for index in range(len(friends)):
    print("my firend name in index: " + str(index) + " is: " + friends[index])