#O Departamento Estadual de Meteorologia solicitou o desenvolvimento de um programa que
#leia um conjunto indeterminado de temperaturas, ao final informe a menor e a maior temperatura, bem
# como a média delas.

num = 0
soma = 0
temperaturas = []

#Entrada de Dados
while num >=0 :
    num = (float(input('Informe a temperatura (ou Digite -1 para encerrar) :  ')))
    if num == -1:
        break
    temperaturas.append(num)


#Processamento de Dados
if len(temperaturas) > 0:
    soma = sum(temperaturas)
    maior = max(temperaturas)
    menor = min(temperaturas)
    media = sum(temperaturas)/len(temperaturas)

#Saída de Dados
print(f'A menor temperatura registrada é {menor} graus Celsius. A maior temperatura registrada é {maior} graus Celsius. A média das temperaturas compiladas é {media:.2f} graus celsius. ')