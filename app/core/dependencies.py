# app/core/dependencies.py

from fastapi import Header, HTTPException
from app.core.config import config

async def validate_authorization(authorization: str = Header(...)):
    if authorization != f"Bearer {config.SECRET_KEY}":
        raise HTTPException(status_code=401, detail="Unauthorized")
