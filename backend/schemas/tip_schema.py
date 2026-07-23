from pydantic import BaseModel



class TipResponse(BaseModel):
    id: int
    title: str
    content: str
    image_url: str | None
    model_config = {
        "from_attributes": True
    }