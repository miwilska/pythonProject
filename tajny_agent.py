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


def dodaj_cyfre (haslo, liczba, nowa):
    nowa.append(haslo + str(liczba))
    if liczba < 9:
        return dodaj_cyfre(haslo, liczba + 1, nowa)
    else:
        return nowa


def dodaj_znak (haslo, pozycja, nowa):
    haslo1 = haslo[0:pozycja] + '!' + haslo[pozycja:]
    nowa.append(haslo1)
    if pozycja < len(haslo) - 2:
        return dodaj_znak(haslo, pozycja + 1, nowa)
    else:
        return nowa


def zamien_litere (haslo, pozycja, nowa):
    if haslo[pozycja].islower():
        haslo2 = haslo[0:pozycja] + haslo[pozycja].upper() + haslo[pozycja+1:]
    nowa.append(haslo2)
    if pozycja < len(haslo)-2:
        return zamien_litere(haslo, pozycja + 1, nowa)
    else: return nowa


def przejrzyj(lista, pozycja, nowa, funkcja):
    nowa += funkcja(lista[pozycja], 0, [])
    if pozycja < len(lista)-1:
        return przejrzyj(lista, pozycja+1, nowa, funkcja)
    else: return nowa


lista = przejrzyj(lista, 0, [], dodaj_cyfre)
lista = przejrzyj(lista, 0, [], zamien_litere)
lista = przejrzyj(lista, 0, [], dodaj_znak)
print(lista)
plik = open("./"+plik, "w")
plik.write('\n'.join(lista))
plik.close()
'''
lista = ['analityk']
print("Nasza lista z hasła, przed wywołaniem funkcji przejrzyj \n")
print(lista)
print ("\n")

lista = przejrzyj(lista, 0, [], dodaj_znak)
print ("lista po wywołaniu funkcji przejrzyj, z parametrem dodaj znak \n")
print( lista )
print ("\n")

'''