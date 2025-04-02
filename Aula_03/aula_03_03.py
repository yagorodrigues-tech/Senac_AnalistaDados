# Escreva um programa que, dados 2 números inteiros (n1 e n2), diga se eles são iguais ou diferentes.
# Utilizando a estrutura do programa anterior, some os dois valores se forem diferentes e multiplique-os se forem iguais.


#Entrada de Dados
n1 = int (input('Informe o primeiro valor:  '))
n2 = int (input('Informe o segundo valor:  '))

#Processamento de Dados
if n1 ==n2:
    a = n1*n2
    print (f'Eles são iguais e multiplicados valem {a}. ')
else:
    a = n1+n2
    print(f'Eles são diferentes e somados valem {a}.')