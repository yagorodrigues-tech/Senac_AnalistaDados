# Escreva um programa que, dado 5 números inteiros calcule a soma deles e identifique o maior deles.

# Entrada de dados
soma = 0
maior = 0

#Procesamento dos Dados - Estrutura de Repetição
for i in range(5):
    n = int(input('Informe um valor inteiro: '))
    if n> maior:
        maior = n
    soma = soma + n

#Saída de Dados
print(f'A soma deles é {soma}.')
print(f'O maior número deles é {maior}.')