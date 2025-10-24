import random

class NQueens:
    
    def __init__(self, n):
        self.n = n
        self.start = [random.randint(0, n-1) for j in range(n)]
    
    
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
                if state[j] == i:
                    print('Q', end=' ')
                else:
                    print('.', end=' ')
            print()


    def get_score(self, state):
        score = 0
        for j1, i1 in enumerate(state):
            for j2, i2 in enumerate(state[j1+1:], start=j1+1): # start=j1+1 to avoid starting from zero and double counting
                # checking for the number of attacking queens - the goal is to minimize this score
                if i1 != i2 and j1 != j2 and abs(i1 - i2) != abs(j1 - j2):
                    score += 1
        return score
