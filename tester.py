import time

class Tester:
    def __init__(self, *data_paths):
        self.input_files = []
        for file in data_paths:
            self.input_files.append(open(file, 'r'))
 
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
            print('Sorting incorrect!')
            return None

        elapsed = final_time - init_time
        return elapsed

    def measure_sorting_algorithms(self, sorting_functions: dict, verbose: bool = True) -> dict:
        ans = {}

        for file in self.input_files:
            if verbose:
                print(f'Testing on file {file.name}')
            ans[file.name] = {}

            idx = 1
            for line in file.readlines():
                if verbose:
                    print(f'----Test{idx}----')
                ans[file.name][idx] = {}

                line = line.split()             
                v = []
                for nmb in line:
                    v.append(int(nmb))
                
                for sorting in sorting_functions:
                    if verbose:
                        print(f'{sorting}: ', end = "")

                    sorting_time = self.measure_sorting(sorting_functions[sorting], v)

                    if sorting_time != None:
                        if verbose:
                            print(f'{sorting_time:.6f}')
                        ans[file.name][idx][sorting] = sorting_time
                    else: 
                        if verbose:
                            print('Error')
                        ans[file.name][idx][sorting] = -1

                idx += 1
        return ans