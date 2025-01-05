import os

class Config:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY","")
    MAX_CONTENT_LENGTH = 4000
    SECRET_KEY = "secret"


config = Config()
