nome = str(input())
salario = float(input())
vendas = float(input())
bonus = (vendas * 15)/100
total = salario + bonus
print(f'TOTAL = R$ {total:.2f}')