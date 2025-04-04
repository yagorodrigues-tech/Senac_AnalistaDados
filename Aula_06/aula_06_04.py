# Crie um programa que:
# 1- Peça ao usuário para digitar dez números inteiros e os armazene em uma lista.
#2- Exiba a lista completa.
# 3- Exiba o maior e o menor número da lista.
#4- Exiba a soma e a média de todos os números.

num = []
soma = 0

#Processamento dos dados
for i in range(10):
    num.append(int(input('Informe dez números inteiros. Digite um número e em seguida clique em "enter" para inserir um novo número: ')))

if len(num) > 0:
    soma = sum(num)
    maior = max(num)
    menor = min(num)
    media = sum(num)/len(num)

#Saída de Dados
print(f'O menor número digitado é {menor}. O maior número registrado é {maior} e a média de todos os números é {media:.2f}. ')