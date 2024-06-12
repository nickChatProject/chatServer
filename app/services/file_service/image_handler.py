import os
import traceback

from fastapi import APIRouter
from fastapi import Request, UploadFile, Depends
from sqlalchemy.orm import Session
from starlette.responses import StreamingResponse, JSONResponse

from app.models.db_connection.database import get_db
from app.models.users.users import Users

router = APIRouter()


@router.get("/image/")
def image(request: Request):
    try:
        image_name = request.query_params["image"]
        file_path = os.path.join('images/', image_name)
        if os.path.exists(file_path):
            def iterfiles():  #
                with open(file_path, mode="rb") as file_like:  #
                    yield from file_like  #

            return StreamingResponse(iterfiles(), media_type="image/png")
        else:
            raise Exception("Image not found")
    #     file_path = os.path.join('images/', image_name)
    #     if os.path.exists(file_path):
    #         return FileResponse(path=file_path, filename=image_name)
    #     else:
    #         raise Exception("Image not found")
    except Exception as e:
        err_res = {'traceback': traceback.format_tb(e.__traceback__)[0], 'error_msg': str(e)}
        return JSONResponse(err_res, status_code=418)


@router.post("/avatar/")
def avatar(request: Request, files: UploadFile, db: Session = Depends(get_db)):
    try:
        cid = str(request.headers.get('cid'))
        upload_picture_path = f"images/{files.filename}"
        old_picture = db.query(Users).filter(Users.cid == int(cid)).first()
        old_picture_path = f"images/{old_picture.picture}"
        if not os.path.isfile(upload_picture_path) and old_picture.picture:
            with open(upload_picture_path, "wb") as f:
                f.write(files.file.read())
            old_picture.picture = files.filename
            db.commit()
            if os.path.isfile(old_picture_path):
                os.remove(old_picture_path)
        elif os.path.isfile(upload_picture_path):
            raise Exception("Image name is already exist, please upload again")
        else:
            with open(upload_picture_path, "wb") as f:
                f.write(files.file.read())
            old_picture.picture = files.filename
            db.commit()

    except Exception as e:
        err_res = {'traceback': traceback.format_tb(e.__traceback__)[0], 'error_msg': str(e)}
        return JSONResponse(err_res, status_code=418)
