from abc import ABC, abstractmethod

from demo.schemas import EnrichResponse


class EnrichStrategy(ABC):
    flag_name: str  # contrato explícito

    @abstractmethod
    def enrich(self, documents: list[str]) -> list[str]:
        pass


class CadastroStrategy(EnrichStrategy):
    flag_name = "cadastro"

    def enrich(self, documents: list[str]) -> list[str]:
        return [f"cadastro_{doc}" for doc in documents]



class AgContaStrategy(EnrichStrategy):
    flag_name = "agencia_conta"

    def enrich(self, documents: list[str]) -> list[str]:
        return [f"agConta_{doc}" for doc in documents]
