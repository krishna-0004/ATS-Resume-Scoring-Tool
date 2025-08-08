import google.generativeai as genai

genai.configure(api_key="AIzaSyC6bbpMgBCyflYGMncOpnveXH8A2LoQJ54")  # Replace or use env var

model = genai.GenerativeModel("gemini-2.5-flash")

def analyze_resume(resume_text):
    prompt = f"""
    Analyze this resume and give:
    1. Score (out of 100)
    2. Top 3 strengths
    3. Top 3 weaknesses
    4. Suitable job roles
    5. Skills to improve

    Resume:
    {resume_text}
    """
    response = model.generate_content(prompt)
    return response.text

def recommend_courses(weaknesses):
    prompt = f"""
    Recommend 5 free online courses for the following weaknesses or missing skills:
    {weaknesses}
    Return Title, Link, and Description.
    """
    response = model.generate_content(prompt)
    return response.text
