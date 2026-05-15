from utils.ai_handler import call_ai
import json

def reels_agent(business, audience, age, location, platform):
    prompt = f"""
You are a viral Instagram reels expert.

Return ONLY JSON:

{{
  "reels": [
    {{
      "idea": "Reel idea",
      "hook": "Hook line",
      "script": "Full script"
    }},
    {{
      "idea": "Reel idea 2",
      "hook": "Hook line",
      "script": "Full script"
    }},
    {{
      "idea": "Reel idea 3",
      "hook": "Hook line",
      "script": "Full script"
    }}
  ]
}}

Business: {business}
Audience: {audience}
Age: {age}
Location: {location}
Platform: {platform}
"""
    response = call_ai(prompt)

    try:
        return json.loads(response)
    except:
        return {"reels": []}