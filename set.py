# Sets in Python are unordered collections of unique elements. They are used when the presence of an item in a collection is more important than the order of items or how many times an item appears. Sets support mathematical operations like union, intersection, difference, and symmetric difference.

nums = { 1,2,3,4,5}

nums2 = set((5,6,7,8,0)
            )

print(nums)
print(nums2)
print(type(nums2))
print(len(nums2))

# No duplicates allowed

nums = {1,2,3,4,5,5,5}

print(nums)   #{1, 2, 3, 4, 5}

# True is a dupe of 1, false is a dupe of 0

nums = {1, True, False, 3, 4, 0} 
print(nums)   # {False, 1, 3, 4}

# check if a value is in a set

print(4 in nums)

# but you cannot refer to an element in the set with an index position or a key

#  Add a new elem to a set

nums.add(8)
print(nums)

# Add from one set to another

morenums = {6,7,8,9,23}
nums.update(morenums)
print(nums)

# You can use update with list, tuple, dictionaries tooo...

# Merge two sets

one = {1,2,3,4,5}
two = {6,7,8,9,10}

mynewset = one.union(two)
print(mynewset)

# Keep only duplicates
one = {1,8,9}
two = {6,7,8,9,10}

one.intersection_update(two)
print(one)  # {8, 9}


# Keep everything excepts duplicates

one = {1,8,9}
two = {6,7,8,9,10}

one.symmetric_difference_update(two)
print(one)