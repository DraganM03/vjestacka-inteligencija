class Node:
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action

    def expand(self, problem):
        successors = []
        for action in problem.get_actions(self.state):
            successor_state = problem.get_successor(self.state, action)
            # state, parent, action
            new_node = Node(successor_state, self, action)
            successors.append(new_node)
        return successors

    def reconstruct_path(self, goal_node):
        actions = []
        curr_mode = goal_node

        while curr_mode != None:
            actions.append(curr_mode.action)
            curr_mode = curr_mode.parent

        return actions[::-1]