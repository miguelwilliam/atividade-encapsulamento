class Jogo:
    def __init__(self, nome):
        self.__nome = nome
    
    @property
    def nome(self):
	    return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
jogo = Jogo(input('diz um jogo: '))
print(f'o nome do seu jogo é {jogo.nome}')
jogo.nome = 'GTA'
print(f'agora, o nome do seu jogo é {jogo.nome}')