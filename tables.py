def KopIter(A, n, m):
    tablica = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):

        for j in range(1, m + 1):

            if i > n or j > m:

                tablica[i][j] = 0

            else:

                k1 = tablica[i - 1][j]

                k2 = tablica[i][j - 1]

                if k1 > k2:

                    tablica[i][j] = A[i - 1][j - 1] + k1

                else:

                    tablica[i][j] = A[i - 1][j - 1] + k2

    return tablica[n][m]


A = [[1, 2, 3], [4, 5, 9]]
n = len(A)
m = len(A[0])

wynik = KopIter(A, n, m)
print(wynik)
