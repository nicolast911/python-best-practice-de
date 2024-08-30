# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Multiprocessing (Part 2)</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
# ## Synchronisieren von Prozessen

# %%
import multiprocessing


def say_hi(lock, name):
    from time import sleep
    from random import random

    sleep(random())
    with lock:
        print(f"Hello, {name}!")


# %%
from multiprocessing import Lock, Process

if __name__ == "__main__":
    _lock = Lock()
    processes = []
    for _name in ["Joe", "Jack", "Jill", "Jane", "Steve", "Sheila"]:
        processes.append(Process(target=say_hi, args=(_lock, _name)))
    for process in processes:
        print(f"Starting {process}.")
        process.start()
    for process in processes:
        print(f"Joining {process}.")
        process.join()
    print("Done.")


# %%
def server(barrier):
    barrier.wait()
    print("Server is serving")
    print("Server is still serving")
    print("Server is serving even more data")


# %%
def client(barrier):
    barrier.wait()
    print("Client is accessing server")
    print("Client is still accessing server")
    print("Client is taking really long to access the server")


# %%
from multiprocessing import Barrier, Process


def run_tasks(task1, task2):
    barrier = Barrier(2)
    print("Starting Processes...", flush=True)

    process1 = Process(target=task1, args=(barrier,))
    process1.start()

    process2 = Process(target=task2, args=(barrier,))
    process2.start()

    process1.join()
    process2.join()


# %%
if __name__ == "__main__":
    print("Server and client:")
    run_tasks(server, client)

# %%
if __name__ == "__main__":
    print("\nClient and Server:")
    run_tasks(client, server)
