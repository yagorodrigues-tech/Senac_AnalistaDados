#Programa Média

#Entrada de Dados
nome = input ('Informe o nome do estudante: ')
n1 = float (input(f" Informe a primeira nota do estudante {nome}: "))
n2 = float (input(f" Informe a segunda nota do estudante {nome}: "))
n3 = float (input(f" Informe a terceira nota do estudante {nome}: "))

#Processamento dos Dados
media = (n1+n2+n3)/3

#Saída de Dados
print(f'Sr(a) {nome} a sua nota foi {media:.1f}')