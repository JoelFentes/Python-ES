import sys

i = 0

'''
while i <= 100:
    i +=1
    if i % 2 == 0:
        print(i)
'''

#Calcular a média de uma lista de números: Crie um programa que receba uma lista de números e retorne a média dos valores presentes na lista.
"""
lista = []

while i != "":
    print("Digite um número para ser adicionado a lista: ")
    i = int(input())
    print("Para parar o programa, Digite 0.")
    lista.append(i)
    if i == 0:
        lista.pop()
        print(lista)
        break

def media_():
    soma_das_notas = sum(lista)
    qtd_de_notas = len(lista)
    mediaLista = soma_das_notas / qtd_de_notas
    print("A média é igual a:",mediaLista)

media_()
"""

#Verificar se um número é par ou ímpar: Desenvolva um programa que receba um número como entrada e determine se ele é par ou ímpar.
'''
x = int(input("Digite um número: ")) 
def num_par_impar():
    if x % 2 == 0:
        print("Seu número",x,"é par!")
    else:
        print("Seu número",x,"é impar!")
        
num_par_impar()
'''

#Converter temperatura de Celsius para Fahrenheit: Escreva um programa que converta uma temperatura em graus Celsius para Fahrenheit.
'''
celsius = float(input("Digite uma temperatura em Celsius para podermos converter em Fahrenheit: "))

def celsius_to_fahr():
    fahrenheit = celsius * 1.8 + 32
    print("O valor em Fahrenheit é:",fahrenheit)

celsius_to_fahr()
'''

#Calcular o fatorial de um número: Crie uma função que calcule o fatorial de um número dado como entrada.
'''
def fatorial_decrementando(numero):
    resultado = 1
    print(f'Calculando o fatorial de {numero} como: ', end='')
    while numero > 0:
        resultado *= numero
        print(numero, end='')
        if numero > 1:
            print(' x ', end='')
        else:
            print(' = ', end='')
        numero -= 1
    return resultado

numero = int(input("Digite um número para calcular o fatorial: "))
resultado_fatorial = fatorial_decrementando(numero)
print(resultado_fatorial)
'''

#Gerador de Senhas
'''
import random

print("Bem-vindo ao Gerador de Senhas!")
 
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

quant = input("Digite a quantidade de senhas a serem geradas: ")
quant = int(quant)

len = input("Digite o tamanho das senhas a serem geradas: ")
len = int(len)

print("Aqui estão suas senhas:")
for pwd in range(quant):
    passwords = ""
    for c in range(len):
        passwords += random.choice(chars)
    print(passwords)    
'''

#Dia 20/12

#1

'''
horas_trab = int(input("Digite a quantidade de horas trabalhadas: "))
valor_hora = int(input("Digite o quanto você ganha por hora: "))

def salario(horas_trab, valor_hora):
    horas_mes = horas_trab * 21
    salario_ =  valor_hora * horas_mes
    print(f'O seu salário é de R${salario_},00')

salario(horas_trab, valor_hora)
'''

#2
'''
horas_provas = int(input("Digite a quantidade de horas de prova: "))
mins_provas = int(input("Digite a quantidade de minutos de prova: "))


def hora_prova(horas_provas, mins_provas):
    prova_min = horas_provas * 60 + mins_provas
    prova_sec = prova_min * 60

    print(f'Você fez a prova em {prova_min} minutos')
    print(f'Você fez a prova em {prova_sec} segundos')

hora_prova(horas_provas, mins_provas)
'''

#3
'''
metros = float(input("Digite a quantidade de metros a ser convertida: "))

def metros_cm(metros):
    cm = metros * 100
    print(f'A quantidade em centímetros é de {cm} cm')
    
metros_cm(metros)
'''