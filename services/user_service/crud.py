import json

from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from models.db_connection.database import get_db
from models.org.companies import Company
from models.org.departments import Department
from models.users import schemas
from models.users.schemas import UserInfoBase
from models.users.users import Users

router = APIRouter()


@router.get("/users/", response_model=list[schemas.Users])
def get_users_by_info(user_info: UserInfoBase, request: Request, db: Session = Depends(get_db)):
    try:
        cid = int(request.headers.get('cid'))
        conditions = [Users.cid != cid]
        if user_info.username:
            conditions.append(Users.name == user_info.username)
        if user_info.comp_name:
            conditions.append(Company.name == user_info.comp_name)
        if user_info.dept_name:
            conditions.append(Department.name == user_info.dept_name)

        users = (db.query(Users.cid, Users.name, Company.name, Department.name).join(Company, Company.id == Users.company_id)
                 .join(Department, Department.id == Users.dept_id).filter(*conditions).all())
        users_list = []
        for user in users:
            user_dict = {
                "id": user[0],
                "username": user[1],
                "company_name": user[2],
                "dept_name": user[3]
            }
            users_list.append(user_dict)
        return JSONResponse(users_list)

    except Exception as e:
        err_res = {'error': str(e)}
        return JSONResponse(err_res, status_code=418)


