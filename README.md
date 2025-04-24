# 💼 CareerCopilot – AI-Powered Career Recommendation App

CareerCopilot is a full-stack AI web app that helps users:

- 🔍 Get personalized **job recommendations** based on their skills
- 🎓 Discover **missing skills** for a target career using a smart **Learning Path Advisor**

Built with `Flask`, `sentence-transformers`, and styled with simple HTML/CSS.

---

## 🚀 Features

- ✅ User login, registration, and session management (stored in JSON)
- 🔐 Secure skill input for job search (via SentenceTransformer embeddings)
- 📘 Learning path suggestion from a custom role–skills JSON knowledge base
- 💡 Simple, responsive UI with scrollable welcome page

---

## 🏗️ Project Structure


---

## 🧠 Learning Path Feature

Users can enter:

- 🔤 Their current skills (e.g., Python, Excel)
- 🎯 A target profession (e.g., Data Scientist)

The app compares these to a local JSON database (`skills_roles.json`) and suggests what skills are still needed to master that role.

```json
[
  {
    "Role": "Data Scientist",
    "Skill": ["Python", "SQL", "Machine Learning", "Statistics"]
  }
]
```


💻 Tech Stack

-Python + Flask for backend

-Sentence Transformers (MiniLM) for job-skill matching

-Pandas + Scikit-learn for similarity scoring

-HTML/CSS/JS for frontend

-JSON for user and skill-role data
