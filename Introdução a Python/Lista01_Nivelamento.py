# Lista 01 - Nivelamento
# Aluno: Joel Oliveira Fentes da Cunha

""" 1. Faça um programa que leia um número inteiro e o imprima.

a = int(input("Escreva um número inteiro: "))
print(f'Seu número é: {a}')

2. Peça ao usuário para digitar três valores inteiros e imprima a soma deles.  
n1 = int(input("Escreva um número inteiro: "))
n2 = int(input("Escreva mais um número inteiro: "))
n3 = int(input("Escreva mais um número inteiro: "))

print(f'A soma dos números é: {n1 + n2 + n3}')

3. Desenvolva um algoritmo em python que leia um número inteiro e imprima o seu antecessor e seu sucessor. 

num = int(input("Escreva um número inteiro: "))
print(f'O antecessor do número é: {num - 1 }, O sucessor do número é: {num + 1}')

4. Leia uma temperatura em graus Celsius e apresente-a convertida em graus Fahrenheit. A fórmula de conversão é: F = C*(9.0/5.0)+32.0, sendo F a
temperatura em Fahrenheit e C a temperatura em Celsius.  

C = float(input("Escreva uma temperatura em graus celsius: "))
F = C*(9/5) + 32
print(f'A temperatura em Fahrenheit é: {F}ºF') 

 5. Leia uma velocidade em km/h (quilômetros por hora) e apresente-a convertida em m/s (metros por segundo). A fórmula de conversão é: M = K*3.6, sendo K a velocidade em km/h e M em m/s. 

K = float(input("Digite uma velocidade em km/h: "))
M = K*3.6
print(f'Sua velocidade em m/s é: {M}')


 6. Leia quatro notas, calcule a média aritmética e imprima o resultado.  

n1 = int(input("Escreva uma nota: "))
n2 = int(input("Escreva mais uma nota: "))
n3 = int(input("Escreva mais uma nota: "))
n4 = int(input("Escreva mais uma nota: "))
media = (n1 + n2 + n3 + n4)/4
print(f'Sua média é: {media}')


 7. Leia um valor em real e a cotação do dólar. Em seguida, imprima o valor correspondente em dólares. 

rs = float(input("Escreva um valor em dinheiro(R$): "))
dolar = float(input("Escreva o valor do dolár hoje: "))
print(f'O valor em dólar é: {rs*dolar}$') 
 
 8. Leia o valor do raio de um círculo e calcule e imprima a área do círculo correspondente. A área do círculo é π*r2 , considere π = 3.141592.  

r = float(input("Escreva o valor do raio: "))
area = 3.141592*(r*r) 
print(f'A área do círculo é: {area}') 


 9. A importância de R$ 780.000,00 será dividida entre três ganhadores de um concurso. Sendo que da quantia total: 
- O primeiro ganhador receberá 46%; - O segundo receberá 32%; - O terceiro receberá o restante;
Calcule e imprima a quantia ganha por cada um dos ganhadores. 

p = 780.000
g1 = p*0.46
g2 = p*0.32
g3 = p*0.22

print(f'O prêmio é de: {p}\nO primeiro ganhador ganhará: {g1}00,00\nO segundo ganhador: {g2}00,00\nO terceiro: {g3}00,00')

 10. Faça um programa que leia um número e, caso ele seja positivo, calcule e mostre: - O número digitado ao quadrado - A raiz quadrada do número digitado 

num = float(input("Digite um número qualquer: "))
if num > 0:
    v1 = num*num
    v2 = num ** 0.5
    print(f'R1: {v1}\nR2: {v2}')
else:
    print(f'Valor negativo :(')


 11. Faça um programa que receba um número inteiro e verifique se este número é par ou ímpar, positivo ou negativo.  

num = int(input("Digite um número qualquer: "))

if num > 0:
    print(f'O número {num} é positivo')
else:
    print(f'O número {num} é negativo')

if num % 2 == 0:
    print(f'O número {num} é par')
else:
    print(f'O número {num} é impar')


 12. Faça um programa que leia 2 notas de um aluno, verifique se as notas são válidas e exiba na tela a média destas notas. Uma nota válida deve ser, obrigatoriamente, um valor entre 0.0 e 10.0, onde caso a nota não possua um
valor válido, este fato deve ser informado ao usuário e o programa termina.  

n1 = float(input("Digite uma nota de 0.0 a 10.0: "))
n2 = float(input("Digite uma nota de 0.0 a 10.0: "))

if ((n1 or n2 < 0) or (n1 or n2 > 10)):
    print('Número digitado não permitido, por favor digite um valor válido. ')
else: 
    media = (n1 + n2)/2
    print(f'Sua média é: {media}')  

 13. Faça um programa que receba a altura e o sexo de uma pessoa e calcule e
mostre seu peso ideal, utilizando as seguintes fórmulas (onde h corresponde à altura): - Homens: (72.7 * h) − 58 - Mulheres: (62, 1 * h) − 44, 7 

h = float(input("Digite sua altura em metros: "))
sexo = input("Digite seu sexo, 'Masculino' ou '1' e 'Feminino' ou '2': ")

if sexo == "Masculino" or sexo == "masculino" or sexo == "1": 
    result = (72.7 * h) - 58
    print(f'Seu peso ideal é: {result}')
else:
    result = (62.1 * h) - 44
    print(f'Seu peso ideal é: {result}')



 14. A nota final de um estudante é calculada a partir de três notas atribuídas entre o intervalo de 0 até 10, respectivamente, a um trabalho de laboratório, a uma avaliação semestral e a um exame final. A média das três notas mencionadas
anteriormente obedece aos pesos: Trabalho de Laboratório: 2; Avaliação Semestral: 3; Exame Final: 5. De acordo com o resultado, mostre na tela se o aluno está reprovado (média entre 0 e 2,9), de recuperação (entre 3 e 4,9) ou se
foi aprovado. Faça todas as verificações necessárias. 

 n1 = float(input("Digite uma nota de 0.0 a 10.0: "))
n2 = float(input("Digite uma nota de 0.0 a 10.0: "))
n3 = float(input("Digite uma nota de 0.0 a 10.0: "))
p1 = 2
p2 = 3
p3 = 5

media_pond = (n1*p1 + n2*p2 + n3*p3)/ 10
if media_pond <= 2.9:
    print(f'Sua média foi {media_pond}, você reprovou! :(')
if media_pond >= 3 and media_pond <= 4.9:
    print(f'Sua média foi {media_pond}, você ficou de recuperação! Não desista!!')
if media_pond >= 5:
    print(f'Parabéns, {media_pond} você foi aprovado!') 


 15. Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As
perguntas são:

- "Telefonou para a vítima?"
- "Esteve no local do crime?"
- "Mora perto da vítima?"
- "Devia para a vítima?"
- "Já trabalhou com a vítima?"

O programa deve no final emitir uma classificação sobre a participação da
pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser
classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".  

print("Responda positivamente com sim, ou negue com não as perguntas a seguir: ")
print("Você telefonou para a vítima? ")
print("Você esteve no local do crime? ")
print("Você mora perto da vítima? ")
print("Você devia para a vítima? ")
print("Você já trabalhou com a vítima? ")

contador = 0
x = 0
for i in range(5):
    res = input('Resposta: ')
    if res == "sim":
        contador += 1
    if res != "sim" and res != "não":
        print("Resposta não computada, por favor, responda somente com sim ou não.")        

if contador == 2:
    print("Você está classificado como suspeito")

if contador == 3 or contador == 4:
    print("Você está classificado como cúmplice")

if contador == 5:
    print("Você está classificado como ASSASSINO") """ 


