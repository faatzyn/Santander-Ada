numero_sorteado = 15
numero_escolhido = int(input('Informe um número entre 1 e 20: '))

contador = 1
while numero_sorteado != numero_escolhido and contador < 5:
    numero_escolhido = int(input('Você errou, informe um número entre 1 e 20 novamente: '))
    contador+=1

print('Você acertou !!! Uhulll !' if numero_sorteado == numero_escolhido else 'Acabou as tentativas....')