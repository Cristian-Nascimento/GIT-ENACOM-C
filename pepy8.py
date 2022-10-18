"""
PEP08 - Python enhancements proposal

1 - Utilize Camel case para nomes de classes

2 - Utilize nomes em minúsculo, separados por underline para funções ou variáveis

3 - Utilize quatro espaços para identação!

4 - Linhas em branco
        Separar funções e definições de classe com duas linhas em branco.
        Métodos dentro de uma classe devem ser separados com uma única linha em branco.

5 - Imports devem ser sempre separados em linhas separadas
        caso tenha muitos imports de um mesmo pacote, recomenda-se fazer:
            from types import {
                StringType,
                ListType,
                SetType,
                OutsType,
            }
        Imports devem ser colocados no topo do arquivo, logo depois de quaisquer comentários ou docstrings
        e antes de constantes ou variáveis globais.        

6 - Espaços em expressões e instruções
    certo: funcao(algo[1], {outro: 2}) errado: funcao ( algo [ 2 ] , { outro: 3 } )

7 - Termine sempre uma instrução com uma linha em branco
"""