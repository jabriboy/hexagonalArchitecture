import unittest
from domain.models.venda import Venda
from domain.models.item_de_venda import ItemDeVenda
from application.interfaces.venda_repository import IVendaRepository

class TestVenda(unittest.TestCase):

    def setUp(self):
        self.venda = Venda()
        self.item1 = ItemDeVenda("Produto A", 10.0, 2)  # 2 unidades de Produto A
        self.item2 = ItemDeVenda("Produto B", 20.0, 1)  # 1 unidade de Produto B
        self.venda.incluir_item(self.item1)
        self.venda.incluir_item(self.item2)

    def test_get_total(self):
        total = self.venda.get_total()
        self.assertEqual(total, 40.0)  # 2 * 10.0 + 1 * 20.0

    def test_get_troco(self):
        troco = self.venda.get_troco(50.0)
        self.assertEqual(troco, 10.0)  # 50.0 - 40.0

    def test_incluir_item(self):
        item3 = ItemDeVenda("Produto C", 15.0, 3)  # 3 unidades de Produto C
        self.venda.incluir_item(item3)
        total = self.venda.get_total()
        self.assertEqual(total, 85.0)  # 40.0 + 3 * 15.0

if __name__ == '__main__':
    unittest.main()