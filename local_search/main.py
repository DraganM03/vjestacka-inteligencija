from n_queens import NQueens
from alhorithms import hill_climbing


nq = NQueens(4)

print(nq.start)
# nq.print_state(nq.start)

# print(nq.get_actions(nq.start))

# actions = nq.get_actions(nq.start)
# nq.print_state(nq.get_successor(nq.start, actions[0]))

# print(nq.get_score(nq.start))

nq.print_state(hill_climbing(nq))