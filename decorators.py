from datetime import datetime

def execution_time(fun):
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        fun(*args, **kwargs)
        final_time = datetime.now()
        tim_elapsed = final_time - initial_time
        print(f'pasaron {tim_elapsed.total_seconds()} segundos')
    return wrapper

@execution_time
def random_func():
    for _ in range(1, 100000000):
        pass

@execution_time
def suma(a:int, b:int):
    return a+b


suma(5,5)