from pydantic import BaseModel, HttpUrl, Field

class ScrapeRequest(BaseModel):
    url: HttpUrl = Field(..., description="The URL of the website to scrape.")

class AnalysisResponse(BaseModel):
    industry: str = Field(..., description="The industry the website belongs to.")
    company_size: str = Field(..., description="The size of the company (small, medium, large).")
    location: str = Field(..., description="The location of the company (city and country).")
