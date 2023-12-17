# Searching Algorithms Visualization

This program provides a graphical user interface (GUI) for visualizing various graph search algorithms on a dynamically generated graph. The application is divided into three main modules: GUI, Visualization, and Algorithms. Each module serves a specific purpose in creating, visualizing, and executing graph search algorithms.

## GUI Module
The GUI module is responsible for creating a user-friendly interface using the Tkinter library. Users can interact with the application by adding or deleting nodes, adding edges with weights, and visualizing different graph search algorithms. The GUI offers options for adjusting animation speed and generating random graphs.

## GUI Components
Add Node / Delete Node: Allows users to add or delete single-letter vertices to/from the graph.
Add Edge with Weight: Enables users to add edges with weights using the format 'node+node+weight'.
Visualization Buttons: Buttons to trigger visualization of various algorithms (DFS, BFS, Hill Climb, Beam Search, Branch & Bound, A*).
Random Graph Generation: Options for generating a random graph or a random connected graph.
Pause / Play / Close: Controls to pause, play, or close the visualization.
Visualization Module
The Visualization module utilizes the NetworkX and Matplotlib libraries to visualize the dynamically changing graph during the execution of search algorithms. The module provides functions for updating the graph and pausing/resuming the visualization.

## Visualization Functions
Visualize: Displays the search process without heuristics, updating the graph at each step.
Visualize_Heuristics: Displays the search process with heuristics, including heuristic values in the visualization.
Graph_Update: Updates and redraws the graph based on changes made by the user.
Algorithms Module
The Algorithms module contains implementations of various graph search algorithms, including DFS, BFS, Hill Climbing, Beam Search, Branch & Bound, and A*. These algorithms are applied to the graph generated in the GUI module.

## Implemented Algorithms
DFS Algorithm: Depth-First Search algorithm.
BFS Algorithm: Breadth-First Search algorithm.
Hill Climb Algorithm: Hill Climbing algorithm with heuristic.
Beam Search Algorithm: Beam Search algorithm with heuristic.
Branch & Bound Algorithm: Branch and Bound algorithm.
A* Algorithm: Search algorithm with heuristic.

## Getting Started
To use the application, run the main program (main.py). The GUI will open, allowing you to interact with the graph and visualize various search algorithms.

## Dependencies
NetworkX
Matplotlib
Tkinter
