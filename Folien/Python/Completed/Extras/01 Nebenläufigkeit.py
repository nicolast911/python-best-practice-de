# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Nebenläufigkeit</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# # Nebenläufigkeit
#
# Definition von Leslie Lamport (in *Time, Clocks, and the Ordering of Events*, 1976):
#
# <blockquote>
# Zwei Ereignisse sind *nebenläufig*, wenn keines das andere kausal beeinflussen kann.
# </blockquote>
#
# D.h., nebenläufige Ereignisse können in beliebiger Reihenfolge ausgeführt werden.

# %% [markdown]
#
# ## Wann ist Nebenläufigkeit sinnvoll?
#
# - Zum Verringern von Latenz und Erhöhen von Durchsatz
# - Zum Ausnutzen mehrerer Prozessoren/Rechenkerne
# - Zur Durchführung von Hintergrundaktivitäten

# %% [markdown]
#
# Wie kann Nebenläufigkeit realisiert werden?
#
# - Interleaving (Zeitscheiben)
# - Asynchrone Verarbeitung (Sonderfall von Interleaving)
# - Parallele Verarbeitung

# %% [markdown]
#
# Wie kann Nebenläufigkeit realisiert werden?
#
# - Interleaving (Zeitscheiben): Coroutines, ...
# - Asynchrone Verarbeitung: Event-Loop, Async, ...
# - Parallele Verarbeitung: Threads, Processes, Futures, ...
#
# Aber: In Python bewirken Threads in der Regel eher ein Interleaving als echte
# parallele Verarbeitung!

# %% [markdown]
#
# ## Threads
#
# Threads werden durch die Klasse `threading.Thread` gekapselt:
#
# - `target` Initarg bestimmt die Funktion, die ausgeführt wird
# - `Thread.start()` startet den Thread
# - `Thread.

# %% [markdown]
#
# ### Hintergrundverarbeitung

# %%
def wait_and_print():
    from time import sleep

    print("Starting...")
    sleep(10)
    print("Stopping...")


# %%
from threading import Thread

my_thread = Thread(target=wait_and_print)

# %%
my_thread.start()

# %%
print("Hello, from main Thread!")
print("My thread is alive:", my_thread.is_alive())

# %%
my_thread.join()
print("This should run only after my_thread is done.")
print("My thread is alive:", my_thread.is_alive())

# %% [markdown]
#
# ### Verringern von Latenz und Erhöhen von Durchsatz

# %%
from time import sleep
from random import random
import timeit


def simulate_processing_time(delta_time=0.1):
    sleep(random() * delta_time + delta_time)


# %%
def process_request(data, results, delta_time=0.1):
    simulate_processing_time(delta_time)
    # Is this correct?
    results.append(f"->{data}")


# %%
def process_requests_sequentially(num_requests):
    results = []
    for i in range(num_requests):
        process_request(i, results)
    return results


# %%
process_requests_sequentially(5)

# %%
timeit.timeit(lambda: process_requests_sequentially(5), globals=globals(), number=10)

# %%
timeit.timeit(lambda: process_requests_sequentially(10), globals=globals(), number=10)

# %%
from threading import Thread


def process_requests_concurrently(num_requests):
    results = []
    threads = []
    for i in range(num_requests):
        thread = Thread(target=lambda: process_request(i, results))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    return results


# %%
process_requests_concurrently(5)

# %%
timeit.timeit(lambda: process_requests_concurrently(5), globals=globals(), number=10)

# %%
timeit.timeit(lambda: process_requests_concurrently(10), globals=globals(), number=10)

# %%
timeit.timeit(lambda: process_requests_concurrently(100), globals=globals(), number=10)


# %%
class MyThread(Thread):
    # Note `run()`is overridden, not `start()`!
    def run(self) -> None:
        # noinspection PyUnresolvedReferences
        process_request(*self._args, **self._kwargs)


