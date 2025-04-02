# Exemplos de utilização do if,else e elif.

#Entrada de Dados
idade = int( input('Informe a sua idade: '))
if idade <18 :
    print ('Você é menor de idade')
elif idade == 18 :
    print('Você tem exatos 18 anos - Acesso liberado')
elif idade > 18 and idade < 65:
    print('Acesso liberado')
elif idade >= 65 :
    print('Você tem mais de 65 anos - Acesso liberado')
else: 
    print ('Acesso liberado')