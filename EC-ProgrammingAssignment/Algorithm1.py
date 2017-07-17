"""
CS566 - EC Programming Assignment
Hanxiong Shi
hanxiong@bu.edu
"""


from common import read_direct_distance, read_user_input, read_graph_input, is_connected, find_adjacent_nodes, print_shortest_path


"""
Algorithm1: Among all nodes v that are adjacent to the node n,
choose the one with the smallest dd(v).
"""


print("\nCS566 - EC Programming Assignment")
print("Hanxiong Shi")
print("hanxiong@bu.edu")
print("Algorithm 1\n")


# Read direct distance map
DIRECT_DISTANCE_MAP = read_direct_distance()
# Read graph input
GRAPH_INPUT = read_graph_input()
# Read user input (starting node)
USER_INPUT_NODE = read_user_input()
# Create a path map to keep track all nodes that visited
# Add the user input node as the 1st node in path map
path_map = []
path_map.append(USER_INPUT_NODE)


def print_direct_distance(direct_distance_map, nodes_list):
    """
    Print all adjacent nodes' direct distance,
    then return the shortest node.
    """
    shortest_node = nodes_list[0]
    shortest_distance = direct_distance_map[shortest_node]
    for n in nodes_list:
        print(n, ": dd(", n, ") = ", direct_distance_map[n])
        # Check if the node has the shortest direct distance
        if direct_distance_map[n] < shortest_distance:
            shortest_distance = direct_distance_map[n]
            shortest_node = n
    return shortest_node


def algorithm_1(node):
    """
    Algorithm 1
    """
    # Print current node
    print("\nCurrent node = ", node)
    # Find adjacent nodes
    adjacent_nodes = find_adjacent_nodes(GRAPH_INPUT, node)
    print("Adjacent nodes = ", adjacent_nodes)
    # Filter out the adjacent nodes that are already in the path
    for n in adjacent_nodes:
        if n in path_map:
            print(n, "is already in the path.")
            adjacent_nodes.remove(n)
    # Loop through adjacent nodes and print out direct distance
    shortest_node = print_direct_distance(DIRECT_DISTANCE_MAP, adjacent_nodes)
    # Check if the shortest node is destination node
    if shortest_node == 'Z':
        print("Z is the destination node. Stop.")
        return
    else:
        print(shortest_node, "is selected.")
        # Add shortest_node to the path map
        path_map.append(shortest_node)
        # Print the shortest path
        print_shortest_path(path_map)
        algorithm_1(shortest_node)


# Init shortest path calculation
algorithm_1(USER_INPUT_NODE)
