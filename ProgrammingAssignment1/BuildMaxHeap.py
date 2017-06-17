"""
CS566 - Programming Assignment 1
Hanxiong Shi
hanxiong@bu.edu
"""
print("\nCS566 - Programming Assignment 1")
print("Hanxiong Shi")
print("hanxiong@bu.edu\n")

def read_integers(filename):
    """
    Parse input files into int array
    """
    with open(filename) as f:
        return [int(x) for x in f]

