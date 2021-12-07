print("hello world")

course = "Python's Course for Beginners"
course = 'Python for "Beginners'
another = course[:] #klonozza tulképp

print(course)
print(course[0]) # P lesz, első karakter
print(course[-2]) # hátulról a második
print(course[0:3]) # Pyt lesz, 3ig megy
print(course[0:]) #az egészet kiírja
print(course[1:]) # első karaktert leszámítva kiírja az összeset
print(course[:5]) #feltételezi a 0-át elsőre, ugyh Pytho

name = 'Jennifer'
print(name[1:-1]) # ennife /első és utsó karakter kilőve

course_multiline = ''''
Hi,
this is my
first email
to you
'''

print(course_multiline)

