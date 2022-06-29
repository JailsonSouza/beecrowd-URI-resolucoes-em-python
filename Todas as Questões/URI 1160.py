t = int(input())
for c in range(0, t):
    pa, pb, g1, g2 = input().split()
    pa = int(pa)
    pb = int(pb)
    g1 = float(g1)
    g2 = float(g2)
    tempo = 0
    while pa <= pb:
        pa += int((pa * g1)/100)
        pb += int((pb * g2)/100)
        tempo += 1
        if tempo > 100:
            break
    if tempo > 100:
        print('Mais de 1 seculo.')
    else:
        print(f'{tempo} anos.')