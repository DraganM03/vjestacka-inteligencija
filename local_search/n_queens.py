import random

class NQueens:
    def __init__(self,n):
        self.n = n
        self.start = [random.randint(0,n-1) for j in range(n)]         # list instead of tuple, because we want to change it down the line
        
    def get_actions(self, state):
        actions = []
        
        for j in range(self.n):
            # fining all the rows which dont contain a queen in the j column
            actions += [(j, i) for i in set(range(self.n)) - {state[j]}] # adding the indexes
        
        return actions


    def get_successor(self, state, action):
        new_state = [i for i in state]
        j, i = action
        new_state[j] = i
        return new_state


    def print_state(self, state):
        for i in range(self.n):
            for j in range(self.n):
                if state[j]==i:
                    print('Q', end=' ')
                else:
                    print('.', end=' ') 
            print()

