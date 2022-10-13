from pydantic import BaseModel, Field


class Card(BaseModel):
    article: int = Field(alias="id")
    name: str
    brand: str
