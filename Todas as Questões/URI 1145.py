x, y = input().split()
x = int(x)
y = int(y)
count = 0
for i in range(1, y+1):
    if i % x == 0:
        print(i)
    elif(i % x != 0)and(i == y):
        print(i, end=" ")
    else:
        print(i, end=" ")
        