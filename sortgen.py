import random

# Data set generator for sorting algorithms

dimensions = [50_000, 500_000]
bounds = [[-9_999, 9_999]]

#dimensions = [50, 500]
#bounds = [[-9_999, 9_999], [0, 9_999]]

# Ascending arrays
def generate_ascending():
    f_asc = open('./data/ascending.in', 'w')
    for dim in dimensions:
        for bound in bounds:
            gen_arr = []
            for _ in range(dim):
                val = random.randint(bound[0], bound[1])
                gen_arr.append(val)

            gen_arr.sort()

            for val in gen_arr:
                print(val, file=f_asc, end=' ')
            print(file = f_asc)

def generate_descending():
    f_desc = open('./data/descending.in', 'w')
    for dim in dimensions:
        for bound in bounds:
            gen_arr = []
            for _ in range(dim):
                val = random.randint(bound[0], bound[1])
                gen_arr.append(val)

            gen_arr.sort(reverse=True)

            for val in gen_arr:
                print(val, file=f_desc, end=' ')
            print(file = f_desc)


def generate_random():
    f_rand = open('./data/random.in', 'w')
    for dim in dimensions:
        for bound in bounds:
            gen_arr = []
            for _ in range(dim):
                val = random.randint(bound[0], bound[1])
                gen_arr.append(val)
            for val in gen_arr:
                print(val, file=f_rand, end=' ')
            print(file = f_rand)

if __name__ == '__main__':
    generate_ascending()
    generate_descending()
    generate_random()