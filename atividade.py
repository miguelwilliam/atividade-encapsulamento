class Integrante_IFRN():
    def __init__(self):
        pass

    def exibirMensagem(self):
        print('Seja bem vindo(a) ao IFRN!!!')

class Professor(Integrante_IFRN):
    def __init__(self):
        super().__init__()
    
    def exibirMensagem(self):
        print('Meus alunos são os melhores!!!')

class Aluno(Integrante_IFRN):
    def __init__(self):
        super().__init__()
    
    def exibirMensagem(self):
        print('Vou estudar pra tirar 100 em POO!!!')
