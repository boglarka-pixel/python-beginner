#fahrenheit converter
celsius = int(input("give a number: "))

def conv(c):
    
    fahrenheit = c * 9 / 5 + 32

    return fahrenheit

fahrenheit = conv(celsius)
print(fahrenheit)