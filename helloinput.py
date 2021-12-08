# print('What\s your name? ')
name = input()


print("hello2")

def get_hello_msg(name):
    print('whats your name?')
    if len(name) == 0:
        print("hello world!")
    else:
        print('hello, ' + name)
        return 'hello! ' + name


# get_hello_msg(name)

def say_hello():
    return get_hello_msg(name)

say_hello()