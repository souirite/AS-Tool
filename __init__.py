from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config["UPLOADED_FILES_DEST"] = "C:/Users/adil.souirite/Desktop/Workspace/AS Tool/Tool/uploads"
app.config["ALLOWED_FILE_EXTENSIONS"] = ["TXT"]


def allowed_filename(filename):
    if not "." in filename:
        return False
    # Split the extension from the filename
    ext = filename.rsplit(".", 1)[1]
    print(ext)
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
                file.save(os.path.join(
                    app.config["UPLOADED_FILES_DEST"], file.filename))
                print("file uploaded ")
                return render_template('eplan.html')
            return render_template('index.html')
            print("wrong extension")

    return render_template('index.html')


app.run(debug=True)
