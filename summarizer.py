import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

# Generate meeting summary
def summarize_meeting(transcript):
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
    model = genai.GenerativeModel("models/gemini-1.5-flash")
    prompt = f"Summarize this meeting transcript: {transcript}"
    response = model.generate_content(prompt)
    return response.text
