
### Playing with List

my_list = ["name 1", "Keren", "Shira", "Niv", "Daniel"]
# print the whole list
print(my_list)

# print some index in the list
print(my_list[2])

lucky_numbers = [5, 3, 39, 20, 22, 44, 55]
my_list.extend(lucky_numbers)
print("the new list after extending the list")
print(my_list)
print("the lengh of the list is " + str(len(my_list)))

# append to the list
lucky_numbers.append(666)
print("My luck numbers are: ")
print(lucky_numbers)

# Insert into the list to specific position:
my_list.insert(1, "name_2")
print("the updates list is: ")
print(my_list)

# to remove element from the list
my_list.remove(my_list[2])
print("item number 3 was remove from the list")
print(my_list)

# pop - remove the last item from the list
my_list.pop()
print("pop the lest item from the list (55)")
print(my_list)

# check the index of specific item in the list
print("the index of \"Shira\" in my list is: " )
print(my_list.index("Shira"))

# sort the list with sort, it is possible to reverse the list or copy
print("this is the sorted list")
my_list = ["name 1", "Keren", "Shira", "Niv", "Daniel"]
my_list.sort()
print(my_list)
