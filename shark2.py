class Shark():
    def nadar(self):
        print("o tubarão está nadando.")

    def nadar_de_costas(self):
        print("o tubarão não nadar para trás, mas pode afundar para trás.")

    def esqueleto(self):
        print("o esqueleto do tubarão é feito de cartilagem.")

class Clowfish:
    def nadar(self):
        print("o Peixe-palhaço estã nadando.")
    def nadar_de_costas(self):
        print("o Peixe-palhaço pode nadar para trás.")
    def esqueleto(self):
        print("o esqueleto do Peixe-Palhaço é feito de osso.")

def polimorfismo_peixe(peixe):
    peixe.nadar()
    peixe.nadar_de_costas()
    peixe.esqueleto()

shark = Shark()
clowfish = Clowfish()


polimorfismo_peixe(shark)
polimorfismo_peixe(clowfish)


for peixe in (shark,clowfish):
    peixe.nadar()
    peixe.nadar_de_costas()
    peixe.esqueleto()

