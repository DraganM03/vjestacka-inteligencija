from sliding_puzzle import SlidingPuzzle

sp = SlidingPuzzle((4,1,2,6,9,8,7,5), (1,2,3,6,9,8,7,4))
# (4,1,2,6,9,8,7,5) - 1 na 4. poziciju, 2 na 1. poziciju, 3 na 2. poziciju, 4 na 6. poziciju,...

print(sp.get_actions(sp.start))
print(sp.get_actions(sp.goal))

sp.print_state(sp.start)

sp.print_state(sp.get_successor(sp.start, 'U'))
# sp.print_state(sp.get_successor(sp.start, 'D')) # ne moze se izvrsiti jer nije validna akcija
sp.print_state(sp.get_successor(sp.start, 'L'))
sp.print_state(sp.get_successor(sp.start, 'R'))