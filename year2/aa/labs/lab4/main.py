# ▒▄▀▄▒▄▀▄  c. AA | FAF | FCIM | UTM | Spring 2023
# ░█▀█░█▀█  FAF-212 Cristian Brinza lab4

# Importing necessary libraries
import time # for timing the execution time of the algorithms
import random # for generating random graphs
import matplotlib.pyplot as plt # for creating visualizations
import networkx as nx # for drawing graphs

# Implementation of DFS Algorithm in Python
def dfs(graph, start):
    # Create a set to keep track of visited nodes and a stack for DFS
    visited, stack = set(), [start]
    # While there are nodes to visit
    while stack:
        # Get the top node from the stack
        vertex = stack.pop()
        
        # If the node has not been visited
        if vertex not in visited:
            # Mark it as visited
            visited.add(vertex)
            # Add its unvisited neighbors to the stack
            stack.extend(graph[vertex] - visited)

    # Return the visited nodes
    return visited

# Implementation of BFS Algorithm in Python
def bfs(graph, start):
    # Create a set to keep track of visited nodes and a queue for BFS
    visited, queue = set(), [start]
    # While there are nodes to visit
    while queue:
        # Get the front node from the queue
        vertex = queue.pop(0)
        
        # If the node has not been visited
        if vertex not in visited:
            # Mark it as visited
            visited.add(vertex)
            # Add its unvisited neighbors to the queue
            queue.extend(graph[vertex] - visited)

    # Return the visited nodes
    return visited


# Create a graph with a given number of nodes and edges
def create_graph(num_nodes, num_edges):
    # Create an empty graph
    graph = {}
    # Add nodes to the graph
    for i in range(num_nodes):
        graph[i] = set()

    # Add edges to the graph
    for i in range(num_edges):
        while True:
            # Select two random nodes
            node1 = random.randint(0, num_nodes - 1)
            node2 = random.randint(0, num_nodes - 1)
            
            # If the two nodes are not the same and there is no edge between them
            if node1 != node2 and node2 not in graph[node1]:
                break
        
        # Add the edge to the graph
        graph[node1].add(node2)
        graph[node2].add(node1)

    # Return the graph
    return graph

# Function to test the DFS and BFS algorithms on a graph and record the execution time
# Test the DFS and BFS algorithms on a graph and record the execution time
def test_algorithm(graph):
    # Time the execution of DFS
    start_time = time.time()
    dfs_result = dfs(graph, 0)
    dfs_time = time.time() - start_time

    start_time = time.time()
    bfs_result = bfs(graph, 0)
    bfs_time = time.time() - start_time
    # Return the size of the graph, the degree of the first node, and the execution times of DFS and BFS
    return len(graph), len(graph[0]), dfs_time, bfs_time

# Run the tests and record the results
graph_sizes = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
edge_densities = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
results = []
for size in graph_sizes:
    for density in edge_densities:
        num_edges = int(size * (size - 1) * density / 2)
        graph = create_graph(size, num_edges)
        results.append(test_algorithm(graph))


'''
Using the subplots function with a 2x2 layout and sets the figure size to 15x15. Then, each subplot is populated with a scatter plot of the data in the results list.
The first subplot in the top-left corner shows the relationship between the number of nodes in the graph and the execution time of a depth-first search (DFS). The second subplot in the top-right corner shows the relationship between the average node degree and the execution time of DFS.
The third subplot in the bottom-left corner shows the relationship between the number of nodes in the graph and the execution time of a breadth-first search (BFS). The fourth subplot in the bottom-right corner shows the relationship between the average node degree and the execution time of BFS.
Lastly, the code generates a sample graph using the create_graph function with 10 nodes and an average node degree of 10. The nx.draw function from the NetworkX library is used to draw the graph with labels and then the plot is displayed using plt.show().
'''
# Create graphs to visualize the results
# Create a figure with 2 rows and 2 columns of subplots with a size of 15x15 inches
fig, axs = plt.subplots(2, 2, figsize=(15, 15))
# Scatter plot the first column of the results as the x-axis and the third column as the y-axis on the first subplot
axs[0, 0].scatter([r[0] for r in results], [r[2] for r in results])
axs[0, 0].set_title('DFS Execution Time vs Graph Size')
axs[0, 0].set_xlabel('Number of Nodes')
axs[0, 0].set_ylabel('Execution Time (s)')
# Scatter plot the second column of the results as the x-axis and the third column as the y-axis on the second subplot
axs[0, 1].scatter([r[1] for r in results], [r[2] for r in results])
axs[0, 1].set_title('DFS Execution Time vs Node Degree')
axs[0, 1].set_xlabel('Average Node Degree')
axs[0, 1].set_ylabel('Execution Time (s)')
# Scatter plot the first column of the results as the x-axis and the fourth column as the y-axis on the third subplot
axs[1, 0].scatter([r[0] for r in results], [r[3] for r in results])
axs[1, 0].set_title('BFS Execution Time vs Graph Size')
axs[1, 0].set_xlabel('Number of Nodes')
axs[1, 0].set_ylabel('Execution Time (s)')
# Scatter plot the second column of the results as the x-axis and the fourth column as the y-axis on the fourth subplot
axs[1, 1].scatter([r[1] for r in results], [r[3] for r in results])
axs[1, 1].set_title('BFS Execution Time vs Node Degree')
axs[1, 1].set_xlabel('Average Node Degree')
axs[1, 1].set_ylabel('Execution Time (s)')

# Display the subplots
plt.show()

# Create a sample graph with 10 nodes and an average node degree of 10
sample_graph = create_graph(10, 10)
# Draw the sample graph using the networkx library with node labels displayed
nx.draw(nx.Graph(sample_graph), with_labels=True)
plt.show()