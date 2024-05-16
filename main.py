from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

import models
from db import engine
from route import user_router, base_router, api_router

#models.Base.metadata.create_all(bind=engine)

origins = ["*"]

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router, tags=["users"])
app.include_router(base_router, prefix="/base", tags=["base"])
app.include_router(api_router, prefix="/api", tags=["API"])

@app.get("/")
async def home():
    return {"detail": "Welcome to Aquaterrius api app."}

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)