n1, n2, n3 = input().split(" ")
n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
if ((n1+n2) > n3) and ((n2 + n3) > n1) and ((n1+n3)> n2):
    print('Perimetro = {:.1f}'.format(n1+n2+n3))
else:
    print('Area = {:.1f}'.format(((n1+n2)*n3)/2))