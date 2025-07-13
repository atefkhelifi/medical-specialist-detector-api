# 🩺 Symptom-to-Specialist API (Flask + Gemini)

This is a simple Flask API that uses **Google Gemini AI** to suggest the correct **medical specialist** based on a user's symptom **description** in any language.

---

## 🌍 Features

- 💬 Accepts natural language symptom descriptions (e.g. "وجيعة في صدري", "n7es b wja3a fi rassi", "I feel dizzy")
- 🌐 Automatically translates to English
- 🧠 Uses **Gemini 2.0 Flash** model to detect the appropriate doctor
- 🔁 Returns specialty only (e.g. "Cardiologist", "Neurologist")
- 🔓 Public API — easy to integrate in frontend or backend
- ☁️ Ready for deployment on **Railway**

---

## 🚀 Usage

### 🧪 Local Test

```bash
curl -X POST http://localhost:5000/detect \
  -H "Content-Type: application/json" \
  -d '{"symptom": "I feel dizzy"}'
```
