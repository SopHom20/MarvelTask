from flask import Flask, render_template, request, redirect, url_for
from main import getCharacter, getDetails, getResults

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', characters = getResults())

@app.route('/searchCharacter', methods=['POST'])
def searchCharacter():
    title = request.form.get('title')
    getDetails(getCharacter(title))
    return redirect(url_for('index'))