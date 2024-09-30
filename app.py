from flask import Flask, jsonify, render_template, request, redirect, url_for
from jinja2.utils import Joiner
import os

app = Flask(__name__)
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

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        # Handle the form data here (e.g., send an email)
        return redirect(url_for('contact'))
    return render_template('contact.html')

@app.route('/pricing')
def pricing():
    return render_template('pricing.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')



if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
