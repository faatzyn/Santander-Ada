nota = 0
for i in range(1,4):
    nota += float(input(f'Informa sua nota {i}:'))

print(f'Média: {nota/3:.2f}')