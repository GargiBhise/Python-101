# Tuples (Data in tuples wont change and the order of the data will not change)

# Tuples are immutable data structures in Python, meaning the elements within a tuple cannot be altered once the tuple is created. Additionally, the sequence of elements in a tuple remains constant, ensuring the order of data is preserved.


mytuple = tuple(('Dave', 42, True))

anothertuple = (1,4,5,6,7, 6,7,6,6)

print(mytuple)
print(type(anothertuple))

newList = list(mytuple)
newList.append('Joe')

newtuple = tuple(newList)
print(newtuple)

print(anothertuple.count(6))