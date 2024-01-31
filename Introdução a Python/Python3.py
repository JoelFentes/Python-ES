#1.
""" 
n1 = int(input("Digite um número inteiro: "))
n2 = int(input("Digite outro número inteiro: "))
n3 = int(input("Digite mais um número inteiro: "))

def comparacao_num_maior(n1, n2, n3):
    if n1 >= n2 and n1 >= n3:
        print(f'O maior número é: {n1}')
    elif n2 >= n1 and n2 >= n3:
        print(f'O maior número é: {n2}')    
    elif n3 >= n1 and n3 >= n2:
        print(f'O maior número é: {n3}')


comparacao_num_maior(n1, n2, n3)

def comparacao_num_menor(n1, n2, n3):
    if n1 <= n2 and n1 < n3:
        print(f'O menor número é: {n1}')
    elif n2 <= n1 and n2 < n3:
        print(f'O menor número é: {n2}')    
    elif n3 <= n1 and n3 < n2:
        print(f'O menor número é: {n3}') 

comparacao_num_menor(n1, n2, n3) 
"""
#1.
""" 
n1 = int(input("Digite um número inteiro: "))
n2 = int(input("Digite outro número inteiro: "))
n3 = int(input("Digite mais um número inteiro: "))


lista: list[int] = []

def valores_cres(n1, n2, n3):
    lista.append(n1)
    lista.append(n2)
    lista.append(n3)
    lista.sort()
    print(f'A ordem dos seus números é {lista[0]}, {lista[1]}, {lista[2]} ')

valores_cres(n1, n2, n3) 
"""


#2.

""" 
def valores_cres2(n1,n2,n3):
    if n1 > n2 and n1 > n3 and n2 > n3:
        first = n1
        second = n2
        third = n3
        print(f'A ordem dos seus números é {first}, {second}, {third} ')
    elif n1 > n2 and n1 > n3 and n2 > n3:
        first = n1
        second = n3
        third = n2
        print(f'A ordem dos seus números é {first}, {second}, {third} ')
    elif n2 > n1 and n2 > n3 and n1 > n3:
        first = n2
        second = n1
        third = n3
        print(f'A ordem dos seus números é {first}, {second}, {third} ')
    elif n2 > n1 and n2 > n3 and n1 < n3:
        first = n2
        second = n3
        third = n1
        print(f'A ordem dos seus números é {first}, {second}, {third} ')
    elif n3 > n1 and n3 > n2 and n2 < n1:
        first = n3
        second = n1
        third = n2
        print(f'A ordem dos seus números é {first}, {second}, {third} ')
    elif n3 > n1 and n3 > n2 and n2 > n1:
        first = n3
        second = n2
        third = n1
        print(f'A ordem dos seus números é {first}, {second}, {third} ')

valores_cres2(n1,n2,n3)
"""
#3.

""" 
idade =  int(input("Digite sua idade: "))

def idade_categ(idade):
    if idade >= 5 and idade <= 7:
        print(f'Sua Categoria é Infantil A')
    elif idade >= 7 and idade <= 10:
        print(f'Sua Categoria é Infantil B')  
    elif idade >= 11 and idade <= 13:
        print(f'Sua Categoria é Juventil A')
    elif idade >= 14 and idade <= 17:
        print(f'Sua Categoria é Juventil B')     
    elif idade > 18:
        print(f'Sua Categoria é Adulto')     
    else:
        print(f'Não Existe Categoria para a sua Idade')             

    
idade_categ(idade)
"""