lista = [1, 3, 7, 11, 13, 17, 23]
cel = 17


def szukaj_for(lista, cel):
    count = 0
    for i in lista:
        if i == cel:
            print("Znalazłem, na pozycji", count)
            break
        else:
            if count == len(lista) - 1:
                print("Nie znalazłam celu")
        count += 1


def szukaj_rek(lista, cel, pozycja):
    if lista[pozycja] == cel:
        print("Znalazłem na pozycji", pozycja)
        return
    elif pozycja == len(lista) - 1:
        print("Nie znalazłam celu")
        return
    szukaj_rek(lista, cel, pozycja + 1)


szukaj_for(lista, cel)
szukaj_rek(lista, cel, 0)

tekst = "Dawno, dawno, temu. Na odległej stronie, o analizie danych i AI..."


def zamień(tekst, pozycja):
    if tekst[pozycja].isupper():
        tekst = tekst[0:pozycja] + tekst[pozycja].lower() + tekst[pozycja + 1:]
    else:
        tekst = tekst[0:pozycja] + tekst[pozycja].upper() + tekst[pozycja + 1:]

    if pozycja == len(tekst) - 1: return tekst;

    return zamień(tekst, pozycja + 1)


print(zamień(tekst, 0))


def search(array, cel):
    left = 0
    right = len(array)
    index = 0

    while left < right:

        index = (left + right) // 2

        if array[index] == cel:
            return index
        else:
            if array[index] < cel:
                left = index + 1
            else:
                right = index

    return -1


print("Wynik przez wyszukiwanie binarne")

index = search(lista, cel)
print(index)


def wSzybkie(lista, początek, koniec, cel):
    if początek > koniec:
        return False
    x = (początek + koniec) // 2
    if lista[x] == cel:
        print("Wynik zostal znaleziony:", x)
        return x
    if lista[x] < cel:
        return wSzybkie(lista, x + 1, koniec, cel)
    if lista[x] > cel:
        return wSzybkie(lista, początek, x - 1, cel)


print("Wynik poprzez wyszukiwanie binarne rekurencyjne")
print(wSzybkie(lista, 0, len(lista) - 1, cel))

# Napisać funkcję rekurencyjna, przyjmującą jako parametr listę, a zwracającą,
# ilość liczb jaką przechowuje. Lista, może zawierać również ciągi znaków, i wyglądać przykładowo tak:

lista1 = [1, 3, 7, 'abc', 11]


# Funkcja, powinna zwrócić liczbę 4
def ile_liczb_for(lista):
    count = 0
    for i in lista:
        if type(i) == int:
            count += 1

    return count


print("Na liście jest: ", ile_liczb_for(lista1))


def ile_liczb_rek(lista, pozycja, count):
    if pozycja == len(lista): return count
    if type(lista[pozycja]) == int:
        return ile_liczb_rek(lista, pozycja + 1, count + 1)
    else:
        return ile_liczb_rek(lista, pozycja + 1, count)


print("Na liście jest: ", ile_liczb_rek(lista1, 0, 0))





