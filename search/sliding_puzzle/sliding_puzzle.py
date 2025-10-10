class SlidingPuzzle:

    def __init__(self, start, goal):
        self.start = start
        #self.state = start
        self.goal = goal

    
    def is_goal(self, state):
        return state == self.goal
    
    def find_blank(self, state):
        return 45 - sum(state)          # suma svih plocica sa plocicom koja nedostaje je uvijek 45 = 9*(9+1)/2 
    
    def get_actions(self, state):       # lista stringova, tipa ['U', 'D', 'L', 'R']
        pos_blank = self.find_blank(state)

        actions = []

        # ako nije poslednji red, mozemo da pomjerimo elemente ispod praznine na gore
        if pos_blank < 7:   # nije 6 jer gledamo find_blank koji vraca bukvalnu poziciju praznine
            actions.append('U')

        # ako nije prvi red, mozemo da pomjerimo elemente iznad praznine na dole
        if pos_blank > 3:
            actions.append('D')

        # ako nije prva kolona, mozemo da pomjerimo elemente lijevo od praznine na desno
        if pos_blank % 3 != 0:
            actions.append('L')
        
        # ako nije zadnja kolona, mozemo da pomjerimo elemente desno od praznine na lijevo
        if pos_blank % 3 != 1:
            actions.append('R')

        return actions

        

    def get_successor(self, state, action):
        pos_blank = self.find_blank(state)

        if action == 'U':
            pos_piece = pos_blank + 3
        elif action == 'D':
            pos_piece = pos_blank - 3
        elif action == 'L':
            pos_piece = pos_blank + 1
        elif action == 'R':
            pos_piece = pos_blank - 1
        else:
            raise ValueError("Invalid action")
        
        # return (s if s != pos_piece else pos_blank for s in state)
        tuple.index
        return (*self.state[:self.state.index(pos_piece)], pos_blank, *self.state[self.state.index(pos_piece)+1:])

    def print_state(self, state):
        pass

    # nije ovo prelazio
    # def __str__(self):
    #     return f'node:\n\tstart: {self.start}\n\tstate: {self.state}\n\tgoal: {self.goal}'