first = 'Dave'

# print(first)
# print(first.lower())
# print(first.upper())


# multiline = '''
# Hello,
# How are you?

# have a great weekend!!!!!!!
# ! '''

# print(multiline.title())
# print(multiline.replace("great", "good"))
# print(multiline)
# print(len(multiline))

# multiline += "                                        "
# multiline = "                                        " + multiline

# print(len(multiline))


# # To remove white space

# print(len(multiline.strip()))
# print(len(multiline.lstrip()))  # left side space
# print(len(multiline.rstrip()))    # Right side space


# Build a menu

# title = "menu".upper()
# print(title.center(20, '*'))

# print("Coffee".ljust(16, ".") + "$1".rjust(4)) 
# print("Muffin".ljust(16, ".") + "$2".rjust(4))  
# print("Cheesecake".ljust(16, ".") + "$1".rjust(4))  # Cheesecake......  $1

# print('***********************************')


# String index values
 #first = "Dave"
# print(first[1])
# print(first[-1])
# print(first[1:-1])
# print(first[1:])

# # Some methods return boolean data

# print(first.startswith('d')) # This is case sensitive
# print(first.endswith('z'))



# Boolean Data type

# myvalue = True
# x = bool(False)
# print(type(x))
# print(isinstance(myvalue, bool))  #  checks if an object is an instance of a specified class or a tuple of classes.


# Integer type

# price = 100
# best_price = int(80)
# print(type(price))
# print(isinstance(best_price, int))



# float type
# gpa = 3.28
# y = float(1.14)
# print(type(gpa))


# Complex type
# comp_value = 5 + 3j
# print(type(comp_value))
# print(comp_value.real)
# print(comp_value.imag)


# Built-in functions for numbers
# gpa = 3.28

# print(abs(gpa))
# print(abs(gpa * -1))
# print(round(gpa)) # round to the nearest integer
# print(round(gpa, 1)) # round to the nearest decimal place we specify

# import math

# print(math.pi)
# print(math.sqrt(64))
# print(math.ceil(gpa))
# print(math.floor(gpa))



# Casting a string to a number

# zipcode = "92010"
# print(type(zipcode))
# ZIp_code = int(zipcode)
# print(type(ZIp_code))


# # Error if you attempt to cast a string a string to number if its incorrect data
# zip_value = "New York"
# ZIp_code = int(zip_value)
# print(type(ZIp_code))   # ValueError: invalid literal for int() with base 10: 'New York'