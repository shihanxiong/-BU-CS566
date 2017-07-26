"""
CS566 - EC Programming Assignment
Hanxiong Shi
hanxiong@bu.edu
"""


from common import read_direct_distance, read_user_input, read_graph_input, is_connected, find_adjacent_unvisited_nodes, print_shortest_path, print_shortest_path_length


"""
Algorithm2: Among all nodes v that are adjacent to the node n,
choose the one for which w(n, v) + dd(v) is the smallest.
"""


print("\nCS566 - EC Programming Assignment")
print("Hanxiong Shi")
print("hanxiong@bu.edu")
print("Algorithm 2\n")

# Read direct distance map
DIRECT_DISTANCE_MAP = read_direct_distance()
# Read graph input
GRAPH_INPUT = read_graph_input()
# Read user input (starting node)
USER_INPUT_NODE = read_user_input()
# Create a path map to keep track of the final shortest path
# Add the user input node as the 1st node in path map
path_map = []
path_map.append(USER_INPUT_NODE)
# Create an array to keep track of all nodes that are visited
visited_nodes = []
visited_nodes.append(USER_INPUT_NODE)


def print_weighted_distance(graph_map, direct_distance_map, current_node, nodes_list):
    """
    Print all adjacent nodes' direct distance,
    then return the shortest node.
    """
    if len(nodes_list) != 0:
        shortest_node = nodes_list[0]
        shortest_distance = graph_map[current_node][shortest_node] + \
            direct_distance_map[shortest_node]
        for n in nodes_list:
            print(n, ": w(", current_node, ",", n, ") + dd(", n, ") = ",
                  graph_map[current_node][n], "+", direct_distance_map[n], "=", graph_map[current_node][n] + direct_distance_map[n])
            # Check if the node has the shortest direct distance
            if graph_map[current_node][n] + direct_distance_map[n] < shortest_distance:
                shortest_distance = graph_map[current_node][n] + \
                    direct_distance_map[n]
                shortest_node = n
        return shortest_node
    else:
        return None


def algorithm_2(node):
    """
    Algorithm 2
    """
    if node == 'Z':
        print("Z is the destination node. Stop.")
        return

    # Print current node
    print("\nCurrent node = ", node)
    # Find adjacent nodes
    adjacent_nodes = find_adjacent_unvisited_nodes(
        GRAPH_INPUT, node, visited_nodes)
    print("Adjacent nodes = ", adjacent_nodes)
    # Filter out the adjacent nodes that are already in the path
    for n in adjacent_nodes:
        if n in path_map:
            print(n, "is already in the path.")
            adjacent_nodes.remove(n)

    # When adjacent_nodes is empty -> dead end
    if len(adjacent_nodes) == 0:
        print("Dead end.")
        # Find the node to track back to
        back_track_to_node = visited_nodes[len(visited_nodes) - 2]
        print("Backtrack to", back_track_to_node)
        # Remove the node from the path map
        path_map.remove(node)
        # Continue
        algorithm_2(back_track_to_node)

    # Loop through adjacent nodes and print out direct distance
    shortest_node = print_weighted_distance(
        GRAPH_INPUT, DIRECT_DISTANCE_MAP, node, adjacent_nodes)
    # Check if the shortest node is destination node
    if shortest_node == 'Z':
        print("Z is the destination node. Stop.")
        # Add Z to the path map
        path_map.append('Z')
        print_shortest_path(path_map)
        print_shortest_path_length(GRAPH_INPUT, path_map)
        return
    # If there's no more adjacent nodes, terminate
    elif shortest_node == None:
        return
    else:
        print(shortest_node, "is selected.")
        # Add shortest_node to the path map
        path_map.append(shortest_node)
        # Add shortest_node to the visited nodes map
        visited_nodes.append(shortest_node)
        # Print the shortest path
        print_shortest_path(path_map)
        algorithm_2(shortest_node)


algorithm_2(USER_INPUT_NODE)
