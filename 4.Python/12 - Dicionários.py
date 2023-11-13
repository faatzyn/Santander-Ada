# Diferença entre lista e dicionário
# Valores únicos
# lista = [1,2,3]
# print(type(lista))
dicionario = {
    'nome':'Luiz',
    'idade':32
}
dicionario2 = dict()
# print(type(dicionario),type(dicionario2), dicionario, dicionario2)
# print(dicionario['idade']) # acessando um indice
dicionario['programador'] = True
dicionario['idade'] = 33 # sobrescreve o valor
print(dicionario)

# Percorrer um dict
for chave in dicionario:
    # for em um dict acessa os indices e não os valores
    print(dicionario[chave])

# Verificar se uma chave existe no dict
print('peso' in dicionario, 'idade' in dicionario)