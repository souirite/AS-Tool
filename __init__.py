from flask import Flask, render_template, request
from config import config
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config.from_object(config)

def allowed_filename(filename):
    if not "." in filename:
        return False
    # Split the extension from the filename
    ext = filename.rsplit(".", 1)[1]    
   # Check if the extension is in ALLOWED_FILE_EXTENSIONS
    if ext.upper() in app.config["ALLOWED_FILE_EXTENSIONS"]:
        return True
    else:
        return False

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/eplan', methods=["GET", "POST"])
def eplan():
    if request.method == 'POST':
        if request.files:
            file = request.files['file']
            filename = secure_filename(file.filename)
            if allowed_filename(filename):
                g = []
                file.save(os.path.join(app.config["UPLOADED_FILES_DEST"], file.filename))
                f = open(os.path.join(app.config["UPLOADED_FILES_DEST"], file.filename),'r')
                for line in f.readlines():
                    l = line.strip().split('\t')     
                    g.append(l)
                
                return render_template('eplan.html', file =g)
            return render_template('index.html')
            print("wrong extension")

    return render_template('index.html')


app.run(debug=True)
