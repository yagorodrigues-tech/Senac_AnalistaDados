# Escreva um programa que efetue o cálculo do valor de uma prestação em atraso, utilizando a fórmula: #valorfinal = prestacao+(prestacao*(taxa/100)*tempo)

#Entrada dos Dados
prestacao = float (input('Informe o valor da prestacao:  '))
taxa = float (input ('Informe a taxa em percentual:  '))
tempo = int(input ('Informe o atraso em dias:  '))

#Processamento dos Dados
juros = prestacao*(taxa/100)*tempo
valorfinal = prestacao + juros

#Saída dos Dados
print( f'Os juros da prestação são {juros:.2f}, portanto o valor final a ser pago será de R$ {valorfinal:,.2f}')