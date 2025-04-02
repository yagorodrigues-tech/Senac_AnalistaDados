#Construa um programa onde serão fornecidas duas notas de cada um dos dez alunos. Calcule a média de cada aluno e mostre a situação de cada aluno de acordo com as seguintes condições:
#- Se a média for maior igual a 70 -> ATENDIDO
#- Se a média for maior igual a 30 e menor que 70 -> PARCIALMENTE ATENDIDO
#- Se a média for menor que 30 -> NÃO ATENDIDO

# Entrada de dados
for i in range(3):
    nome = input('Informe o nome do usuário: ')
    nota_1 = float(input(f'Informe a primeira nota do aluno {nome} : '))
    nota_2 = float(input(f'Informe a primeira nota do aluno {nome} : '))
    media = (nota_1+ nota_2)/2

    if media >=70:
        situacao = 'ATENDIDO'
    elif media >=30 and media <70:
        situacao = 'PARCIALMENTE ATENDIDO'
    else:
        situacao = 'NAO ATENDIDO'

    print(f'Sr(a) {nome} a sua média foi {media}, portanto, sua situaçao é {situacao}.')



