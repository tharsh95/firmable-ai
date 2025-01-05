from fastapi import FastAPI
from app.api.endpoints import router

app = FastAPI(
    title="AI-Powered Web Scraper",
    description="A FastAPI application for web scraping and AI content analysis using Pydantic.",
    version="1.0.0"
)

app.include_router(router)
