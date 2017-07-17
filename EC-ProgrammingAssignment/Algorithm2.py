"""
CS566 - EC Programming Assignment
Hanxiong Shi
hanxiong@bu.edu
"""


from common import read_direct_distance, read_user_input, read_graph_input, is_connected, find_adjacent_nodes, print_shortest_path


"""
Algorithm2: Among all nodes v that are adjacent to the node n,
choose the one for which w(n, v) + dd(v) is the smallest.
"""


print("\nCS566 - EC Programming Assignment")
print("Hanxiong Shi")
print("hanxiong@bu.edu")
print("Algorithm 2\n")

# read direct distance map
DIRECT_DISTANCE_MAP = read_direct_distance()
# read graph input
GRAPH_INPUT = read_graph_input()

