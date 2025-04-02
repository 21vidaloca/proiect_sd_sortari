import time

#import sorting algorithms
from sorts.merge_sort import merge_sort
from sorts.heap_sort import heap_sort
from sorts.insertion_sort import insertion_sort
from sorts.shell_sort import shell_sort

class Tester:
    def __init__(self):
        f_asc = open('./data/ascending.in', 'r')
        f_desc = open('./data/descending.in', 'r')
        f_rand = open('./data/random.in', 'r')

        self.input_files = [f_asc, f_desc, f_rand]

        self.function_name = {
            'Merge Sort': merge_sort,
            'Heap Sort': heap_sort,
            'Shell Sort': shell_sort,
            'Insertion Sort': insertion_sort
        }

    def isSorted(self, v: list) -> bool:
        for i in range(len(v)-1):
            if v[i] > v[i+1]:
                return False
        return True

    def measure_sorting(self, sorting_fun: callable, v: list) -> float:
        w = v.copy()
        init_time = time.perf_counter()
        sorting_fun(w)
        final_time = time.perf_counter()
        
        if not self.isSorted(w) or set(w) != set(v):
            print('Sorting failed!')
            return None

        elapsed = final_time - init_time
        return elapsed


    def test_sorting_algo_on_array(self, v:list):
        for name in self.function_name:
            elapsed = self.measure_sorting(self.function_name[name], v)
            print(f'{name.upper()}: {elapsed:.6f}')

    def test(self):
        for i in range(len(self.input_files)):
            file = self.input_files[i]
            print(f'----Testing first batch on file{i}----')
            idx = 1
            for line in file.readlines():
                print(f'--Test_{idx}--')

                line = line.split()

                v = []
                for nmb in line:
                    v.append(int(nmb))
                self.test_sorting_algo_on_array(v)

                idx += 1

if __name__ == '__main__':
    T = Tester()
    T.test()