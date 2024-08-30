# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Multiprocessing (Part 4)</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %%
def perform_computation(x):
    return x + 1


# %%
[perform_computation(x) for x in [1, 2, 3]]

# %%
list(map(perform_computation, [1, 2, 3]))

# %%
from multiprocessing.dummy import Pool

# %%
with Pool(processes=4) as pool:
    print(pool.map(perform_computation, range(1, 20), chunksize=5))

# %%
with Pool() as pool:
    res = pool.map_async(perform_computation, range(1, 20))
    print("Result object:", res)
    print("Result value: ", res.get(timeout=0.5))

# %%
with Pool() as pool:
    # Performs computation in arbitrary order
    print(list(pool.imap_unordered(perform_computation, range(1, 20), chunksize=5)))

# %%
with Pool() as pool:
    res = pool.apply_async(perform_computation, args=(10,))
    print("Result object:", res)
    print("Result value: ", res.get(timeout=1.0))

# %%
from operator import add

# %%
with Pool() as pool:
    print(pool.starmap(add, [[1, 2], [3, 4]]))

# %%
from time import sleep
from multiprocessing import TimeoutError

with Pool() as pool:
    res = pool.apply_async(sleep, args=(10.0,))
    try:
        print("Result:", res.get(timeout=0.5))
    except TimeoutError:
        print("Got a timeout.")


# %%
from time import sleep
from random import random


def simulate_processing_time(delta_time=0.1):
    sleep(random() * delta_time + delta_time)


# %%
from multiprocessing.dummy import Queue, Process
from queue import Empty


# %%
def producer(producer_id, q, num_items):
    print(f"Producer {producer_id} started...")
    for i in range(num_items):
        print(f"Producer {producer_id} produced item {producer_id}/{i}...")
        q.put(f"Item {producer_id}/{i}")
        simulate_processing_time(0.1)


# %%
def consumer(consumer_id, q, timeout=1.0):
    print(f"Consumer {consumer_id} started...")
    try:
        while True:
            item = q.get(block=True, timeout=timeout)
            print(f"Consumer {consumer_id} starting processing of item {item}...")
            simulate_processing_time(0.2)
            print(f"Consumer {consumer_id} done processing item {item}...")
    except Empty:
        print(f"Consumer {consumer_id} timed out...")


# %%
def run_producer_consumer_queue(num_items, num_producers=1, num_consumers=1):
    processes = []
    q = Queue()
    for i in range(num_consumers):
        processes.append(Process(target=consumer, args=(i + 1, q)))
    for i in range(num_producers):
        processes.append(Process(target=producer, args=(i + 1, q, num_items)))
    for process in processes:
        process.start()
    for process in processes:
        process.join()


# %%
run_producer_consumer_queue(4)

# %%
run_producer_consumer_queue(6, num_producers=1, num_consumers=3)

# %%
run_producer_consumer_queue(2, num_producers=4, num_consumers=3)
