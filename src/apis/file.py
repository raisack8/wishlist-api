import shutil
import os

from fastapi import APIRouter, Depends, File, UploadFile
from sqlalchemy.orm import Session

from ..models.database import get_db
from ..schemas.requests.item_register import PReqItemRegister
from ..schemas.response.item_list_get import GItemGetList
from ..services.item import ServiceItem
from ..services.user import UserCrud

router = APIRouter()

@router.post(
        "/file/upload",
        description="ファイルをアップロード"
        )
async def upload_file(upload_file: UploadFile = File(...)):
    if upload_file:
        file_bytes = upload_file.file
        file_path = os.path.join(os.getcwd(), r"resources")
        upload_dir = open(os.path.join(file_path, upload_file.filename),'wb+')
        shutil.copyfileobj(file_bytes, upload_dir)
        upload_dir.close()
        return {"filenames": upload_file.filename}