from abc import ABC, abstractmethod


class przedmiot(ABC):
    def __init__(self, typ, priorytet, id_numer):
        self.typ = typ
        self.priorytet = priorytet
        self.id_numer = id_numer

    @abstractmethod
    def __str__(self):

        pass


class notatka(przedmiot):
    def __init__(self, priorytet, tytuł, treść, id_numer):
        super().__init__("notatka", priorytet, id_numer)
        self.tytuł = tytuł
        self.treść = treść

    def __str__(self):
        info = str(self.id_numer) + "\n"
        info += self.typ + "Priorytet " + self.priorytet + "\n"
        info += self.tytuł + "\n"
        info += self.treść + "\n"
        return info


class wizytówka(przedmiot):

    def __init__(self, priorytet, imię, nazwisko, telefon, id_numer):
        super().__init__("wizytówka", priorytet, id_numer)
        self.imię = imię
        self.nazwisko = nazwisko
        self.telefon = telefon

    def __str__(self):
        info = str(self.id_numer) + "\n"
        info += self.typ + "Priorytet " + self.priorytet + "\n"
        info += self.imię + " " + self.nazwisko + "\n"
        info += self.telefon + "\n"
        return info


class kupon(przedmiot):

    def __init__(self, priorytet, tytuł, wartosc,id_numer):
        super().__init__("kupon", priorytet, id_numer)
        self.tytuł = tytuł
        self.wartosc = wartosc

    def __str__(self):
        info = str(self.id_numer) + "\n"
        info += self.typ + "Priorytet " + self.priorytet + "\n"
        info += self.tytuł + "\n"
        info += self.wartosc + "\n"
        return info
