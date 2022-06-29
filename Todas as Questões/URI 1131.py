aux = 3
grenais = 0
sgi = 0
sgg = 0
emp = 0
while aux != 2:
    grenais += 1
    n, m = input().split()
    n = int(n)
    m = int(m)
    if (n > m):
        sgi += 1
    elif (n < m):
        sgg += 1
    else:
        emp += 1
    aux = 3
    while aux != 1:
        aux = int(input('Novo grenal (1-sim 2-nao)\n'))
        if (aux == 2):
            break
print('{} grenais'.format(grenais))
print('Inter:{}'.format(sgi))
print('Gremio:{}'.format(sgg))
print('Empates:{}'.format(emp))
if (sgi > sgg):
    print('Inter venceu mais')
elif(sgi < sgg):
    print('Gremio venceu mais')
else:
    print('Nao houve vencedor')