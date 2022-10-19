from pydantic import BaseModel, Field


class CardModel(BaseModel):
    article: int = Field(alias="id", default="Not found")
    name: str = "Not found"
    brand: str = "Not found"

    def __init__(self, **kwargs):
        try:
            kwargs["id"] = kwargs["data"]["products"][0]["id"]
            kwargs["name"] = kwargs["data"]["products"][0]["name"]
            kwargs["brand"] = kwargs["data"]["products"][0]["brand"]
        except Exception as e:
            print(e)
        super().__init__(**kwargs)
