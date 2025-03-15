import time
from caixa import CaixaSupermercado
from datetime import datetime
from typing import List

class Venda:
    def _init_(self):
        self.itens_de_venda: List[ItemDeVenda] = []
        self.data_hora = datetime.now()

    def incluir_item(self, espec_produto: CaixaSupermercado.EspecificacaoProduto, quant_prod: int):
        self.itens_de_venda.append(ItemDeVenda(espec_produto, quant_prod))

    def get_total(self) -> float:
        total = 0.0
        print(f"Total: {total}")
        time.sleep(1)
        for item in self.itens_de_venda:
            total += item.get_subtotal()
            print(f"Total: {total}")
            time.sleep(1)
        return total

    def get_troco(self, valor_pago: float) -> float:
        return valor_pago - self.get_total()


class ItemDeVenda:
    def _init_(self, espec_produto: CaixaSupermercado.EspecificacaoProduto, quant: int):
        self.quant = quant
        self.espec_produto = espec_produto

    def get_subtotal(self) -> float:
        sub_total = self.quant * self.espec_produto.get_preco()
        print(f"SubTotal: {sub_total}")
        time.sleep(1)
        return sub_total


# Exemplo de uso (para testar as classes)
if __name__ == "__main__":

    # Criando uma venda
    venda = Venda()

    # Criando alguns produtos
    produto1 = CaixaSupermercado.EspecificacaoProduto(10.0)
    produto2 = CaixaSupermercado.EspecificacaoProduto(20.0)

    # Incluindo itens na venda
    venda.incluir_item(produto1, 2)  # 2 unidades do produto1 (10.0 cada)
    venda.incluir_item(produto2, 1)  # 1 unidade do produto2 (20.0 cada)

    # Calculando o total da venda
    total = venda.get_total()
    print(f"Total da venda: {total}")

    # Calculando o troco
    troco = venda.get_troco(50.0)
    print(f"Troco: {troco}")