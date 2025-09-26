# intro to python 

# ----- if else -----
n = 25                          # deklaracija ne zahtijeva navodjenje tipa promjenljive
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


# ----- data structures -----
# --- list ---
# - ponasa se kao dinamicki niz, jer nije bas kao ulancana lista

list = [5, 8, 10, 13, 24, 30, 48]  # deklaracija liste, ne moraju svi podaci da budu istog tipa

# - standardne operacije nad listama -
print(list[0], list[4], list[6])   # pristup elementu liste (indeksiranje pocinje od 0)
list[4] = 25                       # promjena vrijednosti elementa liste
print(list)                        # ispis cijele liste


# --- tuple ---


# --- dictionary ---            # ekivalenta hash mapama u drugim jezicima


# --- set ---


# --- 3rd party data structures ---
# counter, queue, heap, ...