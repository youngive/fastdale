from pathlib import Path

import requests
from fastapi import APIRouter, HTTPException
from pydantic import ValidationError
from starlette.responses import FileResponse

from src.schemes.filename import FilenameValidator
import src.utilities.config as cfg

router = APIRouter()

# Корневой URL для скачивания файлов
root = cfg.root


@router.get("/fs/{filename:path}")
async def download_file(filename: str):
    try:
        FilenameValidator(filename=filename)
    except ValidationError as e:
        type = str(e.errors()[0]['type'])
        if type == "string_too_long":
            error = "Filename exceeds 255 characters"
        elif type == "string_pattern_mismatch":
            error = "Invalid characters in filename"
        elif type == "value_error":
            error = "Invalid file extension"
        else:
            error = type
        raise HTTPException(status_code=400, detail=error)

    local_path = Path("assets/static/fs") / filename
    if not local_path.exists():
        # Скачиваем файл из root, если локального файла не существует
        remote_url = root + filename
        try:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Shararam/2.0.3 Chrome/80.0.3987.165 Electron/8.2.5 Safari/537.36"
            }
            response = requests.get(remote_url, headers=headers)
            response.raise_for_status()
            with open(local_path, "wb") as file:
                file.write(response.content)
        except requests.RequestException:
            raise HTTPException(status_code=404, detail="File not found")

    # Определяем Content-Type на основе расширения файла
    content_type = "application/octet-stream"
    if filename.endswith(".swf"):
        content_type = "application/x-shockwave-flash"
    elif filename.endswith(".png"):
        content_type = "image/png"
    elif filename.endswith(".jpg"):
        content_type = "image/jpeg"

    return FileResponse(local_path, media_type=content_type)


@router.get("/base.swf")
async def download_base():
    local_path = Path("assets/static") / "base.swf"
    if not local_path.exists():
        # Скачиваем файл из root, если локального файла не существует
        remote_url = root.replace("/fs/", "/") + "base.swf"
        print(remote_url)
        try:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Shararam/2.0.3 Chrome/80.0.3987.165 Electron/8.2.5 Safari/537.36"
            }
            response = requests.get(remote_url, headers=headers)
            response.raise_for_status()
            with open(local_path, "wb") as file:
                file.write(response.content)
        except requests.RequestException:
            raise HTTPException(status_code=404, detail="File not found")

    return FileResponse(local_path, media_type="application/x-shockwave-flash")
