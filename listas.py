from random import random

lista_1 = [1,50,18,67,5,0,6,438,850,10]

lista_1.sort()
print(lista_1)

curso = 'Programacao,em,Python'
curso = curso.replace(',' , ' ')

print(curso)

# Pode-se colocar qualquer tipo de dado em uma lista, idependente da ordem
lista_misturada = [1, 2.35, True, 'Cristian', [2, 4, 15]]

# Iterando sobre listas

for elemento in lista_misturada:
    print(elemento)

carr = []
produto = ''

while produto != 'sair':
    print('Adicione um produto; Digite "sair" para sair:')
    produto = input()
    if produto != 'sair':
        carr.append(produto)
    
for produto in carr:
    print(produto)

