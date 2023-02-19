class Pessoa:
    olhos = 2  # #atributo defaut ou de classe

    def __init__(self, *filhos, nome=None, idade=None):
        # atributos de instância
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    # método
    def cumprimentar(self):
        return f'Olá {self.nome}! Idade: {self.idade} Id: {id(self)}'

    # método estático (pode ser executado pela instância ou pela classe)
    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos: {cls.olhos}'

    """Ordem de busca do atributo:
    1º olha na instância (esta no __init__())
    2º olha na classe"""


if __name__ == '__main__':
    p = Pessoa('Luiz', 'Luana', nome='Leo', idade=26)
    p.filhos.append(Pessoa(nome='Lucas', idade=10))  # um objeto também pode ser adicionado na lista
    print(p.cumprimentar())
    p.nome = 'Karine'
    p.idade = 24
    print(p.cumprimentar())
    print(p.filhos)

    p.sobrenome = 'Fernandes'
    print(p.__dict__)

    print(Pessoa.olhos)
    print(p.olhos)

    print(p.metodo_estatico(), p.nome_e_atributos_de_classe())
    print(Pessoa.metodo_estatico(), Pessoa.nome_e_atributos_de_classe())