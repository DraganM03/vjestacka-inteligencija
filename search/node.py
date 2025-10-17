class Node:
    
    def __init__(self, state, parent=None, action=None):
        self.state = state
        self.parent = parent
        self.action = action
    
    def expand(self, problem):
        
        successors = []
        
        for action in problem.get_actions(self.state):
            succ_state = problem.get_successor(self.state, action)
            new_node = Node(succ_state, self, action)
            successors.append(new_node)
        
        return successors

    def recon_path(self):
        
        actions = []
        # curr_node = goal_node
        curr_node = self
        
        while curr_node != None:
            if curr_node.action == None:
                break
            actions.append(curr_node.action)
            curr_node = curr_node.parent
        
        return actions[::-1]