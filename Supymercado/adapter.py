from core import CatalogoProdutos, EspecificacaoProduto, ItemVenda, Venda
from ports import CarregadorProdutosPort, InterfaceUsuarioPort, CatalogoPort, VendaPort

class CarregadorProdutosArquivo(CarregadorProdutosPort):
    def carregar_produtos(self) -> CatalogoPort:
        catalogo = CatalogoProdutos()
        try:
            with open("produtos.csv", "r") as arquivo:
                for linha in arquivo:
                    dados = linha.strip().split(',')
                    if len(dados) == 3:
                        try:
                            id = int(dados[0])
                            descricao = dados[1].strip()
                            preco = float(dados[2])
                            catalogo.adicionar_produto(EspecificacaoProduto(id, descricao, preco))
                        except ValueError:
                            print(f"Formato inválido na linha: {linha}")
            print("Catálogo carregado com sucesso!")
        except FileNotFoundError:
            print("Arquivo de produtos não encontrado!")
        return catalogo

class CLIInterfaceUsuario(InterfaceUsuarioPort):
    def __init__(self, catalogo: CatalogoPort):
        self.catalogo = catalogo
        self.venda_atual: VendaPort = None

    def iniciar_venda(self):
        self.venda_atual = Venda()

    def adicionar_item(self, codigo: int, quantidade: int):
        produto = self.catalogo.buscar_produto(codigo)
        if produto:
            item = ItemVenda(produto, quantidade)
            self.venda_atual.adicionar_item(item)
            print(f"Item adicionado: {produto.descricao} x{quantidade}")
        else:
            print("Produto não encontrado!")

    def finalizar_venda(self, valor_recebido: float):
        if self.venda_atual:
            total = self.venda_atual.total
            troco = self.venda_atual.calcular_troco(valor_recebido)
            print(f"\nTotal: R${total:.2f}")
            print(f"Troco: R${troco:.2f}")
            return troco
        return 0.0