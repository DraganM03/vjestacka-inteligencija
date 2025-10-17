from node import Node
from queue import Queue, PriorityQueue


def bfs(problem):
    
    q = Queue()
    q.put(Node(problem.start))
    
    visited = set([])           # this is why we used tuples and not lists
    
    while not q.empty():
        curr_node = q.get()
        
        if problem.is_goal(curr_node.state):
            return curr_node.recon_path()
        
        visited.add(curr_node.state)
        
        for next_node in curr_node.expand(problem):
            if next_node.state not in visited:
                q.put(next_node)
                
    return None                 # if it doesn't find its path to the goal