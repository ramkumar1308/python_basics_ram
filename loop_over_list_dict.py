""" LOOPING oVER LISTS"""

print("LOOPING OVER LISTS - Example1")
print("==============================")

numbers = [7, 9, 12, 54, 99]

print("This list contains: ")
for num in numbers:
  print(num)

# Add your loop below!
for num in numbers:
  print(num ** 2)

print()
print()

print("LOOPING OVER DICTIONARY - Example1")
print("===================================")
""" LOOPING OVER DICTIONARY"""
d = {'x': 9, 'y': 10, 'z': 20}
print ("The value is of key value x is " , d['x'])
for key in d:
#  print(key)
  if d[key] == 10:
    print("This dictionary has the value 10!")
  else:
      print("error,checking next key value")

print()
print()

print("LOOPING OVER DICTIONARY - Example2")
print("==================================")

prices = {"banana" : 4 , "carrot" : 2 , "apple" : 4}
stock = {"banana" : 100 , "carrot" : 50 , "apple" : 1000}

for i in prices:
  print("Name of the fruit : %s " % i)
  print("prices: %s" % prices[i])
  print("stock : %s" % stock[i])
