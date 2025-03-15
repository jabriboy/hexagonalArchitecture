import time
from typing import Dict
from venda import Venda

class CaixaSupermercado:
    def _init_(self):
        self.registra = Registradora()

    def constroi_catalogo_produtos(self):
        try:
            with open("src/Supermercado/ArqEspecProds", "r") as arquivo:
                for linha in arquivo:
                    tokens = linha.strip().split(",")
                    if len(tokens) != 3:
                        print(f"Desconsiderando linha mal formatada: {linha}")
                        continue
                    try:
                        id_produto = int(tokens[0])
                        descricao = tokens[1]
                        preco = float(tokens[2])
                        self.registra.incluir_espec_prod(id_produto, descricao, preco)
                    except ValueError:
                        print(f"Desconsiderando linha mal formatada: {linha}")
        except IOError as e:
            print(f"Erro ao ler o arquivo: {e}")

        print("Arquivo lido...")
        for id_produto in [1, 2, 3, 4]:
            espec_prod = self.registra.get_cat_prod().get_espec_prod(id_produto)
            if espec_prod:
                print(espec_prod)

    def iniciar_venda(self):
        self.registra.iniciar_venda()
        encerra_venda = False
        while not encerra_venda:
            print("Digite 1 para incluir produto; 2 para concluir venda")
            opcao_venda = int(input())
            if opcao_venda == 1:
                print("Digite o código do produto")
                cod_prod = int(input())
                print("Digite o número de unidades")
                quant_prod = int(input())
                self.registra.incluir_item(cod_prod, quant_prod)
            elif opcao_venda == 2:
                total = self.registra.get_total()
                print(f"Total venda: {total}")
                print("Informe o valor pago")
                valor_pago = float(input())
                troco = self.registra.get_troco(valor_pago)
                print(f"Troco = {troco}")
                encerra_venda = True
            else:
                print("Opção inválida")

    @staticmethod
    def main():
        meu_caixa = CaixaSupermercado()
        meu_caixa.constroi_catalogo_produtos()
        termina = False
        while not termina:
            print("Selecione 1 para nova venda, 2 para encerrar")
            opcao = int(input())
            if opcao == 1:
                meu_caixa.iniciar_venda()
            elif opcao == 2:
                print("Tchau")
                termina = True
            else:
                print("Opção inválida")


class Registradora:
    def _init_(self):
        self.cat_prod = CatalogoProdutos()
        self.venda = None

    def get_cat_prod(self):
        return self.cat_prod

    def incluir_espec_prod(self, id_produto, descricao, preco):
        self.cat_prod.incluir_espec_prod(id_produto, descricao, preco)

    def iniciar_venda(self):
        self.venda = Venda()

    def incluir_item(self, cod_prod, quant_prod):
        espec_prod = self.cat_prod.get_espec_prod(cod_prod)
        if espec_prod:
            self.venda.incluir_item(espec_prod, quant_prod)

    def get_total(self):
        return self.venda.get_total()

    def get_troco(self, valor_pago):
        return self.venda.get_troco(valor_pago)


class CatalogoProdutos:
    def _init_(self):
        self.mapa_especs: Dict[int, EspecificacaoProduto] = {}

    def get_espec_prod(self, id_produto):
        return self.mapa_especs.get(id_produto)

    def incluir_espec_prod(self, id_produto, descricao, preco):
        espec_prod = EspecificacaoProduto(id_produto, descricao, preco)
        self.mapa_especs[id_produto] = espec_prod


class EspecificacaoProduto:
    def _init_(self, id_produto, descricao, preco):
        self.id_produto = id_produto
        self.descricao = descricao
        self.preco = preco

    def get_descricao(self):
        return self.descricao

    def get_preco(self):
        print(f"Preço: {self.preco}")
        time.sleep(1)
        return self.preco

    def _str_(self):
        return f"{self.id_produto} {self.descricao} {self.preco}"


if __name__ == "__main__":
    CaixaSupermercado.main()