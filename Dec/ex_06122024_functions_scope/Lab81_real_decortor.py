
def decorotor_1(func):

    def wrapper():
        print("decorotor1")
        func()
    return wrapper()

def decorotor_2(func):
    def wrapper():
        print("decorotor2")
        func()
    return wrapper()

@decorotor_2
@decorotor_1
def say_hello():
    print("say hello..")

say_hello()
