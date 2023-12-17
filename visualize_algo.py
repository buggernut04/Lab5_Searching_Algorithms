import random
import networkx as nx
import matplotlib.pyplot as plt
import time
from tkinter import messagebox, simpledialog
import algorithms as alg

# Create a graph
graph = nx.Graph()
pos = nx.spring_layout(graph)

is_paused = False

def Generate_Dialog():
    try:
        vertices = simpledialog.askinteger("Input", "Enter the number of vertices:")
        edges = simpledialog.askinteger("Input", "Enter the number of edges:")
        
        if vertices is not None and edges is not None:
            graph.clear()
            graph.update(Generate_Graph(vertices, edges))
            Graph_Update()
    except Exception as e:
        messagebox.showerror("Error", str(e))

def Generate_Graph(num_vertices, num_edges, weight_range=(1, 10)):
    # Check if the number of vertices is valid
    if num_vertices < 1:
        raise ValueError("Number of vertices must be greater than 0.")

    # Check if the number of edges is valid
    if num_edges < 0 or num_edges > num_vertices * (num_vertices - 1):
        raise ValueError("Number of edges is invalid.")

    # Create an empty graph
    G = nx.Graph()

    # Add vertices to the graph
    vertices = [chr(ord('A') + i) for i in range(num_vertices)]
    G.add_nodes_from(vertices)

    # Add random edges to the graph
    edges_added = 0
    while edges_added < num_edges:
        i, j = random.sample(range(num_vertices), 2)
        if not G.has_edge(vertices[i], vertices[j]):
            # Add an edge between vertex i and vertex j
            weight = random.randint(weight_range[0], weight_range[1])
            G.add_edge(vertices[i], vertices[j], weight=weight)
            edges_added += 1

    return G

def Generate_Connected_Graph(num_vertices):
    # Generates a random connected graph using the Watts-Strogatz model.

    # Check if the number of vertices is valid
    if num_vertices < 1:
        raise ValueError("Number of vertices must be greater than 0.")

    # Parameters for the Watts-Strogatz model
    K = 4  # Average degree (adjust as needed)
    P = 0.1  # Probability of rewiring (adjust as needed)

    # Generate a connected graph using the Watts-Strogatz model
    G = nx.connected_watts_strogatz_graph(num_vertices, K, P)

    # Relabel nodes to use single-letter labels (A, B, C, ...)
    mapping = {i: chr(ord('A') + i) for i in range(num_vertices)}
    G = nx.relabel_nodes(G, mapping)

    # Assign random weights to edges
    for u, v in G.edges():
        G[u][v]['weight'] = random.randint(1, 10)  # You can adjust the weight range

    return G

def Generate_Connected_Graph_Dia():
    try:
        num_vertices = simpledialog.askinteger("Input", "Enter the number of vertices:")
        if num_vertices is not None:
            graph.clear()
            graph.update(Generate_Connected_Graph(num_vertices))
            Graph_Update()
    except Exception as e:
        messagebox.showerror("Error", str(e))
        

# Function to visualize the search process without heuristic
def Visualize(pattern, title, G, pos, animation_speed):
    plt.figure()

    visited_nodes = []  # List to keep track of visited nodes
    enqueues = 0       # Counter for the number of enqueues

    # Iterate through each step in the search pattern
    for step in pattern:
        node, path, cost = step
        visited_nodes.append(node)  # Add the current node to the visited nodes list

        # Create a string of visited nodes, node colors, and edge labels for Visualize
        visited_sequence = ', '.join(visited_nodes)
        node_colors = ['yellow' if x == node else 'skyblue' for x in G.nodes()]
        edge_labels = {(u, v): G[u][v]['weight'] for u, v in G.edges()}

        # Clear the previous plot, set title, and draw the graph with updated information
        plt.clf()
        plt.title(title, loc="left", fontsize=10, pad=5)
        nx.draw(G, pos, with_labels=True, node_color=node_colors)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='blue')

        # Display information on the plot
        info_text = f"Number of Enqueues: {enqueues}\nPath: {' -> '.join(path + [node])}\nQueue Size: {len(path)}\nPath Elements: {visited_sequence}\nTotal Path Cost: {cost}"
        plt.text(0, 1.0, info_text, verticalalignment='top', horizontalalignment='left', transform=plt.gca().transAxes, fontsize=9)

        plt.draw()
        plt.pause(animation_speed)  # Pause for animation speed

        # Check if Visualize is paused and wait until resumed
        if is_paused:
            while is_paused:
                plt.pause(0.1)

        # Increment the enqueues counter when a new node is enqueued
        if len(path) > 1 and path[-1] != path[-2]:
            enqueues += 1

    plt.show()
    time.sleep(0.5)

