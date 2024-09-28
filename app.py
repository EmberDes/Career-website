from flask import Flask, jsonify, render_template, request, redirect, url_for
from jinja2.utils import Joiner

app = Flask(__name__)

jobs=[
  {
    'id' : 1,
    "title":"Data Analyst",
    "location":"Bengaluru, India",
    "salary":"Rs. 10,00,000"
  },
  {
    "id":2,
    "title":"Data Scientist",
    "location":"Delhi, India",
    "salary":"Rs. 15,00,000"
  },
  {
    "id":3,
    "title":"Frontend Engineer",
    "location":"Remote",
    "salary":"Rs. 12,00,000"
  }
]

@app.route('/')
def helloworld():
  return render_template('home.html' , Jobs = jobs)
@app.route('/jobs')
def list_jobs():
  return jsonify(jobs)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
