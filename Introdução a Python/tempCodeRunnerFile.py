from ast import If


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
