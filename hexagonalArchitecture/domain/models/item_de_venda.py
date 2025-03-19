class ItemDeVenda:
    def __init__(self, espec_produto, quant):
        self.quant = quant
        self.espec_produto = espec_produto

    def get_subtotal(self) -> float:
        return self.quant * self.espec_produto.get_preco()