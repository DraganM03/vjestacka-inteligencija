# Intro to Python

# ======= if else =======
print("===== if else =====")
n = 25                              # deklaracija ne zahtijeva navodjenje tipa promjenljive
if n % 3 == 0:
    print("n = 3k")
elif n % 3 == 1:
    print("n = 3k + 1")
else:
    print("n = 3k + 2")


# ======= loops =======
print("===== loops =====")
# ===== while =====
i = 0
while i < 10:
    print(i, end=" ")               # end=" " da ne bi prelazilo u novi red
    i += 1

print()                             # prelazak u novi red

# ===== for =====
for i in range(10):                 # ponasa se kao for each u drugim jezicima
    print(i, end=" ")

print()                             # prelazak u novi red

# ======= functions =======
def kvadrati_brojeva(a, b):
    for i in range(a, b+1, 1):      # +1 da bi ukljucio i b, 3. argument je korak (moze biti i negativan)
        print(i**2, end=" ")

kvadrati_brojeva(2, 8)
print()                             # prelazak u novi red


# ====== data structures =======
# ===== list =====
# - ponasa se kao dinamicki niz, ne funkcionise kao ulancana lista
# - mutable (promjenjiva)
print("===== list =====")

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

def comparator(x):                  # custom comparator funkcija za opadajuci poredak
    return -x
print(sorted(list, key=comparator))     # sortiranje liste bez promjene originalne liste (key moze biti i lambda funkcija)
print(sorted(list, key=lambda x: -x))   # lambda funkcije su jednolinijske jednkratne funckije za proste operacije

print()

# ===== tuple =====
# - nepromjenjiva verzija liste
# - immutable (nepromjenjiva)

print("===== tuple =====")

tuple = (1, 2, 3)                   # deklaracije torke, ne moraju svi podaci da budu istog tipa
print(tuple)                        # ispis torke, koriste se drugacije zagrade () u odnosu na listu []
print(tuple[1])
# tuple[1] = 5                      # baca TypeError jer je tuple nepromjenjiv
print(tuple[1:])                    # slicing radi kao i kod liste

empty = ()
print(empty, type(empty))           # prazan tuple
single = (1,)                       # tuple sa jednim elementom mora imati zarez
# single = (1)                      # inace se tretira kao int
print(single, type(single))                      

def f(x):
    # return f(x**2, x**3)
    return x**2, x**3               # i ako ne navedemo zagrade, ako stoji zarez izmedju, vratice tuple

x1, x2 = f(10)                      # otpakivanje
x2, x1 = x1, x2                     # rotiranje vrijednosti otpakivanjem
print(x1, x2)

print((x1,x2).index(x1))
print((x1,x2).count(x1))

print()

# ===== dictionary =====                # ekivalenta hash mapama u drugim jezicima
# - kao json objekti/hash tabele - parovi kljuc:vrijednost
# - mutable (promjenjiva)
# - kljucevi moraju biti immutable tipa (string, int, float, tuple, ...), vrijednosti mogu biti bilo kog tipa
print("===== dictionary =====")

dictionary = {
    'key1': 123,
    'key2': 789
}

print(dictionary)                   # ispis cijelog rjecnika
print(dictionary['key1'])           # pristup vrijednosti preko kljuca
dictionary['key1'] = 456            # promjena vrijednosti preko kljuca
dictionary['key3'] = 123            # dodavanje novog kljuc:vrijednost para
print(dictionary)

# print(dictionary['key4'])         # javlja KeyError ako kljuc nije u rjecniku
if 'key4' in dictionary:            # zbog toga bi trebali da provjerimo da li postoji kljuc, prije nego sto pokusamo da mu pristupimo vrijednostima koje su mu dodijeljene
    print(dictionary['key4'])
else:
    print("key4 nije u rjecniku")

dictionary[123] = "abc"             # kljucevi ne moraju biti istog tipa
dictionary[(1,2)] = [1,2,3]         # kljuc moze biti i tuple
print(dictionary)

