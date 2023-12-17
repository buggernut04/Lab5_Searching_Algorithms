import networkx as nx
import visualize_algo as ui
from tkinter import Tk, Label, Entry, Button, StringVar, messagebox

def Add_Node():
    try:
        vertex = entry_node.get().upper()
        if not vertex.isalpha() or len(vertex) != 1:
            raise ValueError("Please enter a valid single-letter vertex.")
        
        ui.graph.add_node(vertex)
        ui.Graph_Update()
        entry_node.delete(0, 'end')  # Clear the entry widget
    except Exception as e:
        messagebox.showerror("Error", str(e))

def Delete_Node():
    try:
        vertex = entry_node.get().upper()
        if not vertex.isalpha() or len(vertex) != 1:
            raise ValueError("Please enter a valid single-letter vertex.")

        ui.graph.remove_node(vertex)
        ui.Graph_Update()
        entry_node.delete(0, 'end')  # Clear the entry widget
    except Exception as e:
        messagebox.showerror("Error", str(e))        
        
def Add_Edge():
    try:
        # Get the input from the entry widget and convert it to uppercase
        edge_input = entry_edge.get().upper()
        
        # Check if the input has at least 3 characters and follows the specified format
        if len(edge_input) < 3 or not edge_input[:2].isalpha() or not edge_input[2:].isdigit():
            raise ValueError("Please enter a valid input. Format: 'node+node+weight'")
        
        # Extract the first two characters as vertices and the remaining characters as weight
        vertices = edge_input[:2]
        weight = int(edge_input[2:])

        # Add an edge to the graph with the specified vertices and weight
        ui.graph.add_edge(vertices[0], vertices[1], weight=weight)
        
        # Update and redraw the graph
        ui.Graph_Update()
        
        # Clear the entry widget
        entry_edge.delete(0, 'end')

    # Handle the case where a ValueError is raised (e.g., invalid input format)
    except ValueError as ve:
        messagebox.showerror("Error", str(ve))

    # Handle other exceptions and show an error message
    except Exception as e:
        messagebox.showerror("Error", str(e))

def on_close():
    root.destroy()

# Function to set a consistent color for buttons
def set_button_color(button, bg_color, fg_color, active_bg_color):
    button.configure(bg=bg_color, fg=fg_color, activebackground=active_bg_color)

# Function to create and configure buttons
def create_button(root, text, command, row, column, bg_color, fg_color, active_bg_color, width=20, height=2):
    button = Button(root, text=text, command=command, width=width, height=height)
    set_button_color(button, bg_color, fg_color, active_bg_color)
    button.grid(row=row, column=column, padx=10, pady=10)
    return button

# Create the main window
root = Tk()
root.title("Searching Algorithm Options")

# Create GUI components for adding and deleting vertices
label_node = Label(root, text="ADD NODE")
entry_node = Entry(root, width=20)
button_add_node = create_button(root, "Add Node", Add_Node, 0, 2, "#3498db", "black", "#2980b9")
button_delete_node = create_button(root, "Delete Node", Delete_Node, 0, 3, "#3498db", "black", "#2980b9")
label_node.grid(row=0, column=0, padx=5, pady=5)
entry_node.grid(row=0, column=1, padx=5, pady=5)

# Create GUI components for adding edges and specifying edge weight
label_edge = Label(root, text="ADD EDGE W/ WEIGHT (ex: BC4):")
entry_edge = Entry(root, width=20)
button_add_edge = create_button(root, "Add Edge", Add_Edge, 1, 2, "#3498db", "black", "#2980b9")
label_edge.grid(row=1, column=0, padx=5, pady=5)
entry_edge.grid(row=1, column=1, padx=5, pady=5)

# Create GUI components for visualization algorithms
label_speed = Label(root, text="Animation Speed (1-10):")
speed_var = StringVar()
speed_var.set("3")  # Default animation speed
speed = Entry(root, textvariable=speed_var, width=20)
label_speed.grid(row=3, column=0, padx=5, pady=5)
speed.grid(row=3, column=1, padx=5, pady=5)

# Visualize algorithm buttons
button_visualize_DFS_Algo = create_button(root, "DFS Algorithm", lambda: ui.Visualize_DFS(speed_var), 4, 0, "#2ecc71", "black", "#27ae60")
button_visualize_BFS_Algo = create_button(root, "BFS Algorithm", lambda: ui.Visualize_BFS(speed_var), 4, 1, "#2ecc71", "black", "#27ae60")
button_visualize_Hill_Climb_Algo = create_button(root, "Hill Climb Algorithm", lambda: ui.Visualize_Hill_Climb(speed_var), 4, 2, "#2ecc71", "black", "#27ae60")
button_visualize_Beam_Search_Algo = create_button(root, "Beam Search Algorithm", lambda: ui.Visualize_Beam_Search(speed_var), 5, 2, "#2ecc71", "black", "#27ae60")
button_visualize_Branch_And_Bound_Algo = create_button(root, "Branch & Bound Algorithm", lambda: ui.Visualize_Branch_Bound(speed_var), 5, 0, "#2ecc71", "black", "#27ae60")
button_visualize_a_star = create_button(root, "A* Algorithm", lambda: ui.Visualize_A_Star(speed_var), 5, 1, "#2ecc71", "black", "#27ae60")

# Random graph generators buttons
button_generate_random_graph = create_button(root, "Random Graph Generator", ui.Generate_Dialog, 4, 3, "#e74c3c", "white", "#c0392b")
button_generate_random_connected_graph = create_button(root, "Random Connected Graph", ui.Generate_Connected_Graph_Dia, 5, 3, "#e74c3c", "white", "#c0392b")

# Pause, Play, and Close buttons
button_pause = create_button(root, "Pause", ui.pause, 10, 1, "yellow", "black", "#2980b9")
button_play = create_button(root, "Play", ui.play, 10, 2, "yellow", "black", "#2980b9")
button_close = create_button(root, "Close", on_close, 15, 4, "#95a5a6", "black", "#7f8c8d")

# Update and display the initial graph
ui.Graph_Update()

# Start the GUI main loop
root.mainloop()