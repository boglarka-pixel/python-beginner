import random

#a = random.randint(2, 8) # int(input('give me a number: '))


# if 9 < a < 100:
#     print('it\'s a "two-digit" number')


# if a % 2 == 0:
#     print('even')
# else:
#     print('odd')


# for i in range(a):
    # print(i+1)



# for i in range(1, a + 1):
#     print(i)

random.seed()
a = random.randint(1, 6)

while (a != 6):
    print('a = ' + str(a) +  'ez nem 6os, dobj újra')
    a = random.randint(1,6)
   
def print_nums(x):

  for i in range(x):

    print(i)

    return

print_nums(10)

for i in range(10):

  if not i % 2 == 0:

    print(i+1)



def func(x):

  res = 0

  for i in range(x):

     res += i

  return res



print(func(4))

letters = ['x', 'y', 'z']

letters.insert(1, 'w')

print(letters[2])


for i in range(10):

  if not i % 2 == 0:

    print(i+1)




list = [1, 1, 2, 3, 5, 8, 13]

print(list[list[4]])