import httpx
import json
import logging
from app.config import PERPLEXITY_API_KEY

# Setup logging
logger = logging.getLogger(__name__)

async def categorize_expense(description: str):
    try:
        headers = {
            "Authorization": f"Bearer {PERPLEXITY_API_KEY}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "model": "sonar",
            "messages": [{
                "role": "user", 
                "content": f"""Categorize this expense: '{description}'. 
                
                Choose from these categories only: Work, Income, Study, Health, Donation, Personal, Other
                
                Determine if it's tax relevant (business/work related = true, personal = false).
                
                Respond with ONLY a valid JSON object in this exact format:
                {{"category": "xyx", "tax_relevant": true or false}}"""
            }],
            "temperature": 0.1 
        }
        
        async with httpx.AsyncClient(timeout=10.0) as client:
            logger.info(f"Calling Perplexity API for description: {description}")
            response = await client.post(
                "https://api.perplexity.ai/chat/completions", 
                json=payload, 
                headers=headers
            )
            
            if response.status_code != 200:
                logger.error(f"Perplexity API error: {response.status_code} - {response.text}")
                return {"category": "Other", "tax_relevant": False}
            
            api_response = response.json()
            logger.info(f"Perplexity API response: {api_response}")
            
            # Extract the content from the API response
            if "choices" in api_response and len(api_response["choices"]) > 0:
                content = api_response["choices"][0]["message"]["content"]
                logger.info(f"AI generated content: {content}")
                
                # Try to parse the JSON from the content
                try:
                    # Clean up the content - remove any extra text before/after JSON
                    content = content.strip()
                    
                    # Find JSON object in the content
                    start_idx = content.find('{')
                    end_idx = content.rfind('}') + 1
                    
                    if start_idx != -1 and end_idx != -1:
                        json_str = content[start_idx:end_idx]
                        ai_data = json.loads(json_str)
                        
                        # Validate the response structure
                        if "category" in ai_data and "tax_relevant" in ai_data:
                            # Ensure category is one of the allowed values
                            allowed_categories = ["Work", "Income", "Study", "Health", "Donation", "Other"]
                            if ai_data["category"] not in allowed_categories:
                                ai_data["category"] = "Other"
                            
                            # Ensure tax_relevant is boolean
                            if not isinstance(ai_data["tax_relevant"], bool):
                                ai_data["tax_relevant"] = str(ai_data["tax_relevant"]).lower() == 'true'
                            
                            logger.info(f"Successfully parsed AI response: {ai_data}")
                            return ai_data
                        else:
                            logger.error("AI response missing required fields")
                            return {"category": "Other", "tax_relevant": False}
                    else:
                        logger.error("No valid JSON found in AI response")
                        return {"category": "Other", "tax_relevant": False}
                        
                except json.JSONDecodeError as e:
                    logger.error(f"Failed to parse AI response as JSON: {e}")
                    logger.error(f"Content was: {content}")
                    return {"category": "Other", "tax_relevant": False}
            else:
                logger.error("Invalid API response structure")
                return {"category": "Other", "tax_relevant": False}
                
    except httpx.TimeoutException:
        logger.error("Perplexity API timeout")
        return {"category": "Other", "tax_relevant": False}
    except Exception as e:
        logger.error(f"Error in categorize_expense: {str(e)}")
        return {"category": "Other", "tax_relevant": False}