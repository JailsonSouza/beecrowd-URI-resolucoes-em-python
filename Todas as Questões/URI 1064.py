som = (0)
med = (0)
i = (1)
while i <= 6:
    val = float(input())
    if(val > 0):
        som = (som + val)
        med += 1
    i +=1
print(med,'valores positivos')
media = (som / med)
print('{:.1f}'.format(media))