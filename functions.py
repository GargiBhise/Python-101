# reusable blocks of code.

def hello_world():
  print("Hello World!!")

hello_world()

# Naming conventions: all lowercase, separate by _


def sum(num1=0, num2=0):
  if (type(num1) is not int or type(num2) is not int):
    return 
  return num1 + num2

total = sum(7,2)
print(total)


def multiple_items(*args):
  print(args)
  print(type(args))

multiple_items("Dave", "Sarah")


def mult_named_items(**kwargs):   #keyword arguments
  print(kwargs)
  print(type(kwargs))

mult_named_items(first = "Dave", last = "Smith")
