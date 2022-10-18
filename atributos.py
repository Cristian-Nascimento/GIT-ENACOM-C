class Produto:
    #atributo de classe
    imposto = 1.05    # 0.05 % de imposto
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1    # Atualizando o valor do contador
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)    # Acessando o atributo valor para operacao de multiplicacao.
        Produto.contador = self.id    # O contador recebe o valor de 'self.id'

p1 = Produto('Computador', 'Gamer', 2500)

print(p1.nome)    #Acesso possivel, mas de forma incorreto
print(p1.valor)    #Acesso possivel

print(p1.id)

"""
Adicionando e Removendo atributo dinamicamente
"""

p1.peso = '25 kg'    # Adicionando o atributo dinamico peso

del p1.peso    # Removendo o atributo dinamico peso
