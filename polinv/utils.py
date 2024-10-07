import time
import random
import threading

from polinv import logger

def random_sleep(min: int = 1, max: int = 5): return time.sleep(random.randint(min, max))

def create_thread_groups(list_: list, number_of_groups: int = 4):
    groups = []
    for _ in range(number_of_groups): groups.append([])
    n = 0
    for item in list_:
        groups[n].append(item)
        if n >= number_of_groups - 1: n = 0
        else: n += 1
    return groups

def make_threads(func, args: list[tuple]) -> list[threading.Thread]:
    threads = []
    for args_ in args: threads.append(threading.Thread(target=func, args=args_))
    return threads

def start_threads_group(threads: list[threading.Thread]):
    for t in threads: t.start()

def join_threads_group(threads: list[threading.Thread]):
    for t in threads: t.join()

class WaitFlag:

    def __init__(self) -> None: self.flag = True

    def reset(self): self.flag = True

    def wait(self):
        while self.flag: time.sleep(1)
    
    def stop(self): self.flag = False

# ===========
# DECORATORS 
# ===========

def unused(func):
    def wrapper(*args, **kwargs):
        logger.danger(f'Function {func.__name__} is marked as unused. It may be removed or changed in future releases.')
        return func(*args, **kwargs)
    return wrapper
