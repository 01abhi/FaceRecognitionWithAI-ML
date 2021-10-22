from flask import render_template, request
from flask import redirect, url_for
import os

UPLOADS_FOLEDER = 'static/uploads'


def base():
    return render_template("base.html")
    
def index():
    return render_template("index.html")

def facerecapp():
    return render_template("facerecapp.html")

def gender():
    return render_template("gender.html")
