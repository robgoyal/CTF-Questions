import datetime
import os
import random
import string

from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

SHORT_ID_LENGTH = 3

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///shawty.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["DEBUG"] = True
app.config["TESTING"] = False
app.config["CSRF_ENABLED"] = True
app.config["SECRET_KEY"] = "guessme"

db = SQLAlchemy(app)

# Short URLS database - replaced with 
class ShortUrls(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(500), nullable=False)
    short_id = db.Column(db.String(20), nullable=False, unique=True)
    created_at = db.Column(db.DateTime(), default=datetime.datetime.now(), nullable=False)

# Create tables
with app.app_context():
    db.create_all()

def generate_short_id(num_of_chars: int):
    """Function to generate a short ID consisting of digits"""
    return ''.join(choice(string.digits) for _ in range(num_of_chars))
 
 
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        short_id = request.form['custom_id']

        if short_id and ShortUrls.query.filter_by(short_id=short_id).first() is not None:
            flash('Please enter different custom id!')
            return redirect(url_for('index'))

        if not url:
            flash('The URL is required!')
            return redirect(url_for('index'))

        if not short_id:
            short_id = generate_short_id(8)

        new_link = ShortUrls(
            original_url=url, short_id=short_id, created_at=datetime.datetime.now())
        db.session.add(new_link)
        db.session.commit()
        short_url = request.host_url + short_id

        return render_template('index.html', short_url=short_url)

    return render_template('index.html')

@app.route('/<short_id>')
def redirect_url(short_id):
    link = ShortUrls.query.filter_by(short_id=short_id).first()
    if link:
        return redirect(link.original_url)
    else:
        flash('Invalid URL')
        return redirect(url_for('index'))