""" 16. Leia a idade e o tempo de serviço de um trabalhador e escreva se ele pode ou
não se aposentar. As condições para aposentadoria são: - Ter pelo menos 65 anos, - Ou ter trabalhado pelo menos 30 anos, - Ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos. """

""" age = int(input("Digite sua idade: "))
tempo_contri = float(input("Digite seu tempo de contribuição: "))

if age >= 65:
    print(f'Sua idade é de: {age} anos, você está apto a aposentadoria')
if tempo_contri >= 30:
    print(f'Seu tempo de contribuição é de: {tempo_contri} anos, você está apto a aposentadoria')
if age >= 60 and tempo_contri >= 25:
    print(f'Você está apto a aposentadoria') """


""" 17. Leia a distância em Km e a quantidade de litros de gasolina consumidos por um
carro em um percurso, calcule o consumo em Km/l e escreva uma mensagem de
acordo com a tabela abaixo: """
""" 
km = float(input("Digite a distância do trajeto em Km: "))
gas = float(input("Digite a quantidade de litros consumidos no percurso: "))

km_por_litro = km / gas

if km_por_litro < 8:
    print(f'Venda o carro, consumo de: {km_por_litro} km/l')

if km_por_litro >= 8 and km_por_litro <= 12: 
    print(f'Econômico, consumo de: {km_por_litro} km/l')

if km_por_litro > 12:
    print(f'Super econômico, consumo de: {km_por_litro} km/l') """

