#1

""" for i in range(0, 51, 1):
    print(i)

#2 
    
for i in range(0, 51, 2):
    print(i) """
    
#3
    
""" from ast import If


x = int(input("Digite um número inicial: "))
y = int(input("Digite um número final: "))
z = 0

if x % 2 == 0:
    for i in range(x, y+2, 2):
        z += 1
        print(i)
    print(f'O número total de pares são: {z}')


if x % 2 == 1:
    for i in range(x+1, y+2, 2):
        z += 1
        print(i)
    print(f'O número total de pares são: {z}')
 """
#4
""" 
x = int(input("Digite um número para ter o seu fatorial: ") )
y = 1

for i in range(1,x+1):
    y *= i
print(y) """

#5

""" b = int(input("Digite a base: "))
ex = int(input("Digite o expoente: "))
x = 1
for i in range(ex):
    x *= b
print(x) """

#6

""" n = int(input("Digite um número para obter sua tabuada: "))
x = 1

print(f'Tabuada de {n}:')
for i in range(11):
    x = n*i
    print(f'{n} x {i} = {x}') """

#7

""" 27. Escreva um programa que leia um numero inteiro positivo “N” e em seguida
imprima “N” linhas do chamado Triângulo de Floyd. Para n = 6, temos:  """


n = int(input("Digite um número inteiro positivo: "))

contador = 1

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(contador, end=" ")
        contador += 1
    print()  
