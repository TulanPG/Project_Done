"""Project made by Tulan"""

"""
 ZADANIE 1. GENERATOR KODÓW POCZTOWYCH
przyjmuje 2 stringi: "79-900" i "80-155" i zwraca listę kodów pomiędzy nimi
"""

def zad_1(start, stop):
    import csv
    # Wykorzystując liste w csv kodów pocztowych, wylistuje wszystkie kody z zakresu podanego start-stop
    go = False
    temp_lista_kodow = []
    lista_kodow = []

    # funkcja najblizej pozwala wykluczyć kody spoza listy, podając najbliższą wartość w górę

    def najblizej(do_sprawdzenia, temp_lista, do_tylu):

        while not (do_sprawdzenia in temp_lista):

            poczatek = int(do_sprawdzenia[:2])
            koniec = int(do_sprawdzenia[3:7])

            # pozwala dodawać i odejmować by mieć wartość pomiedzy kodami
            if do_tylu:
                koniec += 1
                if koniec > 999:
                    poczatek += 1
                    koniec = 0
            else:
                koniec -= 1
                if koniec < 0:
                    poczatek -= 1
                    koniec = 999

            poczatek = str(poczatek)
            koniec = str(koniec)
            if len(poczatek) == 1:
                poczatek = "0" + poczatek
            if len(koniec) == 1:
                koniec = "00" + koniec
            if len(koniec) == 2:
                koniec = "0" + koniec
            do_sprawdzenia = str(poczatek) + "-" + str(koniec)

        return do_sprawdzenia

    with open('kody_pocztowe.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            temp_lista_kodow.append(row[0])
        start_poprawny = start
        stop_poprawny = stop
        # warunek sprawdza czy mamy kod spoza listy
        if not (start in temp_lista_kodow):
            start_poprawny = najblizej(start, temp_lista_kodow, True)
        # warunek sprawdza czy mamy kod spoza listy
        if not (stop in temp_lista_kodow):
            stop_poprawny = najblizej(stop, temp_lista_kodow, False)

        for row in temp_lista_kodow:

            if row == start_poprawny:
                # rozpoczyna wypisywanie kodów gdy kody z listy osiągną wartość (string1)
                go = True
            if go:
                lista_kodow.append(row)
            if row == stop_poprawny:
                # zwraca listę, gdy osiągnie wartość kodu końcowego (string2)
                return lista_kodow

    return lista_kodow


# zad_1("79-900", "88-999"))

"""
ZADANIE 2. PODANA JEST LISTA ZAWIERAJĄCA ELEMENTY O WARTOŚCIACH 1-n. 
NAPISZ FUNKCJĘ KTÓRA SPRAWDZI JAKICH ELEMENTÓW BRAKUJE
1-n = [1,2,3,4,5,...,10]
np. n=10
wejście: [2,3,7,4,9], 10
wyjście: [1,5,6,8,10]
"""


def zad_2(wejscie, n):
    temp_lista = []

    for x in range(1, n + 1):
        if not (str(x) in str(wejscie)):
            temp_lista.append(x)

    wyjscie = temp_lista
    return wyjscie


# zad_2([2,3,7,4,9],10)

"""ZADANIE 3. NALEŻY WYGENEROWAĆ LISTĘ LICZB OD 2 DO 5.5 ZE SKOKIEM CO 0.5, DANE WYNIKOWE MUSZĄ BYĆ TYPU DECIMAL."""


def zad_3():
    from decimal import Decimal
    lista = []
    x = Decimal(2)

    while x <= Decimal(5.5):
        lista.append(Decimal(x))
        x += Decimal(0.5)
    return lista


# zad_3()
