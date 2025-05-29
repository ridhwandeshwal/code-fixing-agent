from heapq import *

def shortest_path_length(length_by_edge, startnode, goalnode):
    unvisited_nodes = [(0, startnode)]
    visited_nodes = set()
    distances = {startnode: 0}

    while unvisited_nodes:
        distance, node = heappop(unvisited_nodes)

        if node == goalnode:
            return distance

        if node in visited_nodes:
            continue
        visited_nodes.add(node)

        for nextnode in get_neighbors(node, length_by_edge):
            new_distance = distance + length_by_edge[node, nextnode]
            if nextnode not in distances or new_distance < distances[nextnode]:
                distances[nextnode] = new_distance
                heappush(unvisited_nodes, (new_distance, nextnode))

    return float('inf')

def get_neighbors(node, length_by_edge):
    neighbors = []
    for start, end in length_by_edge:
        if start == node:
            neighbors.append(end)
    return neighbors
"""
Shortest Path

dijkstra

Implements Dijkstra's algorithm for finding a shortest path between two nodes in a directed graph.

Input:
   length_by_edge: A dict with every directed graph edge's length keyed by its corresponding ordered pair of nodes
   startnode: A node
   goalnode: A node

Precondition:
    all(length > 0 for length in length_by_edge.values())

Output:
    The length of the shortest path from startnode to goalnode in the input graph
"""