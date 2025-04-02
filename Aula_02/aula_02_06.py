#Escreva um programa que calcule a velocidade média de um veículo com base na distância percorrida e no tempo em que uma viagem foi realizada.
#Com base nos dados obtidos no programa anterior e sabendo que o veículo usado consome 12 Km/l,construa um programa que determine a quantidade de combustível gasto nessa viagem.


#Entra de Dados
tempo = float (input('Informe a tempo da viagem em horas:  '))
distancia = float (input('Informe a distância percorrida em Km:  '))

#Processamento de Dados
velocid_media = (distancia/tempo)
quant_combustivel = (distancia/12)

#Saída de Dados
print( f'A velocidade média deste carro é de {velocid_media:,.1f} Km/h e consumiu {quant_combustivel: .1f} litros de combustivel')
