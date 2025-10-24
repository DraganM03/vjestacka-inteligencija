from xo import XOGame

game = XOGame()

print(game.state)
print(game.get_actions())

actions = game.get_actions()
successor = game.get_successor(actions[0])
print(successor)