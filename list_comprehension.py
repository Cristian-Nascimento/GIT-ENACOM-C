"""
List Comprehension
- Utilizando-o nós podemos gerar novas listas com dados processados a partir de outro iterável

# Sintaxe da List
[dado for dado in iterável]
"""

#exemplos

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

res = [numero * 10 for numero in numeros]

print(res)
print()

"""
Para entender o que está acontecendo vou dividir em duas partes1
1- For  numeros in numeros
2 - numero * 10
"""

equa = [num **3 for num in numeros]

print(equa)
print()

# List Comprehension vs Loop

# Loop
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
numeros_dobrados = []

for numero in numeros:
    numeros_dobrados.append(numero * 2)

print(numeros_dobrados)
print()

# List Comprehension
print([numero * 2 for numero in numeros])
print()

# Exemplos
# 1
nome = 'Cristian Nascimento'

print([letra.upper() for letra in nome])
print()

# 2
def caixa_alta(nome):
    nome = nome.replace(nome[0], nome[0].upper())
    return nome

amigos = ['cristian', 'ingryd', 'ana carolina', 'beatriz', 'natiely']

print([caixa_alta(amigo) for amigo in amigos])
print()

# 3
print([numero *3 for numero in range(1, 10)])
print()

# 4
print([bool(valor) for valor in [0, [], '', True, False, 1, 5.545]])
print()

# 5
print([str(numero) for numero in [1, 2, 3, 4, 5, 6, 7, 8, 9]])
print()

# 6
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

pares = [numero for numero in numeros if numero % 2 == 0]
impares = [numero for numero in numeros if numero % 2 != 0]

#Refatorando

# Qualquer número par módulo de 2 é 0, e 0 em Python é false. not False = True
pares = [numero for numero in numeros if not numero % 2]

# qualquer número impar módulo de 2 é 1, e 1 em Python é True
impares = [numero for numero in numeros if numero % 2]

