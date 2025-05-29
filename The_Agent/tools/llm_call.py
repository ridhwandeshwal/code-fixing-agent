import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

def build_fix_prompt(code, error):
    return f"""You are an expert Python programmer.

You are given a buggy function and an error message. Fix the function and return only the fixed code so that it passes all test cases.

### Buggy Code:
{code}

### Error:
{error}

### Fixed Function:
"""

def generate_fix(code, error):
    prompt = build_fix_prompt(code, error)
    response = model.generate_content(prompt)
    return response.text
