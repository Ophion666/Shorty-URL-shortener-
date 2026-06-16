from pydantic import BaseModel, ConfigDict
from datetime import datetime


class ClickResponse(BaseModel):

    id: int

    link_id: int

    user_agent: str

    created_at: datetime

    model_config = ConfigDict(from_attributes=True)