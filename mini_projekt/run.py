from organizer import organizer

organizerAnalityka = organizer("Anality.edu.pl")
while True:
    print("""Co chcesz zrobić?:
                1- Dodać notatkę
                2- Dodać wizytówkę
                3- Wyświetlić notatki
                4- Wyświetlić wizytówki
                5- Dodaj kupon
                6- Wyświetl kupon
                7- Usuń
                0- Zamknać organizer""")
    x = input()

    if x == '0': break
    if x == '1': organizerAnalityka.dodajNotatkę()
    if x == '2': organizerAnalityka.dodajWizytówkę()
    if x == '3': organizerAnalityka.wyświetlNotatki()
    if x == '4': organizerAnalityka.wyświetlWizytówki()
    if x == '5': organizerAnalityka.dodajKupon()
    if x == '6': organizerAnalityka.wyświetlKupony()
    if x == '7': organizerAnalityka.usun_przedmiot()