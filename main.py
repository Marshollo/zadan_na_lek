
def zad_4_3():
    plik = open("zadanie3.txt", "r")
    linia = plik.read()
    print(linia)


def zad_4_4():
    i = 0
    plik = open("plik3.txt", "w")
    for i in range(0, 11):
        plik.write(str(i))
        plik.write("\n")
    plik = open("plik3.txt", "r")

    plik.close()
    plik = open("plik3.txt", "a")
    for i in range(65, 91):
        plik.write(chr(i))
        plik.write("\n")
    plik = open("plik3.txt", "r")
    linia = plik.read()
    print(linia)

# k = True
# while k:
#     k = False
#     x = input("Chcesz dodać (D), usunąć(U), Wypisać(W) , Wyjść (Q)")
#
#     if x == 'D':
#         dodaj()
#     if x == 'U':
#         usun()
#     if x == 'W':
#         printuj()




