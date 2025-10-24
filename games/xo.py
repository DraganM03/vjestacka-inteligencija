from copy import deepcopy

class XOGame:

    def __init__(self):
        self.state = {
            'board': [[' ' for i in range(3)] for i in range(3)],
            'current_player': 'X'
        }
    
    def get_actions(self):  # we are pulling the state from the object itself
        actions = []
        for i in range(3):
            for j in range(3):
                if self.state["board"][i][j] == ' ':
                    actions.append((i, j, self.state["current_player"]))
        return actions

    def get_successor(self, action):
        new_state = deepcopy(self.state)
        i, j, player = action
        new_state["board"][i][j] = player
        new_state["current_player"] = 'O' if player == 'X' else 'X'
        return new_state

    def print_state(self):
        pass

    def has_won(self, player):
        pass

    def game_over():
        pass