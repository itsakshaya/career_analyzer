from flask import Flask, render_template, request

app = Flask(__name__)

# Define the job roles and their required skills
job_roles = {
    "Data Scientist": {"Python", "ML", "Pandas", "SQL"},
    "Cloud Engineer": {"AWS", "Linux", "Networking"},
    "Web Developer": {"HTML", "CSS", "JavaScript", "React"},
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    skills_input = request.form['skills']
    user_skills = {skill.strip().title() for skill in skills_input.split(',') if skill.strip()}

    matches = []
    for role, required_skills in job_roles.items():
        matched_skills = user_skills.intersection(required_skills)
        match_percent = int(len(matched_skills) / len(required_skills) * 100)
        missing_skills = required_skills - user_skills
        matches.append({
            "role": role,
            "match_percent": match_percent,
            "missing_skills": missing_skills
        })

    return render_template('result.html', matches=matches, skills=user_skills)

if __name__ == '__main__':
    app.run(debug=True)
