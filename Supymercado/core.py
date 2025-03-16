from datetime import datetime
from abc import ABC, abstractmethod
from ports import CatalogoPort, VendaPort

# Implementações do Core
class EspecificacaoProduto:
    def __init__(self, id: int, descricao: str, preco: float):
        self.id = id
        self.descricao = descricao
        self.preco = preco

class CatalogoProdutos(CatalogoPort):
    def __init__(self):
        self.produtos = {}

    def adicionar_produto(self, produto: EspecificacaoProduto):
        self.produtos[produto.id] = produto

    def buscar_produto(self, id: int):
        return self.produtos.get(id)

class ItemVenda:
    def __init__(self, produto: EspecificacaoProduto, quantidade: int):
        self.produto = produto
        self.quantidade = quantidade

    @property
    def subtotal(self):
        return self.produto.preco * self.quantidade

class Venda(VendaPort):
    def __init__(self):
        self.data = datetime.now()
        self.itens = []

    def adicionar_item(self, item: ItemVenda):
        self.itens.append(item)

    @property
    def total(self):
        return sum(item.subtotal for item in self.itens)

    def calcular_troco(self, valor_recebido: float):
        return valor_recebido - self.total