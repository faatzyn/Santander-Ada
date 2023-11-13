# Listas
notas = []
notas = list()
notas = [6,7,8,'Luiz', ['a',2,True]]

# Indexação
print(notas[0]) # 6
# print(notas[7]) # Erro, índice fora da faixa
print(notas[-1]) # Imprime o último elemento

# Slices
lista = [10,20,30,40,50,60,70,80,90,100]
print(lista[0:3]) # pega 3 elementos -> Começa do 0 e vai até 2 (0,1,2)
print(lista[2:6:2]) # do 2 até o anterior a 6, de 2 em 2

# Iteração com For
for elemento in lista:
    print(elemento)

# Utilizando o tamanho da lista
print(len(lista)) # tamanho lista
for i in range(len(lista)):
    print(i, lista[i])