from node import Node
from queue import Queue, PriorityQueue


def bfs(problem):
    
    queue = Queue()
    queue.put(Node(problem.start))
    
    visited = set([])           # this is why we used tuples and not lists
    
    while not queue.empty():
        curr_node = queue.get()
        
        if problem.is_goal(curr_node.state):
            return curr_node.recon_path()
        
        visited.add(curr_node.state)
        
        for next_node in curr_node.expand(problem):
            if next_node.state not in visited:
                queue.put(next_node)
                
    return None                 # if it doesn't find its path to the goal


def dfs(problem):
    stack = []                  # implementation of a stack using lists
    stack.append(Node(problem.start))
    
    visited = set([])
    
    while len(stack) > 0:
        curr_node = stack.pop()
        
        if problem.is_goal(curr_node.state):
            return curr_node.recon_path()
        
        visited.add(curr_node.state)
        
        for next_node in curr_node.expand(problem):
            if next_node.state not in visited:
                stack.append(next_node)
                
    return None  

def ucs(problem):
    priority = PriorityQueue()
    priority.put(Node(problem.start))

    visited = set([])
    
    while not priority.empty():
        curr_node = priority.get()
        
        if problem.is_goal(curr_node.state):
            return curr_node.recon_path()
        
        visited.add(curr_node.state)
        
        for next_node in curr_node.expand(problem):
            if next_node.state not in visited:
                priority.put(next_node)
                
    return None      
    
    
    
# A* - homework - implementing the heuristic as a weight