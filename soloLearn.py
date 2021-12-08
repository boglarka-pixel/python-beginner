
#function
def print_nums(x):

  for i in range(x):

    print(i)

    return

print_nums(10)


#for loop
for i in range(10):

  if not i % 2 == 0:

    print(i+1)


#function
def func(x):

  res = 0

  for i in range(x):

     res += i

  return res

print(func(4))


#insert function
letters = ['x', 'y', 'z']

letters.insert(1, 'w')

print(letters[2])


#range
for i in range(10):

  if not i % 2 == 0:

    print(i+1)



#beágyazott
list = [1, 1, 2, 3, 5, 8, 13]

print(list[list[4]]) # 8


#import more module
from math import pi, sqrt

