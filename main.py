import os

import uvicorn
from fastapi import FastAPI

os.environ["conf_path"] = "config.yml"

from endpoints.post import post_router

app = FastAPI()
app.include_router(post_router)

if __name__ == "__main__":
    uvicorn.run(app, host="4.231.5.217", port=8000)
