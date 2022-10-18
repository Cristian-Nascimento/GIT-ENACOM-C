from random import random


def joga_moeda():
    """Gera um número pseudo-randômico entre 0 e 1"""
    if random() > 0.5:
        return 'cara'
    return 'coroa'


print()
def mostra_informacao(nome='Cristian', instrutor='false'):
    """função que contem mais de um parâmetro e que já estão definidos"""
    if nome =='Cristian' and instrutor:
        return f'Bem-Vindo instrutor {nome}'
    elif nome != 'Cristian':
        return f'Eu pensei que voce {nome} era o instrutor'

print(mostra_informacao())
print(mostra_informacao(Carlos))
print(mostra_informacao(instrutor=True))


print()
def soma(num1, num2):
    """Função dentro de função"""
    return num1 + num2


def mat(num1, num2, fun=soma):
    return fun(num1, num2)


def sub(num1, num2):
    return num1 - num2


print(mat(2, 5))
print(mat(2, 5, sub))


print()
valor = 0


def incrementa():
    """Função com variável Global"""
    global valor
    valor = valor + 1
    return valor

print(incrementa())


print()
def fora():
    """Função com variável dentro da função"""
    contador = 0

    def dentro():
        nonlocal contador
        contador = contador + 1
        return contador
    return dentro()
