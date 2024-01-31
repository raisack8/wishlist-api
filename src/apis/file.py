import base64
import shutil
import os

from typing import List
from fastapi import APIRouter, Depends, File, UploadFile
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from cachetools import cached, TTLCache
from ..services.file import ServiceFile

router = APIRouter()


@router.post(
    "/file/upload",
    summary="/upload",
    description="ファイルアップロードAPI<br>UploadFileクラスを特定のフォルダ(バケット)に保存する",
)
async def upload_file(upload_file: UploadFile = File(...)):
    if upload_file:
        file_bytes = upload_file.file
        file_path = os.path.join(os.getcwd(), r"resources")
        upload_dir = open(os.path.join(file_path, upload_file.filename), "wb+")
        shutil.copyfileobj(file_bytes, upload_dir)
        upload_dir.close()
        return {"filenames": upload_file.filename}


@cached(cache=TTLCache(maxsize=10, ttl=3000))
@router.post(
    "/file/get-files",
    summary="/get-files",
    description="ファイルダウンロードAPI<br>読み込みたいファイル一覧を受取り、バイナリ画像データリストを返す",
)
async def get_file(body: List[str]):
    return_dict = {}
    file_path = os.path.join(os.getcwd(), r"resources")
    for file_name in body:
        if file_name == "default.jpg":
            continue
        try:
            return_dict[file_name] = ServiceFile.image_convert_to_binari(
                file_path, file_name
            )
        except Exception as e:
            print(e)
            pass
    return JSONResponse(content=return_dict)
