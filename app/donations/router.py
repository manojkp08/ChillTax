from fastapi import APIRouter, Header
from app.auth.utils import validate_token
from app.database.crud import get_db
import httpx
from app.config import PERPLEXITY_API_KEY

router = APIRouter()

@router.get("/suggestions")
async def get_donation_suggestions(token: str = Header(...)):
    db = next(get_db())
    user_id = validate_token(db, token)
    
    PROMPT = """
    Suggest 5 tax-deductible donations under ₹10,000 in India with:
    - NGO names
    - Cause (education/health/etc.)
    - Tax benefit percentage
    Format as JSON list.
    """
    
    headers = {"Authorization": f"Bearer {PERPLEXITY_API_KEY}"}
    payload = {
        "model": "sonar-medium-online",
        "messages": [{"role": "user", "content": PROMPT}]
    }
    
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "https://api.perplexity.ai/chat/completions",
            json=payload,
            headers=headers
        )
        return response.json()