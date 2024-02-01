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
""" 
n = int(input("Digite um número para obter sua tabuada: "))
x = 1

print(f'Tabuada de {n}:')
for i in range(11):
    x = n*i
    print(f'{n} x {i} = {x}') """

#7
    

""" 21. Faça um programa que leia 10 inteiros positivos, ignorando não positivos, e
imprima sua média.  """

""" soma = 0
media = 0

for i in range(10):
    n = int(input("Digite um valor para a soma: "))
    if n > 0:
        soma += n
        print(soma)

media = soma/10
print(f'Sua média é: {media}')
 """


""" 22. Faça um programa que leia um numero inteiro “N” e depois imprima os N
primeiros números naturais ímpares.  """

""" n = int(input("Digite um número para receber essa mesma quantidade de números ímpares: "))
x = -1

for i in range(n):
    x +=2
    print(x) """

#23. Faça um programa que leia um numero inteiro positivo “N” e imprima todos os números naturais de 0 até “N” em ordem crescente. 

""" n = int(input("Digite um número para receber essa mesma quantidade de números crescente: "))
x = 0

for i in range(n):
    x +=1
    print(x)
 """

#24. Faça um programa que leia um numero inteiro positivo “N” e imprima todos os números naturais de 0 até N em ordem decrescente.  


""" n = int(input("Digite um número para receber essa mesma quantidade de números decrescente: "))
x = n

for i in range(n):
    x -=1
print(x) 
 """

#25. Faça um programa que receba dois números. Calcule e mostre: 
# - a soma dos números pares desse intervalo de números, incluindo os números digitados; 
# - a multiplicação dos números ímpares desse intervalo, incluindo os digitados; 

""" n1 = int(input("Digite um número: "))
n2 = int(input("Digite um número: "))
soma = 0


if n1 % 2 == 1:
    n1 += 1

for i in range(n1, n2+2, 2):
    soma += i
    print(i)

print(f'Sua soma é de: {soma}')
 """