from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.link import LinkCreate, LinkResponse, LinkAnalyticsRespnse
from app.crud.crud_link import create_short_url, get_url_by_key


router = APIRouter(prefix="/links", tags = ["Links"])

@router.post("/link", response_model=LinkResponse)
def transform_link( link: LinkCreate, db: Session = Depends(get_db)):
    return create_short_url(db, link=link)


@router.get("/{shorty_key}/analytics", response_model=LinkAnalyticsRespnse)
def get_analytics(shorty_key: str, db: Session = Depends(get_db)):
    db_key = get_url_by_key(db=db, shorty_key=shorty_key)
    if not db_key:
        raise HTTPException(status_code=404, detail="Not Found")
    count = len(db_key.clicks)

    return LinkAnalyticsRespnse(id=db_key.id, original_url=db_key.original_url, shorty_key=db_key.shorty_key,
                                created_at=db_key.created_at, click_count=count, clicks=db_key.clicks)