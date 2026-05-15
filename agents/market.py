from utils.ai_handler import call_ai
from utils.prompt_builder import get_business_prompt
import json
def market_agent(business, audience, age, location, platform, memory):

    prompt = f"""
    You are an expert marketing strategist.

    Current Business: {business}
    Audience: {audience}
    Age: {age}
    Location: {location}
    Platform: {platform}

    Previous User History:
    {memory}

    Generate improved marketing insights based on past behavior.
    """

    return call_ai(prompt)