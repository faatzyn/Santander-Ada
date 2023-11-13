# Criando uma variável
"""
    Tipos de Variáveis
    1. int: números inteiros
    2. float: números reais, ou seja, parte decimal
    3. str: cadeia de caractéres, ou seja, dados textuais
    4. bool: valores lógicos, True ou False
"""
idade = 26 # idade recebe 26, int
altura = 1.72 # float
nome = 'Luiz' # nome recebe Luiz, str
estudando = True # bool

print(f'nome: {nome}, idade {idade}, altura {altura}, estudando ? {"sim " if estudando else "nao"}')
print(type(idade))
print(type(altura))
print(type(nome))
print(type(estudando))