#3

def cache(func):
    cache_dictionary = {}
    def wrapper(*args,**kwargs):
        if args in cache_dictionary:
            return cache_dictionary[args]
        else:
            result = func(*args)
            cache_dictionary[args] = result
            return result , cache_dictionary
    return wrapper
@cache
def function(a,b):
    return a + b
print(function(4,4))