"""
CS566 - Programming Assignment 1
Hanxiong Shi
hanxiong@bu.edu
"""

import random
import time

print("\nCS566 - Programming Assignment 1")
print("Hanxiong Shi")
print("hanxiong@bu.edu\n")


def print_array(array, num):
    """
    Print the first n elements of an array
    """
    for i in range(0, num):
        print(array[i])


def read_integers(filename):
    """
    Parse input files into int array
    """
    with open(filename) as f:
        return [int(x) for x in f]


"""
Parse all input files into separate int arrays
"""
F_10000 = read_integers("input/random-10000.txt")
F_20000 = read_integers("input/random-20000.txt")
F_30000 = read_integers("input/random-30000.txt")
F_40000 = read_integers("input/random-40000.txt")
F_50000 = read_integers("input/random-50000.txt")
F_60000 = read_integers("input/random-60000.txt")
F_70000 = read_integers("input/random-70000.txt")
F_80000 = read_integers("input/random-80000.txt")
F_90000 = read_integers("input/random-90000.txt")
F_100000 = read_integers("input/random-100000.txt")


def build_max_heap(array):
    """
    Build a max heap
    """
    for i in range((int)(len(array) / 2) - 1, -1, -1):
        max_heapify(array, i)


def max_heapify(array, i):
    """
    Sort the heap to maintain the heap property
    """
    left = 2 * i + 1
    right = 2 * i + 2
    if left <= len(array) - 1 and array[left] > array[i]:
        largest = left
    else:
        largest = i
    if right <= len(array) - 1 and array[right] > array[largest]:
        largest = right
    if largest != i:
        temp = array[i]
        array[i] = array[largest]
        array[largest] = temp
        max_heapify(array, largest)


def build_max_heap_analysis(array):
    """
    Generate max heap analysis for given input file
    The analysis will be average of 10 run times
    """
    total_elapsed_time = 0
    for i in range(0, 10):
        random.shuffle(array)
        start_time = time.time()
        build_max_heap(array)
        end_time = time.time()
        elapsed_time = end_time - start_time
        total_elapsed_time += elapsed_time
    average_elapsed_time = total_elapsed_time / 10 * 1000
    print("\nFor ", len(array), " elements, the average elapsed time is ", average_elapsed_time)
    print("First 15 elements")
    print_array(array, 15)

build_max_heap_analysis(F_10000)
build_max_heap_analysis(F_20000)
build_max_heap_analysis(F_30000)
build_max_heap_analysis(F_40000)
build_max_heap_analysis(F_50000)
build_max_heap_analysis(F_60000)
build_max_heap_analysis(F_70000)
build_max_heap_analysis(F_80000)
build_max_heap_analysis(F_90000)
build_max_heap_analysis(F_100000)
"""
print_array(F_10000, 15)
"""
