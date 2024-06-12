import traceback

from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from sqlalchemy import and_
from starlette.responses import JSONResponse

from app.models.db_connection.database import get_db
from app.models.org.companies import Company
from app.models.org.departments import Department
from app.models.users import schemas
from app.models.users.schemas import UserOrgBase, UserEmailBase
from app.models.users.users import Users, Friends

router = APIRouter()


@router.post("/search_users/org/", response_model=list[schemas.Users])
def get_users_by_org(org_info: UserOrgBase, request: Request, db: Session = Depends(get_db)):
    try:
        cid = int(request.headers.get('cid'))
        users = (db.query(Users.cid, Users.name, Users.email, Users.picture)
                 .join(Company, Company.id == Users.company_id)
                 .join(Department, Department.id == Users.dept_id)
                 .filter(Company.name == org_info.comp_name,
                         Department.name == org_info.dept_name, Users.cid != cid).all())
        users_list = []
        for user in users:
            user_dict = {
                "cid": user[0],
                "username": user[1],
                "email": user[2],
                "picture": user[3],
                "is_friend": False
            }
            users_list.append(user_dict)
        if users_list:
            friends = (db.query(Friends.user_id1).filter(Friends.user_id2 == cid, Friends.status == "friend").all()
                       + db.query(Friends.user_id2).filter(Friends.user_id1 == cid, Friends.status == "friend").all())
            for friend in friends:
                for user in users_list:
                    if friend[0] == user["cid"]:
                        user["is_friend"] = True

            return JSONResponse(users_list)

        else:
            return JSONResponse([])
        # cid = int(request.headers.get('cid'))
        # conditions = [Users.cid != cid]
        # if user_info.username:
        #     conditions.append(Users.name == user_info.username)
        # if user_info.comp_name:
        #     conditions.append(Company.name == user_info.comp_name)
        # if user_info.dept_name:
        #     conditions.append(Department.name == user_info.dept_name)
        #

        #
        #
        # users_list = []
        # for user in users:
        #     user_dict = {
        #         "cid": user[0],
        #         "username": user[1],
        #         "company_name": user[2],
        #         "dept_name": user[3]
        #     }
        #     users_list.append(user_dict)
        # if users_list:
        #     friends = (db.query(Friends.user_id1).filter(Friends.user_id2 == cid).all()
        #                + db.query(Friends.user_id2).filter(Friends.user_id1 == cid).all())
        #
        #     return JSONResponse(users_list)
        # else:
        #     return JSONResponse([])



    except Exception as e:
        err_res = {'traceback': traceback.format_tb(e.__traceback__)[0], 'error_msg': str(e)}
        return JSONResponse(err_res, status_code=418)


@router.post("/search_user/email/")
def get_user_by_email(email: UserEmailBase, request: Request, db: Session = Depends(get_db)):
    try:
        cid = int(request.headers.get('cid'))
        user = db.query(Users.cid, Users.name, Users.email, Users.picture).filter(Users.email == email.email).first()
        if user:
            user_info = {
                "cid": user.cid,
                "username": user.name,
                "email": user.email,
                "picture": user.picture,
                "is_friend": False
            }
            is_friend = db.query(Friends.id).filter(and_(Friends.user_id1 == cid, Friends.user_id2 == user.cid,
                                                         Friends.status == "friend") |
                                                    and_(Friends.user_id1 == user.cid, Friends.user_id2 == cid,
                                                         Friends.status == "friend")).first()
            print(is_friend)
            if is_friend:
                user_info["is_friend"] = True

            return JSONResponse([user_info])
        else:
            return JSONResponse([])

    except Exception as e:
        err_res = {'traceback': traceback.format_tb(e.__traceback__)[0], 'error_msg': str(e)}
        return JSONResponse(err_res, status_code=418)
