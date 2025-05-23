from flask import Flask, render_template

app = Flask(__name__, template_folder='../templates', static_folder='../static')

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')

@app.route('/experience', methods=['GET'])
def experience():
    return render_template('experience.html')

@app.route('/projects', methods=['GET'])
def projects():
    return render_template('projects.html')

@app.route('/skills', methods=['GET'])
def skills():
    return render_template('skills.html')

@app.route('/contact', methods=['GET'])
def contact():
    return render_template('contact.html')

@app.route('/honors', methods=['GET'])
def honors():
    return render_template('honors.html') 