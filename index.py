# This is vercel stuff
from flask_bootstrap import Bootstrap
from flask import Flask, render_template

template_folder_path = "Templates"
static_folder_path = "static"
    
app = Flask(__name__, template_folder=template_folder_path, static_folder=static_folder_path)
app.config['SECRET_KEY'] = '93688a56-2e91-4c5e-8a47-5c97e47024f5'
Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')

app.run(debug=True)