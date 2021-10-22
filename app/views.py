from flask import render_template, request
from flask import redirect, url_for
import os

UPLOADS_FOLDER = 'static/uploads'


def base():
    return render_template("base.html")
    
def index():
    return render_template("index.html")

def facerecapp():
    return render_template("facerecapp.html")

def gender():
    if request.method == 'POST':
        f = request.files['image']
        filename = f.filename
        path = os.path.join(UPLOADS_FOLDER,filename)
        f.save(path)
        return render_template("gender.html", fileupload = True, img_name= filename)
    return render_template("gender.html", fileupload = False, img_name = "FacerecAI.png")
