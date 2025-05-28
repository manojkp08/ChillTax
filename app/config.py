from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
PERPLEXITY_API_KEY = os.getenv("PERPLEXITY_API_KEY")