#1.
'''
l = float(input("Digite o valor do lado do quadrado em cm: "))

def area_quad(l):
    area = l ** 2
    print(f'A área do quadrado é de {area} cm quadrados')

area_quad(l)
'''
#2. 

'''
b = float(input("Digite o valor da base do triangulo em cm: "))
h = float(input("Digite o valor da altura do triangulo em cm: "))

def area_tr(b, h):
    area = b * h / 2
    print(f'Sua área do triangulo é de{area} cm quadrados')

area_tr(b, h)
'''

#3.
'''
r = float(input("Digite o valor do raio do circulo em cm: "))
PI = 3.14159265359

def circulo_(r, PI):
    area_circulo = PI*r**2
    diametro_circulo = 2*r
    perimetro_circulo = 2*PI*r
    print(f'A área do seu circulo é {area_circulo} cm quadrados; \nO diâmetro do circulo é {diametro_circulo} cm; \nO perimetro do circulo é {perimetro_circulo} cm')

circulo_(r, PI)
'''
#4.

area_pintar = float(input("Digite a quantidade de metros quadrados que necessita ser pintado: "))

def loja_tintas(area_pintar):
    lata_tinta = 54
    area_sobra = 0
    latas_necessarias = 1
    if(area_pintar > lata_tinta):
      area_sobra = area_pintar - lata_tinta
      while area_sobra >= 0:
        area_sobra -= lata_tinta
        latas_necessarias += 1
    print(f'Você precisará de {latas_necessarias} latas e gastará um total de R${latas_necessarias*80},00') 

loja_tintas(area_pintar)