import sqlite3
from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/')
def main():
	return render_template("home.html")