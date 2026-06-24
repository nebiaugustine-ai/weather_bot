from fastapi import APIRouter
from google import genai
import os
from google.genai import types
from dotenv import load_dotenv


client = genai.Client()


system_prompt = (
    "Questions regarding weather only"
)

response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents='How does a microwave work?',
    config=types.GenerateContentConfig(
        system_instruction=system_prompt,
        temperature=0.7
    )
)

print(response.text)