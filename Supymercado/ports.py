from abc import ABC, abstractmethod

# Portas do Core
class CatalogoPort(ABC):
    @abstractmethod
    def buscar_produto(self, id: int):
        pass
    
    @abstractmethod
    def adicionar_produto(self, produto):
        pass

class VendaPort(ABC):
    @abstractmethod
    def adicionar_item(self, item):
        pass
    
    @property
    @abstractmethod
    def total(self):
        pass
    
    @abstractmethod
    def calcular_troco(self, valor_recebido: float):
        pass

class CarregadorProdutosPort(ABC):
    @abstractmethod
    def carregar_produtos(self) -> CatalogoPort:
        pass

class InterfaceUsuarioPort(ABC):
    @abstractmethod
    def iniciar_venda(self):
        pass
    
    @abstractmethod
    def adicionar_item(self, codigo: int, quantidade: int):
        pass
    
    @abstractmethod
    def finalizar_venda(self, valor_recebido: float):
        pass
