#Nesse exemplo, identifique se o usuário é feminino ou masculino utlizando o comando if, else ou elif.
#Exercício: Tendo como dado de entrada à altura (h) de uma pessoa, construa um programa que calcule seu peso ideal, utilizando as seguintes fórmulas:
#* Para homens: (72.7*h) - 58
#* Para mulheres: (62.1*h) - 44.7


#Entrada dos Dados
altura = float(input('Informe a sua altura em metros: '))
sexo = (input('Informe o seu gênero: M para masculino ou F para feminino: '))

#Processamento dos Dados
if sexo == 'M' or sexo =='m':
    h = (72.7*altura) - 58
    print(f' O peso ideal para homens é {h:.0f} Kg.')
elif sexo == 'F' or sexo == 'f':
    m = (62.1*altura) - 44.7
    print(f' O peso ideal para mulheres é {m:.1f} Kg.')
else:
    print ('Verifique o sexo informado. Tente novamente usando M ou F.')
