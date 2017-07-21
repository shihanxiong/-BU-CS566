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
                map[headers[idx]][rowname] = int(item)
    return map


def read_user_input():
    """
    Read user input, re-try when input is invalid.
    """
    node = input("Please enter a node: ")
    if len(node) == 1 and node.isalpha():
        node = node.upper()
        print("The user input is ->", node)
        return node
    else:
        print("The input is invalid, please try again.")
        return read_user_input()


def is_connected(graph_map, node_a, node_b):
    """
    Check if two nodes (node_a, node_b) are connected in the given graph map.
    """
    if graph_map[node_a][node_b] != 0:
        return True
    else:
        return False


def find_adjacent_unvisited_nodes(graph_map, node, visited_nodes):
    """
    Look through the map graph and return a list of all the adjacent nodes
    that have not been visited.
    """
    adjacent_nodes = []
    for n in graph_map[node]:
        if is_connected(graph_map, node, n) and n not in visited_nodes:
            adjacent_nodes.append(n)
    return adjacent_nodes


def print_shortest_path(path):
    """
    Print out the shortest path direction.
    """
    path_map = "Shortest path: " + str(path[0])
    for p in path[1:]:
        path_map = str(path_map) + " -> " + str(p)
    print(path_map)
    return


def print_shortest_path_length(graph_map, path):
    """
    Print out the length of the shortest path and sum value
    """
    sum = 0
    distance_num = ""
    for p in range(1, len(path), 1):
        distance = graph_map[path[p - 1]][path[p]]
        distance_num = distance_num + str(distance)
        if p != len(path) - 1:
            distance_num = distance_num + " + "
        else:
            distance_num = distance_num + " = "
        sum = sum + distance
    print("Shortest path length = " + distance_num + str(sum))
    return

