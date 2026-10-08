




class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f"Produto: {self.nome}, Preço: {formatar_dinheiro(self.preco)}"



class Carrinho:
    def __init__(self, produtos:list=None):
        self.produtos = produtos if produtos else []

    @property
    def total(self):
        return sum(produto.preco for produto in self.produtos)

    def __add__(self, other):
        if isinstance(other, Produto):
            return Carrinho(self.produtos + [other])
        elif isinstance(other, Carrinho):
            return Carrinho(self.produtos + other.produtos)
        else:
            raise TypeError("Você tentou adicionar algo inválidoa o carrinho.")

    def __str__(self):
        produtos_str = "\n".join(str(produto) for produto in self.produtos)
        return f"Carrinho:\n{produtos_str}\nTotal: {formatar_dinheiro(self.total)}"



def formatar_dinheiro(valor:float):
    import locale
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    return locale.currency(valor, grouping=True)