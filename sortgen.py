import random
import os

class SortGen:
    def __init__(self, output_folder='./data'):
        self.output_folder = output_folder
        os.makedirs(output_folder, exist_ok=True)
        self.bounds = [(0, 10**6)]  # You can adjust the bounds as needed
        self.sizes = [1000, 10_000, 100_000, 500_000]  # 4 arrays of different sizes

    def _write_to_file(self, filename, arrays):
        with open(os.path.join(self.output_folder, filename), 'w') as f:
            for arr in arrays:
                print(' '.join(map(str, arr)), file=f)
    
    def generate_random(self):
        arrays = []
        for size in self.sizes:
            for bound in self.bounds:
                arr = [random.randint(bound[0], bound[1]) for _ in range(size)]
                arrays.append(arr)
        self._write_to_file('random.in', arrays)

    def generate_ascending(self):
        arrays = []
        for size in self.sizes:
            for bound in self.bounds:
                arr = [random.randint(bound[0], bound[1]) for _ in range(size)]
                arr.sort()
                arrays.append(arr)
        self._write_to_file('ascending.in', arrays)

    def generate_descending(self):
        arrays = []
        for size in self.sizes:
            for bound in self.bounds:
                arr = [random.randint(bound[0], bound[1]) for _ in range(size)]
                arr.sort(reverse=True)
                arrays.append(arr)
        self._write_to_file('descending.in', arrays)

    def generate_nearly_sorted(self, swaps=10):
        arrays = []
        for size in self.sizes:
            arr = list(range(size))
            for _ in range(swaps):
                i, j = random.randint(0, size-1), random.randint(0, size-1)
                arr[i], arr[j] = arr[j], arr[i]
            arrays.append(arr)
        self._write_to_file('nearly_sorted.in', arrays)

    def generate_few_unique(self, unique_count=5):
        arrays = []
        for size in self.sizes:
            unique_values = [random.randint(0, 100) for _ in range(unique_count)]
            arr = [random.choice(unique_values) for _ in range(size)]
            arrays.append(arr)
        self._write_to_file('few_unique.in', arrays)

    def generate_alternating_high_low(self):
        arrays = []
        for size in self.sizes:
            arr = []
            for i in range(size):
                arr.append(size - i if i % 2 == 0 else i)
            arrays.append(arr)
        self._write_to_file('alternating_high_low.in', arrays)

    def generate_large_numbers(self):
        arrays = []
        for size in self.sizes:
            arr = [random.randint(10**6, 10**9) for _ in range(size)]
            arrays.append(arr)
        self._write_to_file('large_numbers.in', arrays)

    def generate_small_range(self):
        arrays = []
        for size in self.sizes:
            arr = [random.randint(0, 10) for _ in range(size)]
            arrays.append(arr)
        self._write_to_file('small_range.in', arrays)

    def generate_chunk_reversed(self, chunk_size=50):
        arrays = []
        for size in self.sizes:
            arr = list(range(size))
            for i in range(0, size, chunk_size):
                arr[i:i+chunk_size] = reversed(arr[i:i+chunk_size])
            arrays.append(arr)
        self._write_to_file('chunk_reversed.in', arrays)


if __name__ == '__main__':
    sg = SortGen()
    sg.generate_ascending()
    sg.generate_descending()
    sg.generate_random()
    sg.generate_alternating_high_low()
    sg.generate_chunk_reversed()
    sg.generate_few_unique()
    sg.generate_large_numbers()
    sg.generate_nearly_sorted()
    sg.generate_small_range()