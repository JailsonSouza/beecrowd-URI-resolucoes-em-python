a,b = input().split(" ")
a = int(a)
b = int(b)
if (a == 1):
    tot = (4*b)
    print('Total: R$ {:.2f}'.format(tot))
elif (a == 2):
    tot = (4.50*b)
    print('Total: R$ {:.2f}'.format(tot))
elif (a == 3):
    tot = (5*b)
    print('Total: R$ {:.2f}'.format(tot))
elif (a == 4):
    tot = (2*b)
    print('Total: R$ {:.2f}'.format(tot))
elif (a == 5):
    tot = (1.50*b)
    print('Total: R$ {:.2f}'.format(tot))