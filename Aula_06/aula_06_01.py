#Faça um programa que pergunte quanto um funcionário recebe por hora e o número de
#horas trabalhadas no mês. Calcule e mostre o total do seu salário, sabendo que são descontados 11%
#para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#a) salário bruto.
#b) Quanto pagou ao IRRF.
#c) quanto pagou ao INSS.
#d) quanto pagou ao sindicato.
#e) o salário líquido.

#Entrada de Dados
ht = float (input('Informe a quantidade de horas que você trabalhou no mês:  '))
vh = float (input('Informe o valor da sua hora trabalhada em reais: '))


#Processamento de Dados
sb = ht*vh
ir = sb* 0.11
inss = sb* 0.08
sind = sb*0.05
sl = sb-ir-inss-sind

#Saída de Dados
print( f'O seu salário bruto é de R$ {sb:.2f}, mas você teve descontos. Você teve de pagar {ir:.2f} reais de imposto de renda, mais {inss:.2f} reais de INSS e mais {sind:.2f} reais ao sindicato.')
print( f'Assim, seu salário bruto é de R$ {sb:.2f}, mas  salário líquido é de R$ {sl:.2f}.')