"""
CS566 - EC Programming Assignment
Hanxiong Shi
hanxiong@bu.edu
"""

import re

"""
This file contains common functions that are being used by both algorithms
"""


def read_direct_distance():
    """
    Parse direct distance file into dictionary
    """
    direct_distance = {}
    with open("input/direct_distance_1.txt") as f:
        for line in f:
            (key, val) = line.split()
            direct_distance[key] = int(val)
    return direct_distance


def read_graph_input():
    """
    Read in a graph input file and store as 2D array
    """
    with open("input/graph_input_1.txt") as f:
        map = {}
        headers = []
        lines = f.readlines()
        for header in re.findall('(\w+)', lines[0]):
            headers.append(header)
            map[header] = {}
        for line in lines[1:]:
            items = re.findall('(\w+)', line)
            rowname = items[0]
            for idx, item in enumerate(items[1:]):
                map[headers[idx]][rowname] = item
    return map


def read_user_input():
    """
    read user input, re-try when input is invalid.
    """
    node = input("Please enter a node: ")
    if len(node) == 1 and node.isalpha():
        node = node.upper()
        print("The user input is ->", node)
        return node
    else:
        print("The input is invalid, please try again.")
        read_user_input()