""" 18. Escreva um programa que escreva na tela, de 1 até 100, de 1 em 1, 2 vezes. A primeira vez deve usar a estrutura de repetição “for”, a segunda vez a estrutura
“while”.  """

for i in range (101):
    print(i)

x = 0

while x < 101:
    x += 1


""" 19. Faça um programa que peça ao usuário para digitar 10 valores e some-os e imprima o resultado.  """

soma = 0

for i in range(10):
    n = int(input("Digite um valor para a soma: "))
    soma += n
    print(soma)


""" 20. Faça um programa que leia 10 inteiros e imprima sua media.  """


soma = 0
media = 0


for i in range(10):
    n = int(input("Digite um valor para a soma: "))
    soma += n
    print(soma)

media = soma/10
print(f'Sua média é: {media}')


""" 21. Faça um programa que leia 10 inteiros positivos, ignorando não positivos, e
imprima sua média.  """

soma = 0
media = 0

for i in range(10):
    n = int(input("Digite um valor para a soma: "))
    if n > 0:
        soma += n
        print(soma)

media = soma/10
print(f'Sua média é: {media}')

""" 22. Faça um programa que leia um numero inteiro “N” e depois imprima os N
primeiros números naturais ímpares.  """

n = int(input("Digite um número para receber essa mesma quantidade de números ímpares: "))
x = -1

for i in range(n):
    x +=2
    print(x)


""" 23. Faça um programa que leia um numero inteiro positivo “N” e imprima todos os números naturais de 0 até “N” em ordem crescente. """

n = int(input("Digite um número para receber essa mesma quantidade de números crescente: "))
x = 0

for i in range(n):
    x +=1
    print(x)

""" 24. Faça um programa que leia um numero inteiro positivo “N” e imprima todos os
números naturais de 0 até N em ordem decrescente.  """

n = int(input("Digite um número para receber essa mesma quantidade de números crescente: "))
x = 0

for i in range(n, 0):
    x -=1
    print(x)

""" 25. Faça um programa que receba dois números. 

Calcule e mostre: 
- a soma dos números pares desse intervalo de números, incluindo os números
digitados; 
- a multiplicação dos números ímpares desse intervalo, incluindo os digitados; """



""" 26. Faça um programa que imprima a tabuada de multiplicação de 1 a 9; """

""" 27. Escreva um programa que leia um numero inteiro positivo “N” e em seguida
imprima “N” linhas do chamado Triângulo de Floyd. Para n = 6, temos:  """