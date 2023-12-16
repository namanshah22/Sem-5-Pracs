def dfs(graph, visited, src, goal):
    if src not in visited:
        visited.append(src)
        if src == goal:           
            exit()
        print(src)
        for i in graph[src]:
            dfs(graph, visited, i, goal)
        #print(goal)

graph = {
  'A': ['B', 'C'],
  'B': ['A', 'D'],
  'C': ['A', 'D', 'E'],
  'D': ['F', 'C', 'B'],
  'E': ['C', 'F', 'G'],
  'F': ['D', 'E', 'H'],
  'G': ['E', 'H'],
  'H': ['F', 'G']
}

visited = []
src = input("Enter source node: ")
goal = input("Enter goal node: ")
dfs(graph, visited, src, goal)
