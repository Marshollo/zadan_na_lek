def tetno(A):
    hrmax = 208-(0.7 * A)
    return (hrmax)



i=0
for i in range (0,100):
    print(i,",",i,",", tetno(i))
    plik = open("plik.csv", "a")
    plik.write








