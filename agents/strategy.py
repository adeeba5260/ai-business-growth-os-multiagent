from utils.ai_handler import call_ai
from utils.prompt_builder import get_business_prompt,get_budget_prompt
import json

def strategy_agent(market_data, content_data, goal, budget, business):

    business_context = get_business_prompt(business)
    budget_context = get_budget_prompt(budget)

    prompt = f"""
    You are a digital marketing strategist.

    Business:
    {business_context}

    Budget:
    {budget_context}

    Goal: {goal}

    Market Data:
    {market_data}

    Content Data:
    {content_data}

    Create:

    - Ads strategy (based on budget)
    - Weekly plan
    - Growth roadmap

    Return JSON:
    {{
       "weekly_plan": ["Monday: ...", "Tuesday: ..."],
        "growth_tips": ["...", "..."],
        "ads": ["...", "..."]
    }}
    """

    return call_ai(prompt)