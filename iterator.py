class Contador:
    def __init__(self, menor, maior):
        """Construct do método para criar um objeto a partir da classe"""
        self.menor = menor
        self.maior = maior

    def __inter__(self):
        """Declarando o metodo como iterator"""
        return self

    def __next__(self):
        """Criando o iterator"""
        if self.menor < self.maior:
            numero = self.menor
            self.menor = self.maior + 1
            return numero
        raise StopIteration

con = Contador(1, 61)

it = iter(con)

print(next(it))
