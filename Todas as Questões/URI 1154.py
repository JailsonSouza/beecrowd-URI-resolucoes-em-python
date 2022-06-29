total = cont = idade = 0
while idade >= 0:
    idade = int(input())
    if idade >= 0:
        total += idade
        cont += 1
media = total / cont
print('{:.2f}'.format(media))