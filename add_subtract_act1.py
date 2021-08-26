import time


def add():
    global x
    for i in range(10000000):
        x += 1

def subtract():
    global x
    for i in range(10000000):
        x -= 1

if __name__ == "__main__":
    x = 0
    start = time.perf_counter()
    add()
    subtract()
    end = time.perf_counter()
    print('final x =' + str(x))
    print(f'elapsed time = {end - start}')
    
# 1. Run this code 5 times. Measure the elaplsed time and determine the average elapsed time.

# 2. Why does X always end up at 0?

# 3. In a sentence or two, describe how this program could be modified to be multithreated.