#4

import time
def timer(func):
    def wrapper(*args,**kwargs):
        start_time = time.time()
        result = func(*args,**kwargs)
        end_time = time.time()
        time.sleep(3)
        print(f"Функція {func.__name__} виконалася за {end_time - start_time} секунд(и)")
        return result
    return wrapper

@timer
def function(a):
  for i in range(2,a):
    if a % i == 0:
      return("Число не є простим")
    else:
      return("Число є простим")
print(function(4))

