#1

import time
def time(func):
    def wrapper(*args , **kwargs):
        returning = func(*args , **kwargs)
        for i in range(1,4):
            if 0 < i < 4:
                time.sleep(2)
                print(returning)
        return returning
    return wrapper
@time
def function(a):
    return a
function("LIGHT WEIGHT!!!")