##ORGANIZAR ARQUIVOS DE ACORDO DO TIPO (.pdf .img .txt .....)
import os
import shutil ##importante na movimentação dos arquivos (shutil.move)

def criar_diretorios(diretorios): ##função para criar diretorios
    for diretorio in diretorios:
        if not os.path.exists(diretorio):
            try:
                os.makedirs(diretorio)
                print(f"Diretorio {diretorio} criado.")
            except Exception as e:
                print(f"Não foi possivel criar o diretorio: {e}")   

def move_files(diretorio_origem):
    for arquivo in os.listdir(diretorio_origem):
        caminho_arquivo = os.path.join(diretorio_origem, arquivo)
        if os.path.isfile(caminho_arquivo):
               extensao = arquivo.split('.')[-1].lower()
               if extensao in ['pdf', 'txt', 'jpg']:
                   diretorio_destino = os.path.join(diretorio_origem, extensao)
                   try:
                       shutil.move(caminho_arquivo, diretorio_destino)
                       print(f"{arquivo} movido para {diretorio_destino}.")
                   except PermissionError:
                       print(f"Sem permissão para mover {arquivo}.")
                   except Exception as e:
                       print(f"Erro inesperado ao mover {arquivo}: {e}")
               else:
                   print(f"Extensão {extensao} de {arquivo} não é suportada.")
def main():
       diretorio_trabalho = "diretorio_trabalho"
       diretorios = [os.path.join(diretorio_trabalho, 'pdf'),
                     os.path.join(diretorio_trabalho, 'txt'),
                     os.path.join(diretorio_trabalho, 'jpg')]
 
       # Criar diretórios se não existirem
       criar_diretorios(diretorios)
 
       # Mover arquivos para os diretórios correspondentes
       move_files(diretorio_trabalho)
 
if __name__ == "__main__":
       main()