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


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
