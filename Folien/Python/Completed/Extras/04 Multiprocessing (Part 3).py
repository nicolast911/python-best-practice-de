# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Multiprocessing (Part 3)</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %%
def perform_computation(x):
    return 2 * x**2 + 1


# %%
if __name__ == "__main__":
    print("List comprehension:")
    print([perform_computation(x) for x in [1, 2, 3]])

# %%
if __name__ == "__main__":
    print("Map")
    print(list(map(perform_computation, [1, 2, 3])))

# %%
from multiprocessing import Pool

# %%
if __name__ == "__main__":
    print("Map with process pool")
    with Pool(processes=4) as p:
        print(p.map(perform_computation, [1, 2, 3]))
