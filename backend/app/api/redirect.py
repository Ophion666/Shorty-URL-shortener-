from fastapi import Depends, APIRouter, HTTPException, Request
from fastapi.responses import RedirectResponse
from app.crud.crud_link import get_url_by_key
from app.crud.crud_click import create_click_record
from app.db.session import get_db
from sqlalchemy.orm import Session
from app.models.click import Click

router = APIRouter(prefix="/r", tags=["Redirect"])

@router.get("/{shorty_key}")
def redirect(shorty_key: str, request: Request, db: Session = Depends(get_db)):
    key = get_url_by_key(db=db, shorty_key=shorty_key)
    if not key:
        raise HTTPException(status_code=404, detail="Not Found")
    else: 
        ip_address = request.client.host
        user_agent = request.headers.get("user-agent", "Unknown")
        create_click_record(db, link_id=key.id, user_agent=user_agent, ip_address=ip_address)
        return RedirectResponse(url=key.original_url, status_code=307)