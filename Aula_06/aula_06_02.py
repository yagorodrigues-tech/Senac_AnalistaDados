#2- Faça um programa para uma loja de tintas, que solicite o tamanho em metros quadrados da
#área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que
#a tinta é vendida em latas de 18 litros, que custam R$ 130,00.
#Informe ao usuário a quantidade de latas de tinta a serem compradas e o valor a ser pago.


import math

#Entrada de Dados
mp = float (input('Informe o tamanho da área a ser pintada em metros quadrados:  '))

#Processamento de Dados
lt = (mp/3)/18
lt_arredondado = math.ceil (lt)
valor = lt_arredondado * 130


#Saída de Dados
print( f'Para fazer a pintura você irá precisar de {lt_arredondado:.2f} latas de tinta e o valor será de {valor:.2f} reais.')