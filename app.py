from flask import Flask, request, jsonify
from dotenv import load_dotenv

from deep_translator import GoogleTranslator
import google.generativeai as genai
import requests  

import os

app = Flask(__name__)

# Load API key securely
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


def translate_to_english(text):
    try:
        return GoogleTranslator(source='auto', target='en').translate(text)
    except:
        return text

def detect_specialist(symptoms):
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "AIzaSyBvQKeFV7BY0JJWOH40zt0IhMCJYuY9jn0")  # or hardcode
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}"

    english = translate_to_english(symptoms)

    prompt = f"What type of doctor should a patient see if they say: '{english}'? Respond with only the doctor's specialty (e.g., Cardiologist, Neurologist)."

    payload = {
        "contents": [
            {
                "parts": [
                    { "text": prompt }
                ]
            }
        ]
    }

    try:
        response = requests.post(url, json=payload)
        data = response.json()
        return data['candidates'][0]['content']['parts'][0]['text'].strip()
    except Exception as e:
        return f"Error: {str(e)}"

@app.route("/detect", methods=["POST"])
def detect():
    data = request.get_json()
    symptom = data.get("symptom")
    if not symptom:
        return jsonify({"error": "Missing 'symptom' field"}), 400

    specialist = detect_specialist(symptom)
    return jsonify({"specialist": specialist})

if __name__ == "__main__":
    app.run(debug=True)
