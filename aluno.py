class Aluno:
    def __init__(self,idade):
        self.idade = idade
       
    def diz_idade(self):
        print(f"a idade desse aluno é:{self.idade}")

# Exemplo de uso da classe Aluno
aluno1 = Aluno(20)

aluno1.diz_idade()
