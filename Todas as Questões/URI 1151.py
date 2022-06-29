n1 = 0
n2 = 1
cont = 3
n = int(input())
if n == 1:
    print(n1)
else:
    print('{} {}'.format(n1,n2), end='')
    while cont <= n:
        n3 = n1 + n2
        print(' {}'.format(n3), end='')
        n1 = n2
        n2 = n3
        cont+=1
print()