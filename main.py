import os
from google import genai
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

prompt = 'Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.'
content = client.models.generate_content('gemini-2.0-flash-001', prompt)

print(content.text, content.usage_metadata)