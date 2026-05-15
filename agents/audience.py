from utils.ai_handler import call_ai
from utils.prompt_builder import get_business_prompt
import json

def audience_agent(audience, age, location):
    prompt = f"""
    You are a customer psychology expert.

    Analyze the target audience in detail:

    Audience Type: {audience}
    Age Group: {age}
    Location: {location}

    Give structured insights:

    1. Interests (what they like)
    2. Buying behavior (how they purchase)
    3. Pain points (what problems they face)
    4. What attracts them (content style, tone, offers)
    """

    return call_ai(prompt)