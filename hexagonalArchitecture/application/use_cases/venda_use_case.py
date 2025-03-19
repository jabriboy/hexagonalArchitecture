from domain.models.venda import Venda
from application.interfaces.venda_repository import IVendaRepository

class VendaUseCase:
    def __init__(self, venda_repository: IVendaRepository):
        self.venda_repository = venda_repository

    def registrar_venda(self, venda: Venda):
        # Lógica para registrar a venda
        self.venda_repository.save(venda)

    def calcular_total_venda(self, venda: Venda) -> float:
        return venda.get_total()

    def calcular_troco(self, venda: Venda, valor_pago: float) -> float:
        return venda.get_troco(valor_pago)