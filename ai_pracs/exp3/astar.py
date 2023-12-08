# Define the graph
graph = {
    'S': {'A': 5, 'B': 8, 'C': 12},
    'A': {'D': 6, 'E': 9},
    'B': {'F': 10},
    'C': {'G': 11},
    'D': {'H': 8, 'I': 15},
    'E': {'J': 7},
    'F': {'K': 12},
    'G': {'L': 9},
    'H': {'M': 10},
    'I': {'N': 5},
    'J': {'N': 8},
    'K': {'N': 6},
    'L': {'N': 10},
    'M': {'N': 7},
    'N': {'Z': 0},
    'Z': {}
}

# Define the heuristic values for A* search
graph_heu = {
    'S': 20, 'A': 16, 'B': 18, 'C': 15,
    'D': 12, 'E': 10, 'F': 8, 'G': 6,
    'H': 6, 'I': 5, 'J': 4, 'K': 3,
    'L': 2, 'M': 1, 'N': 0, 'Z': 0
}

# Input start and goal nodes
curr_node = input("Enter Start Node: ") 
goal_node = input("Enter Goal Node: ")

# Function to search a node in a list
def searchlist(lst, key):
    for item in lst:
        if item[0] == key:
            return item

# Function to calculate the cost function
def cost_function(goal_path, current_node):
    g = 0
    for i in range(len(goal_path) - 1):
        g += graph[goal_path[i]][goal_path[i + 1]]
    g += graph[goal_path[-1]][current_node] + graph_heu[current_node]
    return g

open_list = []   # Priority queue for open list
close_list = []  # List to store closed nodes
open_list.append([curr_node, graph_heu[curr_node], [curr_node]])  # Start with the initial node and its heuristic value
n = 0

try:
    while True:
        parent_node = open_list[0][0]
        close_list.append(parent_node)
        current_path = open_list[0][2]

        if parent_node == goal_node:
            break

        print(f"Currently at node: {parent_node}")

        for neighbor in graph[open_list[0][0]]:
            open_list.append([neighbor, cost_function(current_path, neighbor), current_path + [neighbor]])

        open_list = sorted(open_list, key=lambda x: x[1])
        open_list = [pair for pair in open_list if pair[0] != parent_node]
        n += 1

        print(f"Open List is: {open_list}\nClosed List is: {close_list}\n")

except:
    print("Something went wrong, most likely the node not found :(")

print(f"So the optimized path from {open_list[0][2][0]} to {goal_node} is {open_list[0][2]} with distance: {open_list[0][1]}")
