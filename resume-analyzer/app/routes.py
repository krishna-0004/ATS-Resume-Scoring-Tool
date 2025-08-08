from flask import Flask, request, jsonify
from app.resume_parser import extract_resume_text
from app.gemini_api import analyze_resume, recommend_courses
import tempfile

app = Flask(__name__)

@app.route("/evaluate", methods=["POST"])
def evaluate_resume():
    file = request.files["resume"]
    
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        file.save(tmp.name)
        resume_text = extract_resume_text(tmp.name)

    gemini_output = analyze_resume(resume_text)

    # Ideally, extract weaknesses from gemini_output via LLM parsing
    weaknesses = "No internships, outdated tech stack"  # Hardcoded for now
    course_output = recommend_courses(weaknesses)

    return jsonify({
        "score_and_analysis": gemini_output,
        "courses": course_output
    })
