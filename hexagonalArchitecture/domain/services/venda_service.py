from domain.models.venda import Venda
from application.interfaces.venda_repository import IVendaRepository

class VendaService:
    def __init__(self, venda_repository: IVendaRepository):
        self.venda_repository = venda_repository

    def registrar_venda(self, venda: Venda):
        # Aqui você pode adicionar lógica adicional antes de salvar a venda
        self.venda_repository.save(venda)

    def obter_venda_por_id(self, venda_id: int) -> Venda:
        return self.venda_repository.find_by_id(venda_id)

    def listar_vendas(self):
        return self.venda_repository.find_all()