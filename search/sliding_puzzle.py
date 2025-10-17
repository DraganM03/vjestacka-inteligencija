class SlidingPuzzle:
    
    def __init__(self, start, goal):
        self.start = start
        self.goal = goal
    
    
    def is_goal(self, state):
        return state == self.goal
    
    
    def find_blank(self, state):
        return 45 - sum(state)
    
    
    def get_actions(self, state):
        
        pos_blank = self.find_blank(state)
        actions = []
        
        if pos_blank < 7:
            actions.append('U')
        
        if pos_blank > 3:
            actions.append('D')
            
        if pos_blank % 3 != 1:
            actions.append('R')
        
        if pos_blank % 3 != 0:
            actions.append('L')
        
        return actions
    
    
    def get_successor(self, state, action):
        
        pos_blank = self.find_blank(state)
        
        if action == 'U':
            pos_piece = pos_blank + 3
        
        elif action == 'D':
            pos_piece = pos_blank - 3
        
        elif action == 'R':
            pos_piece = pos_blank - 1
        
        else:
            pos_piece = pos_blank + 1
        
        idx = state.index(pos_piece)
        return state[:idx] + (pos_blank,) + state[idx+1:]

    
    def print_state(self, state):
        
        for i in range(3):
            for j in range(3):
                pos = i*3 + j + 1
                if pos in state:
                    idx = state.index(pos)
                    print(idx + 1, end=' ')
                else:
                    print(' ', end=' ')
            print()
        print()