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
career_copilot </br>
├── app.py  </br>                  # Main Flask application
├── users.json </br>                 # JSON file storing registered users
├── skills_roles.json </br>           # JSON database of roles and associated skills
├── linkedin_jobs.xlsx </br>         # Job listing data
│
├── templates          </br>       # HTML templates rendered by Flask
│   ├── index.html       </br>       # Welcome page
│   ├── login.html        </br>      # Login form
│   ├── register.html      </br>     # User registration
│   ├── forgot.html         </br>    # Forgot password form
│   ├── skills.html          </br>   # Skill input for job recommendation
│   ├── results.html          </br>  # Top matching jobs display
│   ├── learn.html             </br> # Skill gap input form
│   └── learn_result.html       </br># Skill recommendation output
│
├── static          </br>         # Static assets
│   ├── styles.css     </br>        # CSS styles
│   └── script.js       </br>        # JavaScript for scroll animation



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
