import queue
import networkx as nx

def DFS_Algo(graph: nx.Graph(), start_node, end_node, visited=None, path=None, cost=0):
    # Initialize visited set and path list for the first function call
    if visited is None:
        visited = set()
    if path is None:
        path = []

    # List to store the pattern of nodes, paths, and costs during the depth-first search
    pattern = []

    # Check if the current node has not been visited yet
    if start_node not in visited:
        # Append current node, path, and cost to the pattern list
        pattern.append((start_node, path.copy(), cost))
        visited.add(start_node)

        # Check if the current node is the end node
        if start_node == end_node:
            return pattern  # If yes, return the current pattern

        # Explore neighboring nodes using recursion
        for node in graph[start_node]:
            if node not in visited:
                # Recursively call DFS_Algo for the neighboring node
                pattern.extend(
                    DFS_Algo(graph, node, end_node, visited, path + [start_node], cost + graph[start_node][node]['weight'])
                )

                # Check if the last node in the pattern is the end node
                if pattern[-1][0] == end_node:
                    break  # If yes, stop exploring further

    return pattern  # Return the final pattern after the depth-first search


def BFS_Algo(graph: nx.Graph(), start_node, end_node):
    # Initialize a set to keep track of visited nodes
    visited = set()
    
    # Initialize a queue for breadth-first traversal
    q = queue.Queue()
    
    # Enqueue the starting node along with its path and cost
    q.put((start_node, [start_node], 0))
    
    # List to store the pattern of nodes, paths, and costs during the breadth-first search
    pattern = []

    # Continue the breadth-first search until the queue is empty
    while not q.empty():
        # Dequeue a node, its path, and cost
        node, path, cost = q.get()
        
        # Check if the current node has not been visited yet
        if node not in visited:
            # Append current node, path, and cost to the pattern list
            pattern.append((node, path.copy(), cost))
            visited.add(node)
            
            # Check if the current node is the end node
            if node == end_node:
                break  # If yes, stop the search

            # Explore neighboring nodes using breadth-first traversal
            for neighbor in graph[node]:
                if neighbor not in visited:
                    # Create a new path and cost for the neighboring node
                    new_path = path + [neighbor]
                    new_cost = cost + graph[node][neighbor]['weight']
                    
                    # Enqueue the neighboring node along with its new path and cost
                    q.put((neighbor, new_path, new_cost))
    
    return pattern  # Return the final pattern after the breadth-first search

def Hill_Climb_Algo(graph: nx.Graph(), start_node, end_node, heuristic):
    # Initialize current node, path, and cost
    current_node = start_node
    path = [current_node]
    cost = 0

    # List to store the pattern of nodes, paths, and costs during the hill climbing
    pattern = [(current_node, path.copy(), cost)]

    # Continue the hill climbing until the current node reaches the end node
    while current_node != end_node:

        # Get the neighbors of the current node and sort them based on the heuristic value
        neighbors = list(graph[current_node])
        neighbors.sort(key=lambda neighbor: heuristic(neighbor, end_node))

        found = False

        # Explore neighbors in sorted order
        for neighbor in neighbors:
            if neighbor not in path:
                
                # Update path, cost, and current node to the selected neighbor
                path.append(neighbor)
                cost += heuristic(neighbor, end_node)
                current_node = neighbor
                found = True
                
                # Append current node, path, and cost to the pattern list
                pattern.append((current_node, path.copy(), cost))
                break

        # If no unvisited neighbor is found, break the loop
        if not found:
            break

    return pattern  # Return the final pattern after hill climbing


def Beam_Search_Algo(graph: nx.Graph(), start_node, end_node, beam_width, heuristic):
    # Initialize a set to keep track of visited nodes
    visited = set()

    # Initialize a queue for beam search
    q = queue.Queue()

    # Enqueue the starting node along with its path and cost
    q.put((start_node, [start_node], 0))

    # List to store the pattern of nodes, paths, and costs during the beam search
    pattern = []

    # Continue the beam search until the queue is empty
    while not q.empty():
        # List to store entries at the current level of the search
        current_level = []

        # Process a limited number of entries based on the beam width
        for _ in range(min(beam_width, q.qsize())):
            # Dequeue a node, its path, and cost
            node, path, cost = q.get()

            # Check if the current node has not been visited yet
            if node not in visited:
                # Append current node, path, and cost to the pattern list
                pattern.append((node, path.copy(), cost))
                visited.add(node)

                # Check if the current node is the end node
                if node == end_node:
                    break  # If yes, stop the search

                # Get the neighbors of the current node and sort them based on the heuristic value
                neighbors = list(graph[node])
                neighbors.sort(key=lambda neighbor: heuristic(neighbor, end_node))

                # Explore neighbors and add them to the current level
                for neighbor in neighbors:
                    if neighbor not in visited:
                        new_path = path + [neighbor]
                        new_cost = cost + heuristic(neighbor, end_node)
                        current_level.append((neighbor, new_path, new_cost))

        # Enqueue entries from the current level for the next iteration
        for entry in current_level:
            q.put(entry)

    return pattern  # Return the final pattern after the beam search


def Branch_And_Bound_Algo(graph: nx.Graph(), start_node, end_node):
    # Initialize priority queue with the starting node, path, and cost
    pq = queue.PriorityQueue()
    pq.put((0, (start_node, [start_node], 0)))  # Enqueue tuple (priority, (node, path, cost))
    visited = set()
    pattern = []

    # Explore nodes in priority order until the priority queue is empty
    while not pq.empty():
        # Retrieve and unpack the current state (node, path, cost) with priority
        _, (node, path, cost) = pq.get()

        # Append current state to the pattern list if the node is not visited
        if node not in visited:
            pattern.append((node, path.copy(), cost))
            visited.add(node)

            # Stop the search if the end node is found
            if node == end_node:
                break

            # Enqueue neighbors with priority based on cost (branching)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    new_path = path + [neighbor]
                    new_cost = cost + graph[node][neighbor]['weight']
                    pq.put((new_cost, (neighbor, new_path, new_cost)))

    return pattern

def A_Star_Algo(graph: nx.Graph(), start_node, end_node, heuristic):
    # Priority queue for A* search
    pq = queue.PriorityQueue()

    # Initialize with the starting node, path, and cost
    pq.put((0, (start_node, [start_node], 0)))  # Enqueue tuple (priority, (node, path, cost))
    visited = set()
    pattern = []

    # Continue A* search until the priority queue is empty
    while not pq.empty():
        _, (node, path, cost) = pq.get()

        # Process the node if not visited
        if node not in visited:
            # Append current state (node, path, cost) to the pattern list
            pattern.append((node, path.copy(), cost))
            visited.add(node)

            # Break if goal node is reached
            if node == end_node:
                break

            # Explore neighbors and enqueue based on priority (total cost + heuristic)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    new_path = path + [neighbor]
                    new_cost = cost + graph[node][neighbor]['weight']
                    priority = new_cost + heuristic(neighbor, end_node)
                    pq.put((priority, (neighbor, new_path, new_cost)))

    return pattern