# Function to visualize the search process with heuristic
def Visualize_Hueristics(pattern, title, G, pos, heuristic, end_node, animation_speed):
    plt.figure()

    visited_nodes = []  # List to keep track of visited nodes
    enqueues = 0       # Counter for the number of enqueues

    # Iterate through each step in the search pattern
    for step in pattern:
        node, path, cost = step
        visited_nodes.append(node)  # Add the current node to the visited nodes list

        # Create a string of visited nodes, node colors, and edge labels for Visualize
        visited_sequence = ', '.join(visited_nodes)
        node_colors = ['yellow' if x == node else 'skyblue' for x in G.nodes()]
        edge_labels = {(u, v): G[u][v]['weight'] for u, v in G.edges()}

        # Clear the previous plot, set title, and draw the graph with updated information
        plt.clf()
        plt.title(title, loc="left", fontsize=10, pad=5)
        nx.draw(G, pos, with_labels=True, node_color=node_colors)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='blue')

        # Display information on the plot, including heuristic value
        heuristic_value = heuristic(node, end_node) if hasattr(heuristic, '__call__') else 0
        info_text = f"Number of Enqueues: {enqueues}\nPath: {' -> '.join(path + [node])}\nQueue Size: {len(path)}\nPath Elements: {visited_sequence}\nTotal Path Cost: {cost}\nHeuristic: {heuristic_value:.2f}"
        plt.text(0, 1.0, info_text, verticalalignment='top', horizontalalignment='left', transform=plt.gca().transAxes, fontsize=9)

        plt.draw()
        plt.pause(animation_speed)  # Pause for animation speed

        # Check if Visualize is paused and wait until resumed
        if is_paused:
            while is_paused:
                plt.pause(0.1)

        # Increment the enqueues counter when a new node is enqueued
        if len(path) > 1 and path[-1] != path[-2]:
            enqueues += 1

    plt.show()
    time.sleep(0.5)


def Visualize_DFS(speed_var):
    start_node = simpledialog.askstring("Input", "Enter the start node:")
    end_node = simpledialog.askstring("Input", "Enter the end node:")
    speed = max(0.1, min(1.0, 1.0 - (int(speed_var.get()) - 1) / 9))

    if start_node and end_node:
        start_node = start_node.upper()
        end_node = end_node.upper()
        Visualize(alg.DFS_Algo(graph, start_node, end_node), 'DFS_Algo Visualize', graph, pos, speed)

def Visualize_BFS(speed_var):
    start_node = simpledialog.askstring("Input", "Enter the start node:")
    end_node = simpledialog.askstring("Input", "Enter the end node:")
    speed = max(0.1, min(1.0, 1.0 - (int(speed_var.get()) - 1) / 9))
    if start_node and end_node:
        start_node = start_node.upper()
        end_node = end_node.upper()
        Visualize(alg.BFS_Algo(graph, start_node, end_node), 'BFS_Algo Visualize', graph, pos, speed)

# Heuristic function
def Heuristic(node, goal_node):
    # Manhattan distance heuristic
    return abs(ord(node) - ord(goal_node))

def Visualize_Hill_Climb(speed_var):
    start_node = simpledialog.askstring("Input", "Enter the start node:")
    end_node = simpledialog.askstring("Input", "Enter the end node:")
    speed = max(0.1, min(1.0, 1.0 - (int(speed_var.get()) - 1) / 9))
    
    if start_node and end_node:
        start_node = start_node.upper()
        end_node = end_node.upper()

        # Call the hill climbing with heuristic function
        pattern = alg.Hill_Climb_Algo(graph, start_node, end_node, Heuristic)

        Visualize_Hueristics(pattern, 'Hill Climbing Visualize', graph, pos, Heuristic, end_node, speed)

def Visualize_Beam_Search(speed_var):
    start_node = simpledialog.askstring("Input", "Enter the start node:")
    end_node = simpledialog.askstring("Input", "Enter the end node:")
    beam_width = simpledialog.askinteger("Input", "Enter the beam width:")
    speed = max(0.1, min(1.0, 1.0 - (int(speed_var.get()) - 1) / 9))

    if start_node and end_node and beam_width is not None:
        start_node = start_node.upper()
        end_node = end_node.upper()

        # Call the beam search with heuristic function
        pattern = alg.Beam_Search_Algo(graph, start_node, end_node, beam_width, Heuristic)

        # Display the beam width in the title
        title = f'Beam Search Visualize (Beam Width: {beam_width})'
        
        # Pass end_node to the Visualize_Hueristics function
        Visualize_Hueristics(pattern, title, graph, pos, Heuristic, end_node, speed)

def Visualize_Branch_Bound(speed_var):
    start_node = simpledialog.askstring("Input", "Enter the start node:")
    end_node = simpledialog.askstring("Input", "Enter the end node:")
    speed = max(0.1, min(1.0, 1.0 - (int(speed_var.get()) - 1) / 9))

    if start_node and end_node:
        start_node = start_node.upper()
        end_node = end_node.upper()

        # Call the branch and bound search
        pattern = alg.Branch_And_Bound_Algo(graph, start_node, end_node)

        # Display the Visualize
        title = 'Branch and Bound Visualize'
        Visualize(pattern, title, graph, pos, speed)

def Visualize_A_Star(speed_var):
    start_node = simpledialog.askstring("Input", "Enter the start node:")
    end_node = simpledialog.askstring("Input", "Enter the end node:")
    speed = max(0.1, min(1.0, 1.0 - (int(speed_var.get()) - 1) / 9))

    if start_node and end_node:
        start_node = start_node.upper()
        end_node = end_node.upper()

        # Call the A* search with the heuristic function
        pattern = alg.A_Star_Algo(graph, start_node, end_node, Heuristic)

        # Display the Visualize
        title = 'A* Search Visualize'
        Visualize_Hueristics(pattern, title, graph, pos, Heuristic, end_node, speed)

def Graph_Update():
    global pos
    pos = nx.spring_layout(graph)

    plt.clf()
    plt.title("GRAPH")
    edge_labels = {(u, v): graph[u][v]['weight'] for u, v in graph.edges()}
    nx.draw(graph, pos, with_labels=True, node_color='yellowgreen')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels, font_color='red')
    plt.show()

def pause():
    global is_paused
    is_paused = True

def play():
    global is_paused
    is_paused = False
