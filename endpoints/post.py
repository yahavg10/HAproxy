import logging

from fastapi import File, UploadFile, APIRouter

from utils import app_config

logger = logging.getLogger(app_config.logger.logger_name)
post_router = APIRouter()


@post_router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    try:
        logger.info(f"Received file: {file.filename}")

        return {"info": f"File '{file.filename}' uploaded successfully"}

    except Exception as e:
        logger.error(f"Error uploading file {file.filename}: {str(e)}")
        return {"error": f"Failed to upload {file.filename}"}