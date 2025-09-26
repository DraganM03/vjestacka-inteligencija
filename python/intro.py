# intro to python 

# ----- if else -----
n = 25                          # deklaracija je atipicna
if n % 3 == 0:
    print("n = 3k")
elif n % 3 == 1:
    print("n = 3k + 1")
else:
    print("n = 3k + 2")


# ----- loops -----
# --- while ---
i = 0
while i < 10:
    print(i, end=" ")           # end=" " da ne bi prelazilo u novi red
    i += 1

print()                         # prelazak u novi red

# --- for ---
for i in range(10):             # ponasa se kao for each u drugim jezicima
    print(i, end=" ")

print()                         # prelazak u novi red

# ----- functions -----
def kvadrati_brojeva(a, b):
    for i in range(a, b+1, 1):     # +1 da bi ukljucio i b, 3. argument je korak (moze biti i negativan)
        print(i**2, end=" ")

kvadrati_brojeva(2, 8)
print()                         # prelazak u novi red
