from flask import render_template, request
from flask import redirect, url_for
import os
from PIL import Image
from app.utils import pipeline_model

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
        w = getwidth(path)
        #prediction by passing to pipeline model
        pipeline_model(path, filename, color='bgr')
        return render_template("gender.html", fileupload = True, img_name= filename, w = w)
        
    return render_template("gender.html", fileupload = False, img_name = "No Image", w = 300)

def getwidth(path):
    img = Image.open(path)
    size = img.size
    aspect = size[0]/size[1] #aspect ratio
    w = 300 * aspect
    return int(w)