graph = {
  'A': ['B','C'],
  'B': ['A','D','E'],
  'C': ['A','F'],
  'D': ['B'],
  'E': ['B'],
  'F': ['C'],
  #'G': [],
  #'H': [],
  #'I': []
}
def dfs(graph, current_node, goal_node, visited):
    if current_node not in visited:
        visited.append(current_node)
        not_visited = [i for i in graph.keys() if i not in visited]
        if current_node == goal_node:
            print(f"{visited}\t\t{not_visited}\t\tTrue")
            exit()        
        print(f"{visited}\t\t{not_visited}\t\tFalse")
        for i in graph[current_node]:
            dfs(graph, i, goal_node, visited)
start_node = input("Enter start node : ")
goal_node = input("Enter goal node : ")
visited = []
print("Visited\t\tNot Visted\t\tGoal state")
dfs(graph, start_node, goal_node,visited)
