from fastapi import APIRouter, HTTPException,Depends
from app.models.schemas import ScrapeRequest, AnalysisResponse
from app.services.scraper import scrape_content
from app.core.ai_agent import analyze_content
from app.core.dependencies import validate_authorization

router = APIRouter()

@router.post("/scrape", response_model=AnalysisResponse,dependencies=[Depends(validate_authorization)] )
async def scrape_and_analyze(request: ScrapeRequest):
    try:
        # Scrape website content
        content = await scrape_content(request.url)
        
        # Analyze content using AI agent
        response = await analyze_content(content)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
