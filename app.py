from flask import Flask, render_template

app = Flask(__name__)

# --- Your Personal Data (NEW) ---
# This data powers the header, footer, and homepage
personal_data = {
    'name': 'Novelia Joseph',
    'title': 'Computer Applications Master Candidate', 
    'short_bio': 'Motivated and detail-oriented professional specializied in Cloud Computing (AWS), and full-stack development. Enthusiastic about problem-solving and adept at quickly learning new technical challenges.',
    'email': 'noveliajosephk@gmail.com',
    'linkedin': 'https://www.linkedin.com/in/noveliajoseph',
    'github': 'https://github.com/NoveliaJoseph',
    'resume_filename': 'novelia_joseph_resume.pdf', # Ensure this file is in static/files/
    'profile_image': 'novelia-profile.jpg' # Ensure this file is in static/img/
}
# ---------------------------------


# --- Your Technical Project Data (UPDATED AND RENAMED) ---
tech_projects = [
    {
        'id': 1,
        'title': 'Emogram - Sentiment Analysis with Deep Learning',
        'slug': 'emogram-ml', 
        'tech': ['NLTK', 'Python', 'Django', 'BERT/LSTM/CNN'],
        'short_desc': 'Developed a sentiment analysis system for social media (Facebook) using advanced deep learning models.',
        'details': 'Implemented the system with separate mobile and web apps for users and administrators, utilizing BERT, LSTM, and CNN models. The core objective was precise sentiment detection in user-generated content, with findings currently being prepared for a research journal.',
        'image': 'emogram-visual.jpg' 
    },
    {
        'id': 2,
        'title': 'Web-Based Employee Management System',
        'slug': 'employee-system',
        'tech': ['PHP', 'MySQL', 'HTML', 'Backend Development'],
        'short_desc': 'Built a functional web application for employee management, integrating backend and database functionalities.',
        'details': 'Focused on creating smooth operational flow between the user interface and the MySQL database using PHP for server-side logic, demonstrating strong skills in relational database management and full-stack web development.',
        'image': 'employee-system-visual.jpg'
    },
    {
        'id': 3,
        'title': 'Hypermarket Management System',
        'slug': 'hypermarket-system',
        'tech': ['PHP', 'JS', 'MySQL', 'HTML', 'Front-End Interactivity'],
        'short_desc': 'Developed a web application for hypermarket management, utilizing JavaScript for front-end interactivity.',
        'details': 'Completed the full-stack development cycle, connecting the front-end interface with database management using PHP and MySQL, and enhancing user experience with client-side JavaScript features.',
        'image': 'hypermarket-visual.jpg'
    }
]
# ---------------------------------


# --- Flask Context Processor (NEW) ---
# Makes the personal_data dictionary available in ALL templates (base.html, index.html, etc.)
@app.context_processor
def inject_personal_data():
    return {'personal_data': personal_data}


# 1. Homepage Route
@app.route('/')
def index():
    # Passes featured_projects and all personal data
    return render_template('index.html', 
                           featured_projects=tech_projects[:2], # CHANGED to tech_projects
                           data=personal_data)

# 2. All Projects Route
@app.route('/projects')
def projects_list():
    # Passes the entire list of projects
    return render_template('projects.html', projects=tech_projects) # CHANGED to tech_projects

# 3. Individual Project Detail Route (Dynamic URL)
@app.route('/projects/<project_slug>')
def project_detail(project_slug):
    # Finds the project dictionary that matches the slug
    project = next((p for p in tech_projects if p['slug'] == project_slug), None) # CHANGED to tech_projects
    
    if project is None:
        # Simple error handling if project is not found
        return "404 Project Not Found", 404
        
    return render_template('project_detail.html', project=project)
# ... after the existing routes (index, projects_list, project_detail) ...

# 4. Contact Page Route (Display Form)
@app.route('/contact')
def contact():
    # We will display the contact form on a dedicated page
    return render_template('contact.html')

# 5. Form Submission Route (for future database integration)
# We use POST because data is being sent to the server
@app.route('/contact', methods=['POST'])
def submit_contact():
    # In a real app, this is where you would save the data to a database (like Firestore)
    # or send yourself an email notification.
    
    # For now, we'll simulate success and redirect
    return render_template('contact_success.html', data=personal_data)



if __name__ == '__main__':
    app.run(debug=True)