


""" It's also common to need to iterate over two lists at once. This is where the built-in zip function comes in handy.

zip will create pairs of elements when passed two lists, and will stop at the end of the shorter list.

zip can handle three or more lists as well! """

list_a = [3, 9, 17, 15, 19, 20, 50, 30, 46, 33]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]

for a,b in zip(list_a, list_b):
  if a > b:
    print (a)

""" for else """

names = ['ram','sudh','jean','romero','sarath']

for name in names:
  if name == "romero":
    print ("A name is " + str(name))
    break
  print ("A " + str(name))
else:
  print ("for loop ends and then else executed")