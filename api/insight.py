from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles
import os
import json
import re
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

app = FastAPI()

# Mount static HTML folder
app.mount("/static", StaticFiles(directory="static"), name="static")

# Serve the frontend
@app.get("/")
async def serve_index():
    return FileResponse("static/index.html")

# Insight synthesizer logic
PROMPT_TEMPLATE = """
You are an insight synthesizer.

You will be given a list of survey responses.

1. Group the responses into 3 key themes.
2. For each theme, give:
   - A short, clear title.
   - Exactly 1-2 quotes per theme that best represent it.
   - An optional sentiment score (positive, neutral, negative).

Survey Responses:
{survey_data}

Your output format MUST be valid JSON like this:
[
  {{
    "theme": "...",
    "quotes": ["...", "..."],
    "sentiment": "..."
  }},
  ...
]
"""

def extract_json(text):
    cleaned = re.sub(r"```(?:json)?", "", text).strip("` \n")
    match = re.search(r'\[\s*{.*}\s*\]', cleaned, re.DOTALL)
    return match.group(0) if match else cleaned

@app.post("/api")
async def generate_insights(request: Request):
    body = await request.json()
    responses = body.get("responses", [])
    
    model = genai.GenerativeModel("models/gemini-1.5-pro")
    prompt = PROMPT_TEMPLATE.format(survey_data=json.dumps(responses, indent=2))
    
    try:
        gemini_response = model.generate_content(prompt)
        json_text = extract_json(gemini_response.text)
        return JSONResponse(content=json.loads(json_text))
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
