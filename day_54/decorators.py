import time

def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        function()
    return wrapper_function

def say_hello():
    print("hello")

@delay_decorator
def say_world():
    print("world")

say_hello()
say_world()