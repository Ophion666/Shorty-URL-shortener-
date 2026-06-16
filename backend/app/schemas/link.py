from pydantic import BaseModel, ConfigDict
from datetime import datetime
from app.schemas.click import ClickResponse


class LinkCreate(BaseModel):
    original_url : str


class LinkResponse(BaseModel):
    id: int

    original_url: str

    shorty_key: str

    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class LinkAnalyticsRespnse(LinkResponse):
    click_count: int

    clicks: list[ClickResponse] = []