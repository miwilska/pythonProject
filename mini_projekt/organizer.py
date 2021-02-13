from przedmioty import notatka, wizytówka, kupon
#global __number_of_element

class organizer:
    __właściciel = ""
    __bazaDanych = []
    __nastepny_numer_elementu = 1

    def __init__(self, właściciel):
        self.właściciel = właściciel


    def dodajNotatkę(self):
        priorytet = input("Priorytet:")
        tytuł = input("Tytuł:")
        treść = input("Treść:")
        self.numer_elementu = organizer.__nastepny_numer_elementu
        organizer.__nastepny_numer_elementu += 1
        nowaNotatka = notatka(priorytet, tytuł, treść, self.numer_elementu)
        self.__bazaDanych.append(nowaNotatka)

    def dodajKupon(self):
        priorytet = input("Priorytet:")
        tytuł = input("Tytuł:")
        wartosc = input("Wartosc:")
        self.numer_elementu = organizer.__nastepny_numer_elementu
        organizer.__nastepny_numer_elementu += 1
        nowyKupon = kupon(priorytet, tytuł, wartosc, self.numer_elementu)
        self.__bazaDanych.append(nowyKupon)

    def dodajWizytówkę(self):
        priorytet = input("Priorytet:")
        imię = input("Imię:")
        nazwisko = input("Nazwisko:")
        telefon = input("Telefon:")
        self.numer_elementu = organizer.__nastepny_numer_elementu
        organizer.__nastepny_numer_elementu += 1
        nowaWizytówka = wizytówka(priorytet, imię, nazwisko, telefon, self.numer_elementu)
        self.__bazaDanych.append(nowaWizytówka)

    def wyświetlNotatki(self):
        print("Lista notatek:")
        for i in self.__bazaDanych:
            if i.typ == 'notatka':
                print(i)

    def wyświetlWizytówki(self):
        print('Lista wizytów')
        for i in self.__bazaDanych:
            if i.typ == 'wizytówka':
                print(i)

    def wyświetlKupony(self):

        print('Lista kuponow')
        for i in self.__bazaDanych:
            if i.typ == 'kupon':
                print(i)

    def usun_przedmiot(self):

        print("Wyswietlam liste elekemtnów do usunięcia: ")
        for i in self.__bazaDanych :
            print(i)
        cos = input("Podaj numer co usunac:")
        for i in self.__bazaDanych:
            if i.id_numer == int(cos):
                print(i)
        potwierdzenie = input("To na pewno to? (t = tak)")
        if potwierdzenie == 't':
            del self.__bazaDanych[int(cos)]
