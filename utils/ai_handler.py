from groq import Groq
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Get API key from .env file
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def call_ai(prompt):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content

