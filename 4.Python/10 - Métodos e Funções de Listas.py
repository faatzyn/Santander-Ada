# Métodos
lista = [12,2,32,48,5,6,7,8,9]
print('Antes do append:', lista)

# Append
# Adiciona um elemento no final da lista
lista.append(10)
print('Depois do append:', lista)

# Insert
# Escolho a posição que vou jogar o novo elemento
lista.insert(2, 2.5)
print('Depois do insert:', lista)

# Extend
lista2 = [20,30,40]
# Juntar duas lista, jogando no final da primeira lista
lista.extend(lista2)
print('Depois do extend:', lista)

# Pop
# Remover o ultimo item da lista se não passar o indice
lista.pop()
print('Depois do pop():', lista)
lista.pop(0)
print('Depois do pop(0):', lista)

# Remove
# Eu passo o valor que eu quero retirar
lista.remove(2.5)
print('Depois do remove(2.5):', lista)
# sempre remove o primeiro que encontra

# Count
# Contar quantas vezes um elemento aparece na lista
print('Quantidade de 2 na lista:', lista.count(2))

# index
# Retorna o indice do elemento
print('index de 2 na lista:', lista.index(2))

# sort
# Ordena a lista de forma crescente se vazio
lista.sort()
print('sort lista:', lista)
lista.sort(reverse=True) # trás para frente
print('sort(reverse=True) lista:', lista)


# FUNÇÔES DE LISTA
# len()
# retorna o tamanho da lista
print('len()',len(lista))

# sum()
# retorna a soma da lista
print('sum()',sum(lista))

# max()
# pega o maior valor da lista
print('max()',max(lista))

# min()
# pega o menor valor da lista
print('min()',min(lista))