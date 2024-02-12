from typing import Union

from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse

from tools import check_url_patterns, get_data, get_urls_from_string

app = FastAPI()


@app.get("/")
async def start():
    return RedirectResponse("http://www.github.com/r0ld3x/terabox-api")


@app.get("/get")
async def read_item(url: str):
    if not url:
        raise HTTPException(
            status_code=400,
            detail="Url Not Found. ex: /get?url=https://www.terabox.app/",
        )
    link = get_urls_from_string(url)
    if not link:
        raise HTTPException(
            status_code=400,
            detail="Invalid Terabox url.",
        )
    check = check_url_patterns(url)
    if not check:
        raise HTTPException(
            status_code=400,
            detail="Invalid Terabox url.",
        )
    data = get_data(url)
    if not data:
        raise HTTPException(
            status_code=400,
            detail="No data found.",
        )
    return data
