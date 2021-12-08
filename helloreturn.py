
def hello():
    print("hello world!")
    def get_hello_message():
        return hello()
    def say_hello():
        print(get_hello_message())


hello()