#Faça um programa que obtenha o valor para a variável HT (horas trabalhadas no mês), obtenha o valor para a variável VH (valor hora trabalhada), obtenha o valor para a variável PD (percentual de desconto) e 
# calcule o salário bruto => SB = HT * VH, mais o total de desconto => TD = (PD/100)*SB e o salário líquido => SL = SB – TD.
# Apresentando ao final o Salário Liquido.


#Entrada de Dados
ht = float (input('Informe a quantidade de horas trabalhadas no mês:  '))
vh = float (input('Informe o valor da hora trabalhada em reais: '))
pd = float (input('Informe o percentual de desconto do seu salário:  '))

#Processamento de Dados
sb = ht*vh
td = (pd/100)*sb
sl = sb-td

#Saída de Dados
print( f'O seu salário bruto é de R$ {sb:.2f}, mas seu salário líquido é de R$ {sl:.2f}')