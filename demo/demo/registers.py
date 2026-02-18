

from demo.enrich_strategy import AgContaStrategy, CadastroStrategy


STRATEGY_REGISTRY = {
    "cadastro": CadastroStrategy(),
    "agencia_conta": AgContaStrategy(),
}


def get_strategies():
    return STRATEGY_REGISTRY
