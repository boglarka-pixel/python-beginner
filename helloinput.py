def get_hello_message():
    name = input('What\'s your name? ')
    if not name:
        name = 'world'
    return f'hello {name}!'


print(get_hello_message())