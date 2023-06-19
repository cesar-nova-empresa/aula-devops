import requests
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World! -- TURMA DA CESAR SCHOOL"

@app.route('/cesar')
def index_cesar():
    return "Hello, World! -- ROTA CESAR"
