from sqlalchemy.orm import Session
from app.schemas.link import LinkCreate
from app.models.link import Link
from app.core.security import generate_shorty_key

def get_url_by_key(db: Session, shorty_key: str):
    return db.query(Link).filter(Link.shorty_key == shorty_key).first()


def create_short_url(db: Session, link: LinkCreate):
    while True:
        key = generate_shorty_key()
        db_link = get_url_by_key(db, shorty_key=key)
        if not db_link:
            break
    new_link = Link(original_url=link.original_url, shorty_key=key)
    db.add(new_link)
    db.commit()
    db.refresh(new_link)
    return new_link