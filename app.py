full_name = 'John Smith'
age = 20
is_newPatient = True

# function
name = input('What is your name? ')
print('Hi ' + name)

weight_lbs = input('Weight (lbs): ')
weight_kg = input(int(weight_lbs) * 0.5)

favorite_color = input('What is your favorite color?')
print('My favoite color is ' + favorite_color)


birth_year = input('Birth year: ')

age = 2021 - int(birth_year)

print(age)
print(type(age))
print(type(birth_year))
