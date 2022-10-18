# *args é um parâmetro, coloca os valores extras informados como entrada em uma tupla.
# Os parâmetros *args e **kwargs NÃO são obrigatórios!


def soma_numeros(*args):
    """Aplicando o *args, uma função contendo o *args pode receber n parâmetros"""
    return sum(args)

print(soma_numeros(4,5,9))
print(soma_numeros())


print()
def verifica(*args):
    """*args com Strings"""
    if 'Cristian' in args and 'ENACOM' in args:
        return f'Bem-Vindo Cristian a ENACOM!'
    return 'Eu não te conheço ué!'

print(verifica('José'))
print(verifica())
print(verifica(1, 'Cristian', 'ENACOM', True))


print()
# Aplicando desempacotador
def soma_todos_numeros(*args)
    """Aplicando desempacotador para poder concluir a função"""
    return sum(*args)

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(soma_todos_numeros(*numeros)) # Ao adiciona o '*' antes da variável, o mesmo é desempacotada!.

# **kwargs exige que utilizamos parâmetros nomeados, e transforma esses parâmetros extras em um dicionário.


def cores_favoritas(**kwargs):
    """Iterando no dicionário"""
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} é {cor}')

cores_favoritas(cristian='black', joão='Yellow', marcos='Brown', carol='Pink')


def cumprimento_especial(**kwargs):
    if 'Cristian' in kwargs and kwargs['Cristian'] == 'Python':
        return 'Voce recebeu um cumprimento Pythônico Cristian'
    elif 'Cristian' in kwargs:
        return f"{kwargs['Cristian']} Cristian!"
    return 'Não sei quem é você...'

print(cumprimento_especial())
print(cumprimento_especial(Cristian='Python'))
print(cumprimento_especial(Cristian='Oi'))
print(cumprimento_especial(Cristian='Especial'))

""" A ordem correta de parâmetros
1° parâmetros obrigatórios;
2° *args;
3° parâmetros (default) não obrigatórios;
4° **kwargs;
"""


# Desenpacotamento com **kwargs


def mostra_nomes(**kwargs):
    return f"{kwargs['nome'] {kwargs['sobrenome']}"


nomes = {'nome':'Cristian', 'sobrenome':'Nascimento'}

print(mostra_nomes(**nomes)) # Ao adicionar o '**' antes da variável, o mesmo é desempacotada!.
