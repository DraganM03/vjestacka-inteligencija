# intro to python 

# ----- if else -----
n = 25                              # deklaracija ne zahtijeva navodjenje tipa promjenljive
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
    print(i, end=" ")               # end=" " da ne bi prelazilo u novi red
    i += 1

print()                             # prelazak u novi red

# --- for ---
for i in range(10):                 # ponasa se kao for each u drugim jezicima
    print(i, end=" ")

print()                             # prelazak u novi red

# ----- functions -----
def kvadrati_brojeva(a, b):
    for i in range(a, b+1, 1):      # +1 da bi ukljucio i b, 3. argument je korak (moze biti i negativan)
        print(i**2, end=" ")

kvadrati_brojeva(2, 8)
print()                             # prelazak u novi red


# ----- data structures -----
# --- list ---
# - ponasa se kao dinamicki niz, jer nije bas kao ulancana lista

list = [5, 8, 10, 13, 24, 30, 48]   # deklaracija liste, ne moraju svi podaci da budu istog tipa

# - standard list operations -
print(list[0], list[4], list[6])    # pristup elementu liste (indeksiranje pocinje od 0)
list[4] = 25                        # promjena vrijednosti elementa liste
print(list)                         # ispis cijele liste

# - python specific list operations -
print(list[-1], list[-2])           # pristup elementima liste od kraja (-1 je zadnji element, -2 pretposljednji, ...)
print(list[2:5])                    # slicing, pristup podlisti (krajnja granica nije ukljucena)
print(list[:-1])                    # od pocetka do pretposljednjeg
print(list[3:])                     # od 3. do kraja   
print(list[:])                      # plitka kopija cijele liste

list[2:3] = [11, 12, 13, 14]        # zamjena podliste (moze da se mijenja se velicina liste)
print(list) 

print(list[::-1])                   # obrtanje liste (3. argument je korak)

list.append(100)                    # dodavanje elementa na kraj liste
print(list)

print(list.pop())                   # uklanjanje i vracanje zadnjeg elementa liste
print(list)

print(list.index(13))               # trazenje indeksa prvog pojavljivanja elementa u listi
print(list.index(13, 5, 10))        # trazenje indeksa elementa u podlisti (od start do stop-1)
# print(list.index(99))             # baca ValueError ako element nije u listi

n = 99
if n in list:                       # provjera da li je element u listi
    print(list.index(n))
else:
    print(f"{n} nije u listi")

print(list.count(13))               # broj pojavljivanja elementa u listi

def comparator(x):                 # custom comparator funkcija za opadajuci poredak
    return -x
print(sorted(list, key=comparator))  # sortiranje liste bez promjene originalne liste (key moze biti i lambda funkcija)
print(sorted(list, key=lambda x: -x)) # lambda funkcije su jednolinijske jednkratne funckije za proste operacije

# --- tuple ---


# --- dictionary ---            # ekivalenta hash mapama u drugim jezicima


# --- set ---


# --- 3rd party data structures ---
# counter, queue, heap, ...