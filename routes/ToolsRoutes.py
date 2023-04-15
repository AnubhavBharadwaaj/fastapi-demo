from fastapi import APIRouter, Path, Query, Request
from .services.services import *

router = APIRouter()
print("Change")
@router.get("/video/{url:path}")
async def get_video(url):
    return {"url": youtube_video_downloader(url)[1:-1]}

@router.get("/ideapin/{url:path}")
async def get_idea_pin(url):
    return {"url": youtube_idea_pin_downloader(url)[1:-1]}

@router.get("/image/{url:path}")
async def get_idea_pin_image(url):
    return {"url": youtube_image_pin_downloader(url)[1:-1]}
