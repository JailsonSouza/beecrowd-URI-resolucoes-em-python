a, b, c = input().split(" ")
a = float(a)
b = float(b)
c = float(c)
if ((b>a)and(b>c)):
    aux = (b)
    b = (a)
    a = (aux)
if ((c>a)and(c>b)):
    aux = (c)
    c = (a)
    a = (aux)
    
if (a >= (b+c)):
    print('NAO FORMA TRIANGULO')
elif ((a*a) == ((b*b)+(c*c))):
    print('TRIANGULO RETANGULO')
elif ((a*a) > ((b*b)+(c*c))):
    print('TRIANGULO OBTUSANGULO')
if ((a*a) < ((b*b)+(c*c))):
    print('TRIANGULO ACUTANGULO') 
if ((a == b) and (b == c) and(c == a)):
    print('TRIANGULO EQUILATERO')
elif (((a == b) and (b == a)) or ((b == c) and (c == b)) or ((c == a) and (a == c))):
    print('TRIANGULO ISOSCELES')
