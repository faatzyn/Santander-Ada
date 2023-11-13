def maior_de_idade():
    print('Digite sua idade: ')
    idade = int(input())

    if (idade >= 18 ):
        print('Maior de idade.')
    else:
        print('Ainda não é maior de idade.')
# maior_de_idade()

def media():
    print('Digite sua média: ')
    media = float(input())
    print('Qual o porcentual de presença (entre 0 e 100): ')
    presenca = float(input())

    if (media >= 7 and presenca >= 70):
        print('Você foi aprovado !!!!')
    elif (media >= 5 and presenca >= 50):
        print('Foi para recuperação :X')
    else:
        print('Você foi reprovado. :(')

media()