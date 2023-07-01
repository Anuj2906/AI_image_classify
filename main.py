import os
from flask import Flask, flash, request, redirect, url_for,render_template
from werkzeug.utils import secure_filename
from model import check
from PIL import Image


UPLOAD_FOLDER = 'static'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
def home():
    static_folder = app.static_folder
    for filename in os.listdir(static_folder):
        file_path = os.path.join(static_folder, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)
    return render_template("index.html")

@app.route("/edit", methods = {"GET","POST"})
def edit():
    if request.method == "POST":
        static_folder = app.static_folder
        for filename in os.listdir(static_folder):
            file_path = os.path.join(static_folder, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)
        if 'file' not in request.files:
            flash('No file part')
            return "error"
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return render_template("index.html")
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            image = Image.open(file)
            pre = check(image)
            if(pre >= 0.55):
                flash('REAL IMAGE')
            else:
                flash('AI GENERATED IMAGE')
            return render_template("index.html", filename = filename)
        else:
            flash('Allowed file types are: png, jpg, jpeg')

    return render_template("index.html")

@app.route("/display/<filename>")
def display_image(filename):
    return redirect(url_for('static', filename = filename), code = 301)

app.run(debug=True)