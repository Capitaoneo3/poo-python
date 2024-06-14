#exemplo de fazer uma lista de objetos
class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
    def __repr__(self):
        return f"Pessoa(nome='{self.nome}', idade={self.idade})"
    
pessoa1 = Pessoa("alice",15)
pessoa2 = Pessoa("pedro",20)
Pessoa3 = Pessoa("otavio",18)

lista_pessoas = [pessoa1,pessoa2,Pessoa3]

for pessoa in lista_pessoas:
    print(f"nome:{pessoa.nome}, idade:{pessoa.idade}")

