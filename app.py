from flask import Flask, jsonify, render_template, request, redirect, url_for, session, make_response, flash
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Set a secret key for session management

visitor_count = 0

# Create a file to store the visitor count
count_file = 'visitor_count.txt'
if os.path.exists(count_file):
    with open(count_file, 'r') as f:
        visitor_count = int(f.read())

jobs = [{
    'id': 1,
    "title": "Data Analyst",
    "location": "Bengaluru, India",
    "salary": "Rs. 10,00,000"
}, {
    "id": 2,
    "title": "Data Scientist",
    "location": "Delhi, India",
    "salary": "Rs. 15,00,000"
}, {
    "id": 3,
    "title": "Frontend Engineer",
    "location": "Remote",
    "salary": "Rs. 12,00,000"
}]

@app.route('/')
def index():
    global visitor_count
    visitor_count += 1
    with open(count_file, 'w') as f:
        f.write(str(visitor_count))
    return render_template('home.html', Jobs=jobs, visitor_count=visitor_count)

@app.route('/jobs')
def list_jobs():
    return jsonify(jobs)

@app.route('/get_visitor_count')
def get_visitor_count():
    return jsonify({'visitor_count': visitor_count})

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/features')
def features():
    return render_template('features.html')

# Dummy user data for demonstration
users = {
    "user@example.com": "password123"
}

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        remember = request.form.get('remember')  # Check if "Remember Me" is checked

        # Check if the user exists and the password is correct
        if email in users and users[email] == password:
            # User is authenticated
            session['email'] = email  # Store user email in session

            # If "Remember Me" is checked, set a cookie
            if remember:
                resp = make_response(redirect(url_for('dashboard')))
                resp.set_cookie('email', email, max_age=60*60*24*30)  # Cookie lasts for 30 days
                return resp
            else:
                return redirect(url_for('dashboard'))
        else:
            flash('Invalid email or password')
            return redirect(url_for('login'))  # Redirect to login on failure

    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        # Handle the form data here (e.g., send an email)
        flash('Your message has been sent successfully!')
        return redirect(url_for('contact'))  # Redirect to contact page after submission
    return render_template('contact.html')

@app.route('/pricing')
def pricing():
    return render_template('pricing.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/dashboard')
def dashboard():
    email = session.get('email') or request.cookies.get('email')
    if email:
        return f'Welcome