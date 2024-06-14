class Computador:
    def __init__(self,cpu_p,qntd_memoria_p):
        self.cpu = cpu_p
        self.qntd_memoria =qntd_memoria_p
        self.ligado = False

    def ligar(self):
        self.ligado = True
        print("computador ligando")

    def desligar(self):
        self.ligado = False
        print("computador desligando")
   
class Pc_gammer(Computador):
    def __init__(self, cpu_p, qntd_memoria_p):
        super().__init__(cpu_p, qntd_memoria_p)
        self.jogando=False

    def iniciar_jogo(self):
        self.jogando = True
        print("iniciar jogo")
    def fechar_jogo(self):
        self.jogando = False
        print("fechar jogo")
   
meu_pc = Pc_gammer("i9 1000x","64GB")
print(f"os atributos ligado:{meu_pc.ligado} e jogando:{meu_pc.jogando}")
meu_pc.ligar()
meu_pc.iniciar_jogo()
print(f"os atributos ligado:{meu_pc.ligado} e jogando:{meu_pc.jogando}")
print(meu_pc.cpu)