from rich import print
from rich.traceback import install
install()



class Book:
    def __init__(self, name, npages):
        self.name  = name
        self.pages = npages
        self.current_page = 1
        print(f"[blue]Você acaba de abrir o livro [yellow]{self.name}[/] que possui ao todo [red]{self.pages} páginas[/]. [/]\nVocê está na [yellow]pagina 1[/]")

    def next(self, x = 1):
        if self.current_page == 20:
            print("Não é possivel avançar mais, limite de páginas atingido.")
        else:
            for i in range(1, x + 1):
                if self.current_page == self.pages:
                    print("[red]Você chegou ao final do livro.[/]")
                    break
                self.current_page += 1
                print(f"Página {self.current_page} -->", end= " ")
                
            print(f" Você avançou {x} páginas e agora está na página {self.current_page}.\n") 

        
        



b1 = Book("Chainsaw man", 20)
b1.next()
b1.next(16)
b1.next(4)

