# Faça um programa que leia uma temperatura em graus Celsius e apresente-a convertida em graus Fahrenheit. A fórmula de conversão é: 
# F = (9 * C + 160) / 5, na qual F é a temperatura em Fahrenheit e C é a temperatura em Celsius;

#Entrada de Dados
temp_celsius = float (input('Informe a temperatura em Celsius:  '))

#Processamento de Dados
temp_fahrenheit = (9* temp_celsius + 160)/5

#Saída de Dados
print( f'Essa temperatura corresponde a {temp_fahrenheit:,.1f} graus em Fahrenheit. ')
