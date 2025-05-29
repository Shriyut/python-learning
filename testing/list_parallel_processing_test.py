import concurrent.futures
import time


def process_element(x):
    result = x * x
    timestamp = time.time()
    return x, result, timestamp


data = [1, 2, 3, 4, 5]

with concurrent.futures.ThreadPoolExecutor() as executor:
    results = list(executor.map(process_element, data))

print(results)
