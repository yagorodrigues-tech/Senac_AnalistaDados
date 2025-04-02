#Escreva um programa que leia um valor inteiro e apresente os resultados do quadrado e do cubo do valor lido


#Entrada de Dados
n = int (input('Informe um número inteiro:  '))

#Processamento de Dados
quadrado = pow(n,2)
cubo = pow (n,3)

#Saída de Dados
print( f' O quadrado do número é {quadrado:.1f} e o cubo do número é {cubo:.1f} ')