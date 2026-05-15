from utils.ai_handler import call_ai
import json

def content_refiner_agent(content, market, audience):

    prompt = f"""
    You are an expert AI content editor.

    Improve and restructure the given content for maximum engagement.

    Market Context:
    {market}

    Audience:
    {audience}

    Original Content:
    {content}

    IMPORTANT RULES:
    - Return ONLY valid JSON
    - Do NOT include explanations
    - Do NOT include markdown
    - Do NOT include extra text

    Output format MUST be:

    {{
        "post_ideas": [],
        "captions": [],
        "hashtags": [],
        "reels": [
            {{
                "idea": "",
                "script": ""
            }}
        ]
    }}
    """

    response = call_ai(prompt)

    try:
        return json.loads(response)
    except:
        return {
            "post_ideas": [],
            "captions": [],
            "hashtags": [],
            "reels": []
        }