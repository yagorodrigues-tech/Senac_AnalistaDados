#2- Faça um programa que receba do usuário o nome e a idade de 3 pessoas. Ao final mostre a soma e a média das idades.

# Entrada de dados
soma = 0
maior_idade = 0
menor_idade = 200

#Processamento de Dados
for i in range(3):
    nome = input('Informe o nome do usuário: ')
    idade = int(input('Informe a idade do usuário: '))
    if idade> maior_idade:
        maior_idade = idade
        maior_nome = nome

    if idade < menor_idade:
        menor_idade = idade
        menor_nome = nome
       
    soma = soma + idade


#Saída de Dados
print(f'A soma das idades foi {soma}.')
print(f'A média das idades foi {(soma / (i+1)):.2f} anos.')
print(f'A pessoa com maior idade se chama {maior_nome}. E sua idade é {maior_idade} anos.')
print(f'A pessoa com menor idade se chama {menor_nome}. E sua idade é {menor_idade} anos.')