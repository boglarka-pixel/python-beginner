import math

is_hot = False
is_cold = True

if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
    # akármennyi lehet itt
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("It's a lovely day")
print("this will be printed anyway")

# 1st exercise

house = 1000000

has_good_credit = False

if has_good_credit:
    down_payment = house * 0.1
else:
    down_payment = house * 0.2
print(f'{math.floor(down_payment)}')

