while True:
    try:
        n = int(input())

        M = []

        for l in range(n):
            L = []
            cont = l
            for c in range(n):
                if (l+c) == n-1:
                    L.append(2)
                elif (l == c):
                    L.append(1)
                else:
                    L.append(3)
            M.append(L)

        for i in range(n):
            for j in range(n):
                print(f'{M[i][j]}', end="")
            print('')

    except EOFError:
        break