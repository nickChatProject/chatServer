import os

from fastapi import APIRouter
from fastapi import Request
from starlette.responses import StreamingResponse, JSONResponse

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
        err_res = {'error': str(e)}
        return JSONResponse(err_res, status_code=418)