from flask import Flask,redirect,render_template
from weather import app



@app.route('/')
def home():
    return render_template('home.html')