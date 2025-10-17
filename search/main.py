from sliding_puzzle import SlidingPuzzle
from algorithms import bfs, dfs, ucs

sp = SlidingPuzzle((4, 1, 2, 6, 9, 8, 7, 5), (1, 2, 3, 6, 9, 8, 7, 4))
# print(sp.start, sp.goal)

# print(sp.get_actions(sp.start), sp.get_actions(sp.goal), sp.get_actions(((4, 1, 3, 6, 9, 8, 7, 5))))

# sp.print_state(sp.goal)

# sp.print_state(sp.start)

# state = sp.get_successor(sp.start, 'R')
# sp.print_state(state)
# state = sp.get_successor(state, 'R')
# sp.print_state(state)
# state = sp.get_successor(state, 'U')
# sp.print_state(state)
# state = sp.get_successor(state, 'L')
# sp.print_state(state)

print('bfs:', bfs(sp))
print('dfs:', dfs(sp))
print('ucs:', ucs(sp))