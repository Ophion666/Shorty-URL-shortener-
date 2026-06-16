from app.models.click import Click
from sqlalchemy.orm import Session

def create_click_record(db: Session, link_id: int, ip_address: str, user_agent: str):
    click_rec = Click(link_id = link_id, ip_address = ip_address, user_agent = user_agent)
    db.add(click_rec)
    db.commit()
    db.refresh(click_rec)
    return click_rec
