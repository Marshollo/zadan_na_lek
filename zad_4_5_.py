def dodaj():
    plik = open("dane.txt", "a")
    imie = input("Jakie imię\n")
    nazwisko = input("Jakie nazwsko\n")
    stanowisko = input("Jakie stanowisko\n")
    wynagrodzenie = input("Jakie wynarodzenie\n")
    zapisanie = imie + " " + nazwisko + " " + stanowisko + " " + wynagrodzenie +"\n"
    plik.write(zapisanie)


def usun():
    plik = open("dane.txt, w")
    linie = plik.readlines()
    delete = input("Co usunąc?")
    for linia in linie:
        if 


while True:
    print("Dodaj, usuń")
    x = input("Co wybierasz?\n"
              "D - Dodaj\n U-Usun")
    if x == 'D':
        dodaj()