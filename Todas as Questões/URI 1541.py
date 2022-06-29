import cmath
import math

while True:
    a, b, c = input().split(" ")
    a = int(a)
    b = int(b)
    c = int(c)
    print(a, ' ',b,' ', c)
    if a == 0 or b == 0 or c == 0:
        break
    at = math.trunc(((a*b)*100) / c)
    print(at)
	ml = math.sqrt(at)
	rp = math.trunc(ml)
	print(rp)