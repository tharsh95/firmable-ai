import json
from openai import OpenAI
from app.core.config import config
from app.models.schemas import AnalysisResponse

client = OpenAI(api_key=config.OPENAI_API_KEY)

async def analyze_content(content: str) -> AnalysisResponse:
    """
    Analyze content using OpenAI's GPT model and return structured analysis.
    """
    prompt = f"""
    Analyze the following website content and answer these questions:
    1. What industry does the website belong to?
    2. What is the size of the company (e.g., small, medium, large)?
    3. In which city and country is the company located?

    Provide your answers in **strict JSON format** with the following keys:
    - 'industry': string
    - 'company_size': string
    - 'location': string

    Example:
    {{
      "industry": "Technology",
      "company_size": "Medium",
      "location": "San Francisco, USA"
    }}

    Content:
    {content[:config.MAX_CONTENT_LENGTH]}  # Truncate content
    """

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
        )

        # Extract and validate the JSON response
        raw_output = response.choices[0].message.content

        # Parse the raw output into JSON
        parsed_data = json.loads(raw_output)  # Raises JSONDecodeError if invalid

        # Validate using Pydantic model
        analysis = AnalysisResponse.parse_obj(parsed_data)
        return analysis
    except json.JSONDecodeError as e:
        raise ValueError(f"Error decoding JSON from AI response: {str(e)}")
    except Exception as e:
        raise ValueError(f"Error analyzing content: {str(e)}")
