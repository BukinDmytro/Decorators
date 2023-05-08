#2 як додати функцію і число


def add(func):
    def wrapper(*args,**kwargs):
        print(24 + 100)
    return wrapper

@add
def function(a,b,c):
    return a * b * c
function(2,3,4)