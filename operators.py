# Operators are symbols used to perform operation son value.

# Arithmetic Operators

a = 3
b = 5

print(f"Addition - {a} + {b} = {a + b}")
print(f"Subtraction - {a} - {b} = {a - b}")
print(f"Multiplication - {a} * {b} = {a * b}")
print(f"Division - {b} / {a} = {b / a}")
print(f"Floor Division - {b} // {a} = {b // a}")
print(f"Modulus - {b} % {a} = {b % a}")
result = a ** b
print(f"Exponentiation - {a} ** {b} = {result}")
print(round(a/b))


# For a = 5, b = 3
''' 
Addition - 5 + 3 = 8
Subtraction - 5 - 3 = 2
Multiplication - 5 * 3 = 15
Division - 3 / 5 = 0.6
Floor Division - 3 // 5 = 0
Modulus - 3 % 5 = 3
Exponentiation - 5 ** 3 = 125 '''

# For a = 3, b = 5
'''Addition - 3 + 5 = 8
Subtraction - 3 - 5 = -2
Multiplication - 3 * 5 = 15
Division - 5 / 3 = 1.6666666666666667
Floor Division - 5 // 3 = 1
Modulus - 5 % 3 = 2
Exponentiation - 3 ** 5 = 243 
'''

# Boolean Operators:(and, or, not)
x = True
y = False
z = True

print(x and y)  # False
print (y and z) # False
print(x or y) #True
print(not z)  #False

