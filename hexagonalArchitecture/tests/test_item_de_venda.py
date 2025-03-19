import unittest
from domain.models.item_de_venda import ItemDeVenda
from domain.models.especificacao_produto import EspecificacaoProduto

class TestItemDeVenda(unittest.TestCase):

    def setUp(self):
        self.produto = EspecificacaoProduto(id_produto=1, descricao="Produto Teste", preco=10.0)
        self.quantidade = 2
        self.item_de_venda = ItemDeVenda(espec_produto=self.produto, quant=self.quantidade)

    def test_get_subtotal(self):
        expected_subtotal = self.produto.get_preco() * self.quantidade
        self.assertEqual(self.item_de_venda.get_subtotal(), expected_subtotal)

    def test_item_de_venda_initialization(self):
        self.assertEqual(self.item_de_venda.quant, self.quantidade)
        self.assertEqual(self.item_de_venda.espec_produto, self.produto)

if __name__ == '__main__':
    unittest.main()