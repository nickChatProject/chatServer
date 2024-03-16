from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from models.db_connection.database import get_db
from models.users import schemas
from models.users.users import Users

router = APIRouter()


@router.get("/users/", response_model=list[schemas.Users])
def get_all_users(db: Session = Depends(get_db)):
    users = db.query(Users).all()
    return users



