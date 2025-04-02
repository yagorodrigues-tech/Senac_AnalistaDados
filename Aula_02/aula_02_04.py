#Crie um programa que calcule a idade de uma pessoa a partir do ano de nascimento dela

#Importando a biblioteca de data e hora
import datetime


#Entrada de Dados
data_atual= datetime.date.today()
ano_nasc = int (input('Informe o ano em que você nasceu:  '))
ano_atual = data_atual.year

#Processamento de Dados
idade = ano_atual - ano_nasc

#Saída de Dados
print( f'Você tem {idade:,.0f} anos de idade. ')