import os

from fastapi import APIRouter, Request, UploadFile
from starlette.responses import FileResponse, JSONResponse

router = APIRouter()


@router.get("/file/")
def file(request: Request):
    try:
        file_name = request.query_params["file"]
        file_path = os.path.join('files/', file_name)
        if os.path.exists(file_path):
            return FileResponse(path=file_path, filename=file_name)
        else:
            raise Exception("File not found")
    except Exception as e:
        err_res = {'error': str(e)}
        return JSONResponse(err_res, status_code=418)


@router.post("/file/")
async def create_upload_file(files: UploadFile):
    try:
        file_path = f"files/{files.filename}"
        print(files.filename)
        with open(file_path, "wb") as f:
            f.write(files.file.read())
        return {"message": "File saved successfully"}

    except Exception as e:
        err_res = {'error': str(e)}
        return JSONResponse(err_res, status_code=418)


