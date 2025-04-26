import numpy as np

def generate_random_array(size):
    return np.random.randint(0, 10000, size, dtype=int)

def generate_increasing_array(size):
    return np.arange(size)

sizes = [2**x for x in range(2, 20)]

for size in sizes:
    random_array = generate_random_array(size)
    increasing_array = generate_increasing_array(size)

    np.savetxt(f'benchmark/random_array_{size:08d}.txt', np.insert(random_array, 0, size), fmt='%d', newline=' ')
    with open(f'benchmark/random_array_{size:08d}.txt', 'a') as file:
        file.write('\nIncreasing\nFindminmax\nPrint\nRebalance\nExit')

    np.savetxt(f'benchmark/increasing_array_{size:08d}.txt', np.insert(increasing_array, 0, size), fmt='%d', newline=' ')
    with open(f'benchmark/increasing_array_{size:08d}.txt', 'a') as file:
        file.write('\nIncreasing\nFindminmax\nPrint\nRebalance\nExit')

print("Arrays have been generated and saved to files.")