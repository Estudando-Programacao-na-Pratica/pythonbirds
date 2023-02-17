class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade

    # método
    def cumprimentar(self):
        return f'Olá {self.nome}! Idade: {self.idade} Id: {id(self)}'

if __name__ == '__main__':
    p = Pessoa('Leo', 26)
    print(p.cumprimentar())
    p.nome = 'Karine'
    p.idade = 24
    print(p.cumprimentar())