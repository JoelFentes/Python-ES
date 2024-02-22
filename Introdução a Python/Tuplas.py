
'''
tuple = ()

tuple = tuple + (1,)
tuple = tuple + ([2, 3, 4, 5, 6],)

print(tuple)

print(type(tuple))

tuple[1][2] = 100

print(tuple)
'''

""" 
tupla = ()

tupla = tupla + ('nome': "Joel", 'idade': 18,)

print(tupla) 
"""

#1.

""" tupla = (1, 3, 5, 2, 3, 5, 1, 1, 3,)

new_tupla = ()


for i in tupla:
    if i not in new_tupla:
        new_tupla = new_tupla + (i,)
 """
#2.

"""         
list = [1, 2, 3]
new_lista = []

for x in list:
    new_lista.append((x, x**3))
print(new_lista)

 """

#3.

string = "A casa é bonita, A casa é azul"
list_string = []
list_string.append(string.split(" "))
count = 0

#4.

flag = True

while flag == True:
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    notas = int(input("Digite a idade: "))

    aluno = [nome, idade, notas]

