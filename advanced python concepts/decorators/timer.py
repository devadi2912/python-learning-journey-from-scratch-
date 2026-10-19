"""this is a timer decorator function """

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"Time taken: {time.time() - start:.4f} seconds")
        return result
    return wrapper

@timer
def process_data():
    for i in range (20):
        print ("running..")
    time.sleep(2)

process_data()