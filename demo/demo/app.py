from http import HTTPStatus
from demo.enrich_strategy import AgContaStrategy, CadastroStrategy
from demo.registers import get_strategies
from demo.schemas import EnrichResponse, EnrichSchema, Message
from fastapi import Depends, FastAPI


app = FastAPI()


@app.get("/", status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return Message(msg="hello world")


@app.post("/enrich", status_code=HTTPStatus.OK,response_model=EnrichResponse)
def enrich_data(enrich: EnrichSchema, strategies: dict = Depends(get_strategies)):

    response_flags = {}

    for flag_name, enabled in enrich.flags.items():
        if enabled and flag_name in strategies:
            strategy = strategies[flag_name]
            result = strategy.enrich(enrich.documents)
            response_flags[strategy.flag_name] = result
            

    return EnrichResponse(documents=enrich.documents, flags=response_flags)
