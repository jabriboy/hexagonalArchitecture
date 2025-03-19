from datetime import datetime

class ItemDeVenda:
    def __init__(self, espec_produto, quant):
        self.espec_produto = espec_produto
        self.quant = quant

    def get_subtotal(self) -> float:
        return self.quant * self.espec_produto.get_preco()


class Venda:
    def __init__(self):
        self.itens_de_venda = []
        self.data_hora = datetime.now()

    def incluir_item(self, espec_produto, quant_prod: int):
        self.itens_de_venda.append(ItemDeVenda(espec_produto, quant_prod))

    def get_total(self) -> float:
        total = sum(item.get_subtotal() for item in self.itens_de_venda)
        return total

    def get_troco(self, valor_pago: float) -> float:
        return valor_pago - self.get_total()