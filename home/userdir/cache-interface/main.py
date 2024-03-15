from fastapi import FastAPI, HTTPException, Request
import shutil
import os

app = FastAPI()

CACHE_PATH = "/data/nginx/cache"


@app.post("/invalidate/")
async def invalidate_cache(request: Request):
    """
    Handles incoming webhook requests from Webflow, emitted whenever site_publish events occur.

    Nginx cache is invalidated by removing the cached files from disk
    """
    webhook_data = await request.json()

    try:
        # Check if cache directory exists
        if os.path.exists(CACHE_PATH):
            shutil.rmtree(CACHE_PATH)
            os.makedirs(CACHE_PATH, exist_ok=True)
        else:
            return {"message": "Cache directory does not exist, no action taken."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    return {"message": "Cache invalidated successfully"}

