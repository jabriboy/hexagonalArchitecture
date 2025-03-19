from core.port.IVendaRepository import IVendaRepository

class RegistrarVendaUseCase:
    def __init__(self, venda_repository: IVendaRepository):
        self.venda_repository = venda_repository

    def execute(self, venda):
        # Lógica de negócio aqui
        self.venda_repository.save(venda)