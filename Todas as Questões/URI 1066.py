vp = (0)
vi = (0)
vpos = (0)
vneg = (0)
i = (1)
while i <= 5:
    val = int(input())
    if(val % 2 == 0):
        vp += 1
    if(val % 2 != 0):
        vi += 1
    if(val > 0):
        vpos += 1
    if(val < 0):
        vneg += 1
    i +=1
print(vp,'valor(es) par(es)')
print(vi,'valor(es) impar(es)')
print(vpos,'valor(es) positivo(s)')
print(vneg,'valor(es) negativo(s)')