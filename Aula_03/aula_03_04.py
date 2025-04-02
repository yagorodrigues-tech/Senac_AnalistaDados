#- Faça um programa que pergunte a uma pessoa: a sua idade, o seu peso e quanto dormiu nas últimas 24 h e diga se ela pode doar ou não sangue de acordo com as seguintes condições:
# Ter entre 16 e 69 anos.
# Pesar mais de 50 kg.
# Estar descansado (ter dormido pelo menos 6 horas nas últimas 24 horas).


#Entrada de Dados
idade = int (input('Informe a sua idade: '))
peso = float (input('Informe o seu peso em Kg: '))
t = int (input('Informe quanto tempo dormiu nas últimas 24h em horas: '))

#Processsamento de Dados

if idade < 16 or idade > 69 :
    print('Você não tem idade adequada para doar.')
elif peso < 50 :
    print('Você não tem o peso adequado para doar.')
elif t < 6 :
    print('Você não dormiu o suficiente para doar.')
else:
    print('Você está liberado para doar.')