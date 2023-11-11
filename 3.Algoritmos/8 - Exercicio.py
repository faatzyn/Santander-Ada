# INICIO MOSTRAR_MENU
#     VAR opcao_selecionado: STRING
#     MOSTRAR "Menu de operacao"
#     MOSTRAR "[a] Mostrar Saldo"
#     MOSTRAR "[b] Efetuar Deposito"
#     MOSTRAR "[c] Efetuar Saque"
#     MOSTRAR "[d] Finalizar"
#     ESPERAR_DIGITACAO -> opcao_selecionado
#     RETORNAR opcao_selecionado
# FIM MOSTRAR_MENU
def mostrarMenu():
    menu = '''
    Menu de operacao
    [a] Mostrar Saldo
    [b] Efetuar Deposito
    [c] Efetuar Saque
    [d] Finalizar
    '''
    print(menu)
    return input()

# INICIO principal
#     VAR opcao_selecionado: STRING
#     VAR valor: INTEIRO
#     VAR saldo: INTEIRO
#     VAR encerrar_programa: BOOLEANO

#     DEFINIR encerrar_programa -> Falso

#     ENQUANTO encerrar_programa IGUAL_A Falso
#         CHAMAR MOSTRAR_MENU -> opcao_selecionado

#         SE opcao_selecionado IGUAL_A a
#             MOSTRAR "Seu saldo é: ", saldo

#         OU_SE opcao_selecionado IGUAL_A b
#             MOSTRAR "Digite o valor a depositar: "
#             ESPERAR_DIGITACAO -> valor
#             SOMAR valor, saldo -> saldo
#             MOSTRAR "Deposito efetuado"

#         OU_SE opcao_selecionado IGUAL_A c
#             MOSTRAR "Digite o valor a retirar: "
#             ESPERAR_DIGITACAO -> valor

#             SE valor MAIOR_QUE saldo
#                 MOSTRAR "Saque nao permitido, saldo insuficiente"
#             SENAO
#                 SUBTRAIR valor, saldo -> saldo
#             FIM SE

#         OU_SE opcao_selecionado IGUAL_A d
#             DEFINIR Verdadeiro -> encerrar_programa
        
#         SENAO
#             MOSTRAR "Opcao invalida, tente novamente"
#         FIM SE
#     FIM ENQUANTO
# FIM
encerrar_programa = False
saldo = float(0)
while(encerrar_programa != 'd'):
    encerrar_programa = mostrarMenu()
    if encerrar_programa == 'a':
        print(f'Seu saldo é R$ {saldo:.2f}')

    elif encerrar_programa == 'b':
        saldo += float(input('Digite o valor a depositar: '))
        print('Deposito efetuado')

    elif encerrar_programa == 'c':
        valor = float(input('Digite o valor a retirar: '))

        if valor > saldo:
            print('Saque nao permitido, valor maior que saldo')
        else:
            saldo -= valor
            print('Saque efetuado com sucesso')

    elif encerrar_programa == 'd':
        print('Programa encerrado com suceso')

    else:
        print('Opcao invalida')


    print(encerrar_programa)
    
