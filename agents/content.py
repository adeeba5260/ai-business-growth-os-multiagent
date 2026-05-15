from utils.ai_handler import call_ai
from utils.prompt_builder import get_business_prompt,get_budget_prompt
import json

def content_agent(business, audience_data, platform, budget):

    business_context = get_business_prompt(business)
    budget_context = get_budget_prompt(budget)

    prompt = f"""
You are a social media expert.

IMPORTANT RULE:
Return ONLY valid JSON.
DO NOT skip any field.

Return EXACT structure:

{{
  "post_ideas": ["..."],
  "captions": ["..."],
  "hashtags": ["..."],
  "reels": [
    {{
      "idea": "Reel idea",
      "script": "Full viral script with hook + body + CTA"
    }},
    {{
      "idea": "Reel idea 2",
      "script": "Full script"
    }},
    {{
      "idea": "Reel idea 3",
      "script": "Full script"
    }}
  ]
}}

Business: {business}
Audience: {audience_data}
Platform: {platform}
Budget: {budget}
"""

    response = call_ai(prompt)

    try:
        return json.loads(response)
    except:
        return {
            "post_ideas": [],
            "captions": [],
            "hashtags": []
        }