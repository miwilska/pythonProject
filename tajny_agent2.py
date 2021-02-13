#!/usr/bin/python3
from abc import ABC, abstractmethod
class kontact(ABC):

    def __init__(self, type, numer, imie, nazwisko):
        self.type = type
        self.numer = numer
        self.imie = imie
        self.nazwisko = nazwisko
        self.znajomi = []

    @abstractmethod
    def __str__(self):
        pass

class zolnierz(kontact):

    def __init__(self, numer, imie, nazwisko):
        super().__init__('regular', numer, imie, nazwisko)

    def __str__(self):
        info = str(self.numer) + " " + self.imie + " " + self.nazwisko + "\n"
        info += "Zna:" + str(self.znajomi)
        return info

class network():

    __osoby = []
    __autoryzowany = False
    __tajnyLogin = 'analityk'
    __tajneHaslo = 'edu.pl'

    def autoryzuj(self):
        login = input('Podaj login:')
        haslo = input('Podaj haslo:')
        if login == self.__tajnyLogin and haslo == self.__tajneHaslo:
            print("Autoryzacja poprawna")
            return True
        else:
            print("Hasło lub login niepoprawny")
            return False

    def zalogowany(funk):

        def wew(self, *args, **kwargs):
            print("Log - wykonujemy funkcję:", funk.__name__)
            if self.__autoryzowany == False:
                print("Musisz być zalogowany.")
                return
            else:
                return funk(self, *args, **kwargs)

        return wew

    @zalogowany
    def wyswietl(self, lista):
        for i in lista:
            print(i)

    @zalogowany
    def dodajOsobe(self, numer):
        imie = input("Imię:")
        nazwisko = input("Nazwisko:")
        new = zolnierz(numer, imie, nazwisko)
        return new

    @zalogowany
    def dodajZnajomego(self, osoby):
        a = int(input("Numer osoby 1"))
        b = int(input("Numer osoby 2"))

        for o in osoby:
            if o.numer == a:
                o.znajomi = o.znajomi + [b]
            if o.numer == b:
                o.znajomi = o.znajomi + [a]

        return osoby


    def wykonuj(self):
        while True:
            print("""
                1 - wyświetl sieć kontaktów
                2 - dodaj osobę
                3 - dodaj powiązanie pomiędzy kontaktami
                4 - zaloguj
                9 - zamknij \n
            """)
            x = input("co chcesz zrobić?")

            if x == '1':
                self.wyswietl(self.__osoby)
            if x == '2':
                nowa = self.dodajOsobe(len(self.__osoby)+1)
                if nowa != None: self.__osoby.append(nowa)
            if x == '3':
                self.dodajZnajomego( self.__osoby )
            if x == '4':
                if self.autoryzuj():
                    self.__autoryzowany = True
                else:
                    self.__autoryzowany = False
            if x == '9':
                import sys
                sys.exit()


n = network()
n.wykonuj()