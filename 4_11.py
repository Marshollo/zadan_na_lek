def tetno(A):
    hrmax = 208-(0.7 * A)
    return (hrmax)



i=0
plik = open("plik.csv", "w")

for i in range (0,100):
    # print(i,",",i,",", tetno(i))
    plik.write(f"{i}, {i}, {tetno(i)}\n")








