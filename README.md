# FastAPI Web Scraper with AI Analysis

## Overview
This project is a FastAPI application that performs the following tasks:
1. Scrapes content from a given URL using an async scraper.
2. Analyzes the scraped content using an AI agent.
3. Provides results through a RESTful API.

## Features
- **Web Scraping**: Extracts content from JavaScript-rendered websites using Playwright.
- **AI Analysis**: Uses an AI agent to analyze content and provide structured responses.
- **Authorization**: Secured with an API key in the `Authorization` header.

---

## Installation

### Prerequisites
- Python 3.10 or later
- Docker (optional for containerization)
- Playwright (for web scraping)

### Local Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/tharsh95/firmable-ai.git
   cd firmable-ai
   ```
2. Install
   ```bash
   pip install -r requirements.txt
   playwright install
   ```
3. Run the application
   ```bash
   uvicorn app.main:app --host 0.0.0.0 --port 8000
   ```
   ## Hosted Link
   ```bash
   http://ec2-13-201-76-216.ap-south-1.compute.amazonaws.com/scrape
   ```
## Endpoints
### POST /scrape
  - Scrapes a URL and analyzes its content.

  Request
  Headers:
  ```bash
Authorization: Bearer <Secret_Api_key>
  ```
"secret" is the secret_api_key
### Body
```bash
{
  "url": "https://example.com"
}
```
### Response
Status code - 200 OK
```bash
{
  "industry": "Technology",
  "company_size": "Large",
  "location": "San Francisco, USA"
}
```
### Errors:

#### 401 Unauthorized: Missing or invalid API key.
#### 500 Internal Server Error: Failed to scrape or analyze content.

---

### Run with Docker
#### Pull the Docker Image
#### The application is prebuilt into a Docker image hosted on Docker Hub. To pull the image, use the following command:
```bash
docker pull tharsh95/firm-ai:v1.0
```
Run the Docker Image
Replace your_openai_api_key with your actual OpenAI API key before running the command:

```bash
docker run -e OPENAI_API_KEY=your_openai_api_key -p 8000:8000 tharsh95/firm-ai:v1.0
```
#### Access the Application
#### Once the container is running, access the application at:
```bash
http://localhost:8000
```
