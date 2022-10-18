"""
Levantando os próprios erros com raise

raise = Lança exceções

OBS: Raise não é uma função. É uma palavra reservada.

OBS: O Raise assim como o return, finaliza a função.

Para simplificar, pense no raise como sendo útil para que possamos criar nossas próprias exceções
e mensagens de erro.

a forma geral utilizada é:
    raise TipoErro ('Mensagem de erro')

# Exemplo 1

    Def color(texto, cor):
        if type(texto) ins not str:
            raise TypeError('Texto precisa ser uma string')
        if type(cor) ins not str:
            raise TypeError('Coro precisa ser uma string')
        print(f'O texto {texto} será impresso na cor {cor}')

    color('True',7)

# Exemplo 2

    def color(texto, cor):
        cores = ('verde', 'amarelo', 'azul', 'branco')
        if type(texto) is not str:
            raise TypeError('texto precisa ser uma string')
        if type(cor) is not str:
            raise TypeError('cor precisa ser uma string')
        if cor not in cores:
            raise ValueError(f'A cor precisa ser uma entre: {cores}')
        print(f'O texto {texto} será impresso na cor {cor}')
    
    color = ('ENACOM', 'azul')

"""