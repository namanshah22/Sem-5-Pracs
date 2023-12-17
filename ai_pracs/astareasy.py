from heapq import heappop,heappush

graph = {
    "A": {"B": 9, "C": 4, "D": 7},
    "B": {"E": 11},
    "C": {"E": 17, "F": 12},
    "D": {"F": 14},
    "E": {"Z": 5},
    "F": {"Z": 9},
}

graph_heu = {"A": 21, "B": 14, "C": 18, "D": 18, "E": 5, "F": 8, "Z": 0}

def a_star(graph,start,goal,heurestic):
    open_list=[(0,start,[])] # Priority queue - with (f(n),current_node,path)
    close_list=set() # keeps track of visited nodes
    
    while open_list:
        _,current,path=heappop(open_list) # removes the smallest and returns
        
        if current in close_list:
            continue # if node is already visited skip
    
        close_list.add(current) # mark current as visied
        path=path+[current] # add current node to path
        #distance=heurestic[neighbor]+cost

        if current == goal:
            return path    #goal reached
        
        # calculates the priority and adds the neighbor to the open list
        for neighbor,cost in graph[current].items():
            if neighbor not in close_list:
                heappush(open_list,(heurestic[neighbor]+cost,neighbor,path))
    
    return None

# Example usage
start_node = 'A'
goal_node = 'Z'

path= a_star(graph, start_node, goal_node, graph_heu)

if path:
    print(f"A* Path: {path}")
    print(f"Total distance : {sum(graph[path[i]][path[i+1]] for i in range(len(path)-1))}")
else:
    print("No path found.")
