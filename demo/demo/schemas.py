from pydantic import BaseModel


class Message(BaseModel):
    msg: str


class EnrichSchema(BaseModel):
    documents: list[str]
    flags: dict[str, bool]


class EnrichResponse(BaseModel):
    documents: list[str]
    flags: dict[str, list[str]]