# %%
def process_requests_concurrently_2(num_requests):
    results = []
    threads = [MyThread(args=(i, results)) for i in range(num_requests)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    return results


# %%
process_requests_concurrently_2(5)

# %%
timeit.timeit(lambda: process_requests_concurrently_2(5), globals=globals(), number=10)

# %%
timeit.timeit(lambda: process_requests_concurrently_2(10), globals=globals(), number=10)

# %%
timeit.timeit(
    lambda: process_requests_concurrently_2(100), globals=globals(), number=10
)


# %% [markdown]
#
# ### Mehrere Threads und das GIL

# %%
def perform_computation(data, results, num_iterations=1_000_000):
    result = 0
    for i in range(num_iterations):
        result += 1
    results.append(f"->{data}: {result}")


# %%
def perform_computations_sequentially(num_requests):
    results = []
    for i in range(num_requests):
        perform_computation(i, results)
    return results


# %%
perform_computations_sequentially(5)

# %%
timeit.timeit(
    lambda: perform_computations_sequentially(5), globals=globals(), number=10
)

# %%
timeit.timeit(
    lambda: perform_computations_sequentially(10), globals=globals(), number=10
)


# %%
def perform_computations_concurrently(num_requests):
    results = []
    threads = []
    for i in range(num_requests):
        thread = Thread(target=lambda: perform_computation(i, results))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    return results


# %%
perform_computations_concurrently(5)

# %%
timeit.timeit(
    lambda: perform_computations_concurrently(5), globals=globals(), number=10
)

# %%
timeit.timeit(
    lambda: perform_computations_concurrently(10), globals=globals(), number=10
)


# %% [markdown]
#
# In Python wird immer nur *ein* Python Thread ausgeführt, alle anderen Threads
# existieren zwar, warten aber "bis sie an der Reihe sind". Daher bringt Multithreading
# nur dann Vorteile, wenn z.B. auf Ein/Ausgabe-Operationen gewartet wird, nicht wenn
# mehrere Berechnungen beschleunigt werden sollen!

# %% [markdown]
# ## Workshop
#
# - Notebook `workshop_410_concurrency`
# - Abschnitt "Parallele Requests"

# %% [markdown]
#
# ### Synchronisieren von Threads
#
# Die nebenläufige Programmierung führt zu Problemen, die es in sequentiellen Programmen
# nicht gibt:

# %%
def add_ones():
    global _result
    for i in range(10_000):
        tmp = _result + 1
        # if random() > 0.99:
        #     simulate_processing_time(0)
        _result = tmp


# %%
from threading import Thread

_result = 0
_threads = [Thread(target=add_ones) for _ in range(100)]
for _thread in _threads:
    _thread.start()
for _thread in _threads:
    _thread.join()
print(f"\n_result = {_result}")


# %%
def append_one():
    global _result_list
    for i in range(100_000):
        _result_list.append(1)


# %%
from threading import Thread

_result_list = []
_threads = [Thread(target=append_one) for _ in range(100)]
for _thread in _threads:
    _thread.start()
for _thread in _threads:
    _thread.join()
print(f"\nLength of _result_list: {len(_result_list)}")

# %% [markdown]
#
# #### Barrieren (Barriers)
#
# Mit Barrieren (Barriers) kann eine fixe Anzahl an Threads synchronisiert werden:

# %%
from threading import Barrier, Thread

_barrier = Barrier(2, timeout=5)


# %%
def server1():
    print("Server is starting!")
    simulate_processing_time(1.0)
    print("Server started up!")
    _barrier.wait()
    print("Server is serving!")


# %%
def client1():
    print("Client is starting!")
    _barrier.wait()
    print("Client is accessing server!")


# %%
_c = Thread(target=client1)
_c.start()

# %%
_s = Thread(target=server1)
_s.start()

# %%
_c.join()
_s.join()

# %%
_s = Thread(target=server1)
_s.start()

# %%
_c = Thread(target=client1)
_c.start()

# %%
_s.join()
_c.join()

# %% [markdown]
#
# #### Locks
#
# Locks sind ein low-level Synchronisierungsmechanismus, mit dem man erzwingen kann,
# dass nur ein Thread eine Resource nutzt:

# %%
from threading import Lock, Thread

_result_lock = Lock()


# %%
def add_ones_locked():
    global _result
    for i in range(10_000):
        with _result_lock:
            tmp = _result + 1
            if random() > 0.99:
                simulate_processing_time(0)
            _result = tmp


# %%
_result = 0
_threads = [Thread(target=add_ones_locked) for _ in range(100)]
for _thread in _threads:
    _thread.start()
for _thread in _threads:
    _thread.join()
print(f"\n_result = {_result}")


# %%
def server2():
    _barrier.wait()
    print("Server is serving")
    print("Server is still serving")
    print("Server is serving even more data")


# %%
def client2():
    _barrier.wait()
    print("Client is accessing server")
    print("Client is still accessing server")
    print("Client is taking really long to access the server")


# %%
def run_tasks(task1, task2):
    thread1 = Thread(target=task2)
    thread1.start()

    thread2 = Thread(target=task1)
    thread2.start()

    thread1.join()
    thread2.join()


# %%
run_tasks(server2, client2)

# %%
from threading import Lock

_print_lock = Lock()


# %%
def server3():
    _barrier.wait()
    try:
        _print_lock.acquire()
        simulate_processing_time()
        print("Server is serving")
        print("Server is still serving")
        print("Server is serving even more data")
    finally:
        _print_lock.release()


# %%
def client3():
    _barrier.wait()
    if _print_lock.acquire(blocking=False):
        print("Client is accessing server")
        print("Client is still accessing server")
        print("Client is taking really long to access the server")
        _print_lock.release()
    else:
        print("WARNING: Could not acquire lock!!!")


# %%
run_tasks(server3, client3)

# %%
run_tasks(client3, server3)


# %%
def server4():
    _barrier.wait()
    with _print_lock:
        print("Server is serving")
        print("Server is still serving")
        print("Server is serving even more data")


# %%
def client4():
    _barrier.wait()
    with _print_lock:
        print("Client is accessing server")
        print("Client is still accessing server")
        print("Client is taking really long to access the server")


# %%
run_tasks(server4, client4)

# %%
run_tasks(client4, server4)

# %% [markdown]
#
# #### Condition Variables
#
# Condition Variables sind ein Synchronisierungsmechanismus, der auf Locks basiert, aber
# einen zusätzlichen Mechanismus zur Koordination von Threads bietet: `notify()` (und
# `notify_all()`):
#
# Typischerweise verwendet man Condition Variables, wenn sich mehrere Threads einen
# gemeinsamen Zustand teilen und sowohl lesend als auch schreibend darauf zugreifen
# müssen:
#
# - Threads, die den Zustand lesen wollen, verwenden `wait()` und warten damit bis der
#   gewünschte Zustand erreicht ist
# - Threads, die den Zustand schreiben, verwenden `notify()` oder `notify_all()` um
#   eventuell wartende Threads über die Änderung zu benachrichtigen

# %%
from threading import Condition, Thread


# %%
def consumer(consumer_id, cv, items):
    print(f"Consumer {consumer_id} started...", flush=True)
    with cv:
        print(f"Consumer {consumer_id} waiting...", flush=True)
        wait_succeeded = True
        while True:
            while not items and wait_succeeded:
                wait_succeeded = cv.wait(timeout=1.0)
            if not wait_succeeded:
                print(f"Consumer {consumer_id} timed out...", flush=True)
                break
            print(f"Consumer {consumer_id} starts consuming...", flush=True)
            item = items.pop()
            simulate_processing_time(0.1)
            print(f"Consumer {consumer_id} ends consuming item {item}...", flush=True)


# %%
def producer(producer_id, cv, num_items, items):
    from random import randint

    print(f"Producer {producer_id} started...", flush=True)
    for _ in range(num_items):
        with cv:
            item = randint(100, 999)
            print(f"Producer {producer_id} is producing item {item}", flush=True)
            items.append(item)
            cv.notify()
            simulate_processing_time(0.05)


# %%
def run_producer_consumer(num_items, num_producers=1, num_consumers=1):
    threads = []
    items = []
    cv = Condition()
    for i in range(num_consumers):
        threads.append(Thread(target=consumer, args=(i + 1, cv, items)))
    for i in range(num_producers):
        threads.append(Thread(target=producer, args=(i + 1, cv, num_items, items)))
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()


# %%
run_producer_consumer(2)

# %%
run_producer_consumer(6, num_producers=1, num_consumers=3)

# %%
run_producer_consumer(4, num_producers=3, num_consumers=4)


# %%
from queue import Queue, Empty


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
from threading import Thread


def run_producer_consumer_queue(num_items, num_producers=1, num_consumers=1):
    processes = []
    q = Queue()
    for i in range(num_consumers):
        processes.append(Thread(target=consumer, args=(i + 1, q)))
    for i in range(num_producers):
        processes.append(Thread(target=producer, args=(i + 1, q, num_items)))
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
