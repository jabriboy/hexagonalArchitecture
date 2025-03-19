from abc import ABC, abstractmethod
from typing import List
from domain.models.venda import Venda

class IVendaRepository(ABC):
    @abstractmethod
    def save(self, venda: Venda) -> None:
        pass

    @abstractmethod
    def find_by_id(self, venda_id: int) -> Venda:
        pass

    @abstractmethod
    def find_all(self) -> List[Venda]:
        pass

    @abstractmethod
    def delete(self, venda_id: int) -> None:
        pass