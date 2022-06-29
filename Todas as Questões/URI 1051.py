s = float(input())
if (s >= 0) and (s <= 2000):
    print('Isento')
elif (s > 2000) and (s <= 3000):
    ns = (s - 2000) 
    b = ((ns * 8)/100)
    print('R$ {:.2f}'.format(b))
elif (s > 3000) and (s <= 4500):
    b = ((1000 * 8)/100)
    ns = (s - 3000)
    bb = ((ns * 18)/100)
    st = (b+bb)
    print('R$ {:.2f}'.format(st))
elif s > 4500:
    b = ((1000 * 8)/100)
    ns = (s - 3000)
    bb = ((1500 * 18)/100)
    nns = (s - 4500)
    bbb = ((nns * 28)/100)
    stt = (b+bb+bbb)
    print('R$ {:.2f}'.format(stt))
