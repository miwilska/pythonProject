#!/usr/bin/python3
import sys
if len(sys.argv)<2 or len(sys.argv)>3:
    print (""" Program wymaga co najmniej 1 parametru:
                1 - hasło (wymagane)
                2 - nazwa pliku w którym mają zostać zapisane wyniki. Domyślenie hasla.txt""")
    sys.exit()
elif len(sys.argv) == 3:
    plik = sys.argv[2]
else:
    plik = "hasla.txt"
lista = [sys.argv[1]]
def dodajCyfre (haslo, liczba, nowa):
    nowa.append(haslo + str(liczba))
    if liczba < 9:
        return dodajCyfre(haslo, liczba+1, nowa)
    else: return nowa
def zamienLitere (haslo, pozycja, nowa):
    if haslo[pozycja].islower():
        haslo2 = haslo[0:pozycja] + haslo[pozycja].upper() + haslo[pozycja+1:]
    nowa.append(haslo2)
    if pozycja < len(haslo)-2:
        return zamienLitere(haslo, pozycja+1, nowa)
    else: return nowa
def przejrzyj(lista, pozycja, nowa, funkcja):
    nowa += funkcja(lista[pozycja], 0, [])
    if pozycja < len(lista)-1:
        return przejrzyj(lista, pozycja+1, nowa, funkcja)
    else: return nowa
lista = przejrzyj(lista, 0, [], dodajCyfre)
lista = przejrzyj(lista, 0, [], zamienLitere)
print(lista)
plik = open("./"+plik, "w")
plik.write('\n'.join(lista))
plik.close()