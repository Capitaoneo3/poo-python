class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
    def diz_idade(self):
        print(f"a idade desse aluno é:{self.idade}")
    def diz_nome(self):
        print(f"o nome desse aluno é:{self.nome}")    

pessoa1 = Pessoa("joao",24)
pessoa1.diz_idade()
pessoa1.diz_nome()