# kretanje po rjecniku
print("\nKljuc : Vrijednost")
for key in dictionary:              # iteracija po kljucevima rjecnika
    print(f"{key}: {dictionary[key]}")

print("\nVrijednosti:")
for v in dictionary.values():       # .values() - lista vrijednosti rjecnika
    print(v)

print("\nKljucevi:")
for k in dictionary.keys():         # .keys() - lista kljuceva rjecnika. isto kao prva for petlja
    print(k)

print("\nKljuc : Vrijednost")
for k, v in dictionary.items():     # .items() - lista (kljuc, vrijednost) torki rjecnika
    print(f"{k}: {v}")

print()

# ===== set =====
# - neuredjena kolekcija jedinstvenih elemenata
# - mutable (promjenjiva)
# - elementi moraju biti immutable tipa (string, int, float, tuple, ...)

print("===== set =====")

set1 = {1, 2, 3, 4, 5}              # deklaracija skupa
print(set1, type(set1))             # ispis skupa

set1.add(6)                         # dodavanje elementa u skup
set1.add(5)                         # vec postojeci elementi se nece duplirati iako se izvrsi "dodavanje"
print(set1)                         # nece dodati jer 5 vec postoji u skupu

if 3 in set1:                     # provjera da li element postoji u skupu
    print("3 je u skupu")
else:
    print("3 nije u skupu")

set2 = {4, 5, 6, 7, 8}

# skupovne operacije
print(set1 | set2)                  # unija skupova
print(set1 & set2)                  # presjek skupova
print(set1 - set2)                  # razlika skupova
print(set1 ^ set2)                  # simetricna razlika skupova

# nije spomenuo, ali postoje i:
print(set1 <= set2)                 # provjera da li je set1 podskup set2
print(set1 >= set2)                 # provjera da li je set2 podskup

set1.remove(1)                      # uklanjanje elementa iz skupa (javlja KeyError ako element nije u skupu)
set1.discard(10)                    # uklanjanje elementa iz skupa (ne javlja gresku ako element nije u skupu)
print(set1)

# tips and tricks
set1 = set1 | {10, 11, 12}          # dodavanje vise elemenata u skup
set1 |= {13, 14, 15}                # isto ^
print(set1)

print()

# ===== 3rd party data structures =====
# counter, queue, heap, ...


# ===== kretanje kroz strukture =====
print("===== kretanje kroz strukture =====")
y = [1,2,3,4]
z = [5,6,7,8]
for i in range(len(y)):
    print(y[i] + z[i], end=" ")

print()

# struktura - lista, tuple, string, set, dictionary (iteracija po kljucevima)

for i,j in zip(y,z):                # zip pravi tuple od elemenata iz vise struktura tako sto 
                                    # spaja svaki i-ti element iz svih navedenih struktura x,y,... do kraja najkarace od njih, tj. (x[i], y[i], ...)
    print(i+j, end=" ")

print()

for idx, el in enumerate(y):        # enumerate pravi tuple (indeks, element) za svaki element iz strukture y
    print(idx, el, end=" ")

print()

for el in sorted(y):                # sortiranje strukture
    print(el, end=" ")

print()

for el in reversed(y):              # obrtanje strukture
    print(el, end=" ")

print('\n')

# ===== list comprehensions =====
# - generisanje liste po zadatom sablonu
print("===== list comprehensions =====")

sve_nule = [0 for x in range(10)]   # lista koja sadrzi samo nule
print(sve_nule)

squares = [x**2 for x in range(10)]  # lista kvadrata brojeva od 0 do 9
print(squares)

even = [x for x in range(20) if x % 2 == 0]  # lista parnih brojeva od 0 do 19
print(even)

nested = [[0 if x%2==0 else 1 for x in range(y-2,y+1)] for y in range(0,9,3)]   # ugnjezdene liste
print(nested)                       

