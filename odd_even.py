a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
for i in range(10):
    if i % 2 == 0:
        print "%d is even " % i
    else:
        print "%d is odd " % i

for i in range(len(a)):
    print i
print len(a)