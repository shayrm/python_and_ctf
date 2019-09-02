# basic of reading from file
# we will use the sample file called my_list.txt
'''
Unicode String
    u"Unicode", u'Unicode', u"""Unicode""", etc. 
    Unicode is the Universal Character Set; 
    each character requires from 1 to 4 bytes of storage. 
    ASCII is a single-byte character set; 
    each of the 256 ASCII characters requires a single byte of storage. Unicode permits any character in any of the languages in common use around the world.

Raw String
    r"raw\nstring", r'raw\nstring', etc. 
    The backslash characters (\) are not interpreted by Python, but are left as is. 
    This is handy for Windows files names that contain \'s. 
    It is also handy for regular expressions that make extensive use of backslashes. Example: 
    '\n' is a one-character string with a non-printing newline; r'\n' is a two-character string.
'''
# print some unicode strings:
print("Priting some Unicade strings")
print("=======================")
print(u'\u65e5\u672c' + " and " + u'\U0001F4A9')
print("=======================")

input("press enter to continue...")
# open the file with read or write (r, w, or r+) or append (a)
my_list_file = open("my_list.txt", "r")

#check if the file can be readable (answer will be True or False)

my_list_file = open("my_list.txt", "r")
print("read the one line...")
print("=======================")
print(my_list_file.readline() + "\n")

# since we read the first line, the "reader" will continue from the last place in the file
print(my_list_file.readable())
print("read the whole file...")
print("=======================")
print(my_list_file.read() + "\n")



# It is inportent to close the file when done reading or changing the file
my_list_file.close()

my_list_file = open("my_list.txt", "r")
index = 1

for line in my_list_file.readlines():
    print("Line " + str(index) + ":: \n" + line)
    index += 1

# It is inportent to close the file when done reading or changing the file
my_list_file.close()

my_list_file = open("my_list.txt", "a")
# make sure you add the python escape characters before so the adding will be on a new line
# more information could be found here:
# https://docs.python.org/2/reference/lexical_analysis.html#string-literals
my_list_file.write("\nAdding a notehr line to the file - by python script")

my_list_file.close()

