from abc import ABC, abstractmethod


class Arquivo(ABC):
    def __init__(self, nome:str = '', tam:int = 0, extensao: str = ''):
        self.nome = nome
        self.tamanho = tam / 1000000
        self.ext = extensao
        # construir nome completo apenas quando houver extensão
        self.nomec = f"{nome}.{extensao}({self.tamanho}MB)" if extensao else nome

    @abstractmethod
    def abrir(self):
        pass



class PDF(Arquivo):
    def __init__(self, nome, tam, extensao = 'pdf'):
        super().__init__(nome, tam, extensao)

    def abrir(self):
        print(f"Abrindo o arquivo '{self.nomec}' com Adobe Reader")



class DOC(Arquivo):
    def __init__(self, nome, tam, extensao = 'docx' ):
        super().__init__(nome, tam, extensao)

    def abrir(self):
        print(f"Abrindo o arquivo '{self.nomec}' com Word Express")

## DUCK TYPING
def abrir_arquivo(objeto):
    try:
        objeto.abrir()
    except:
        print(f'Nao consegui abrir {objeto.__class__.__name__}')


