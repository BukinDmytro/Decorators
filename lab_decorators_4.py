#4


def loger(func):
    def wrapper(*args , **kwargs):
        result = func(*args , **kwargs)
        print(f"Функція: {func.__name__} , Аргументи: {args} , Результат: {result}")
        return result
    return wrapper

@loger
def function(a,b):
    return a + b
print(function(4,4))