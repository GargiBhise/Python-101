# # Used to store data values that are in key value pair.

# band = {
#   "name" : "Justin",
#   "age" : 30,
#   "address" : "123 fgkjh"
# }

# band2 = dict(name = "Geo", age = 40, address = "2143 kjgh")

# print(band)
# print(band2)
# print(type(band))
# print(len(band2))

# # Access items

# print(band["age"])
# print(band.get("age"))

# print(band2.keys())
# print(band2.values())

# # list all key/value pairs
# print(band.items())

# # verify if a key exists

# print("name" in band)
# print("fname" in band)

# # change values
# band["name"] = "Jenny"
# band.update({"age": 45})
# print(band)

# #Remove items
# print(band2.pop("age")) 
# print(band2)

# band["name"] = "Justin"
# print(band)

# print(band.popitem()) # removes last added item
# print(band)

# # Delete and clear
# band["name"] = "Justin"
# del band["name"]
# print(band)


# # delete the dictionary
# band2.clear()
# print(band2)


# copy dictionary

classroom = {
  "Furniture" : "Desk",
  "Stationary" : "Pen",
  "Stationary" : "Pencil",
  "gadgets" : "Laptop",
  "Books" : "Maths"
}

# classref = classroom  # creates a reference to the original dictionary
# print("Bad Copy!!!")
# print(classref)
# print(classroom)

# classref["time"] = 10
# print(classref)

# classroomcopy = classroom.copy()
# classroomcopy["time"] = 10
# print(classroom)
# print(classroomcopy)

# # or use the dict() constructor function

# classroom2 = dict(classroom)
# print(classroom2)


### Nested Dictionaries

member1 = {
  "name" : "Plant",
  "instrument" : "Guitar"
}

member2 = {
  "name" : "John",
  "instrument" : "Drums"
}

member3 = {
  "member1" : member1,
  "member2" : member2
}

print(member3)

print(member3["member1"]["name"])
