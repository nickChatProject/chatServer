import os
import traceback

from fastapi import APIRouter, Request, UploadFile
from starlette.responses import FileResponse, JSONResponse

router = APIRouter()


@router.get('/test/')
def test():
    return JSONResponse({"test": "this is a test"})
