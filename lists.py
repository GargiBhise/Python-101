# Lists allow the storage of multiple elements within a single variable.
# In Python, lists are among four built-in data types designed for holding collections of data. The other three data types are Tuple, Set, and Dictionary, each having distinct characteristics and applications.

users = ['John', 'Smith', 'Joe', 'Dave']

data = ['John', 25, 'Computer Science', '3.5']

emtylist = []

# print("Dave" in data)

# print(users[-1]) # Last value in the list

# print(users.index('Dave'))

# print(data[0:4])
# print(data[-4:-1])

# print(len(users))

# users.append('Sarah') # ['John', 'Smith', 'Joe', 'Dave', 'Sarah']
# print(users)

# users += ['RObert', 'Mike'] # ['John', 'Smith', 'Joe', 'Dave', 'Sarah', 'RObert', 'Mike']
# print(users)

# users += 'joee' # ['John', 'Smith', 'Joe', 'Dave', 'Sarah', 'RObert', 'Mike', 'j', 'o', 'e', 'e']  # Adds each character as a separate element
# print(users)

# data.extend(['Mike', 'Jenny'])  # ['John', 25, 'Computer Science', '3.5', 'Mike', 'Jenny']
# print(data)

# # users.extend(data)
# # print(users)


# users.insert(0, 'Bob')
# print(users)

# users[2:2] = ['Eddie', 'Alex']
# print(users)

# users.remove('Bob')
# print(users)

# print(users.pop(4))
# print(users)

# del users[0]
# print(users)

# #del data # NameError: name 'data' is not defined

# data.clear() # it will empty the list and print []. It will not delete the list
# print(data)



### ********  SORt the LIST ********

# users.append('dave')
# users.sort()  # When its lowercase, it comes after the uppercase. ['Dave', 'Joe', 'John', 'Smith', 'dave']
# print(users)

# users.sort(key=str.lower)  # ['Dave', 'dave', 'Joe', 'John', 'Smith']
# print(users)

nums = [4, 42, 6, 7, 8, 97, 34]
nums.reverse()
print(nums)

nums.sort(reverse=True) # [97, 42, 34, 8, 7, 6, 4]
print(nums)

# type of list

print(type(data))