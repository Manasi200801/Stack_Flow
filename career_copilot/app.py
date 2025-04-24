from flask import Flask, render_template, request, redirect, url_for, session
import pandas as pd
import json
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Load job data
df = pd.read_excel('linkedin_jobs.xlsx')
df['full_text'] = df['title'].astype(str) + ' - ' + df['description'].astype(str)
model = SentenceTransformer('all-MiniLM-L6-v2')
job_embeddings = model.encode(df['full_text'].tolist(), show_progress_bar=True)

# Load users
def load_users():
    with open('users.json') as f:
        return json.load(f)

def save_users(data):
    with open('users.json', 'w') as f:
        json.dump(data, f, indent=4)

# Load skill-role knowledge base
with open('skills_roles.json') as f:
    rag_data = json.load(f)

def recommend_learning_path(user_skills, target_role):
    matched_role = next((role for role in rag_data if role['Role'].lower() == target_role.lower()), None)
    if not matched_role:
        return f"❌ No data found for role: {target_role}"

    role_skills = set(map(str.lower, matched_role['Skill']))
    user_skills_set = set(map(str.lower, user_skills))

    already_have = role_skills & user_skills_set
    still_need = role_skills - user_skills_set

    response = f"🎯 <strong>Target Role:</strong> {target_role}<br><br>"
    response += f"✅ <strong>Your Skills:</strong> {', '.join(already_have) if already_have else 'None'}<br><br>"

    if still_need:
        response += f"🧠 <strong>Skills You Need to Learn:</strong> {', '.join(still_need)}<br><br>"
        response += "<strong>📘 Recommended Learning:</strong><ul>"
        for skill in still_need:
            response += f"<li>Learn <strong>{skill.title()}</strong> via relevant courses or platforms</li>"
        response += "</ul>"
    else:
        response += "🎉 You're already well-prepared for this role!"

    return response

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        users = load_users()['users']
        username = request.form['username']
        password = request.form['password']
        for user in users:
            if user['username'] == username and user['password'] == password:
                session['user'] = username
                return redirect(url_for('skill_input'))
        return render_template('login.html', error="Invalid credentials.")
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        users_data = load_users()
        username = request.form['username']
        password = request.form['password']
        for user in users_data['users']:
            if user['username'] == username:
                return render_template('register.html', error="User already exists.")
        users_data['users'].append({"username": username, "password": password})
        save_users(users_data)
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/forgot-password', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'POST':
        return render_template('forgot.html', message="Password reset link sent (not really).")
    return render_template('forgot.html')

@app.route('/skill-input', methods=['GET', 'POST'])
def skill_input():
    if 'user' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        skills = request.form['skills']
        user_embedding = model.encode([skills])
        similarities = cosine_similarity(user_embedding, job_embeddings)[0]
        df['similarity'] = similarities
        top_matches = df.sort_values(by='similarity', ascending=False).head(2)
        jobs = [{
            'title': row['title'],
            'company': row['companyName'],
            'location': row.get('location', 'N/A'),
            'url': row.get('jobUrl', '#'),
            'similarity': f"{row['similarity']:.4f}"
        } for _, row in top_matches.iterrows()]
        return render_template('results.html', jobs=jobs, skills=skills)

    return render_template('skills.html')

@app.route('/learn-path')
def learn_path():
    return render_template('learn.html')

@app.route('/learn-recommend', methods=['POST'])
def learn_recommend():
    skills_input = request.form['skills']
    target = request.form['role']
    user_skills = [s.strip() for s in skills_input.split(',')]
    result = recommend_learning_path(user_skills, target)
    return render_template('learn_result.html', result=result)

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)