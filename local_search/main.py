from n_queens import NQueens

nq = NQueens(4)

print(nq.start)

nq.print_state(nq.start)

actions = nq.get_actions(nq.start)
print(actions)

successors = nq.get_successor(nq.start, actions[0])
print(successors)

nq.print_state(successors)