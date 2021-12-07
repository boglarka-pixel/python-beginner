# c-ben --> int szam = 10;

szam1 = 10
szam2 = 20

szam3 = 3.14

_szam = 45
_szam_ = 50


print(szam1 + szam2)

szam1 = 87

print(szam1 + szam2)

#expression
print('*' * 10)

price = 10
rating = 4.9
name = 'Mosh'
is_published = False
print(price)

first = 'John'
last = 'Smith'
message = first + ' [ ' + last  +' ] ' + 'is a coder'
msg = f'{first} [{last}] is a coder' #formatted string

print(message)
print(msg)

course = 'Python for Beginners'
print(len(course)) #20
upperCourse = course.upper()
print(upperCourse) #PYTHON FOR BEGINNERS
print(course.find('o')) #4, mert a 4. indexen van a kis o
print(course.find('Beginners')) #11, mert ott kezdődik
print(course.replace('Beginners', 'Absolute Beginners')) #Python for Absolute Beginners

print('Python' in course) #true
