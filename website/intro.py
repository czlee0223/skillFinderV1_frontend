from flask import Blueprint, render_template
from jinja2 import Template

intro = Blueprint('intro',__name__)

@intro.route('/')
def home():
    return render_template("intro.html")