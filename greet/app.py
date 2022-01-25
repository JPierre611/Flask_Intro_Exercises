from flask import Flask

app = Flask(__name__)

@app.route('/welcome')
def welcome():
	"""Shows Welcome message"""
	return "welcome"

@app.route('/welcome/home')
def welcome_home():
	"""Shows welcome home message"""
	return "welcome home"

@app.route('/welcome/back')
def welcome_back():
	"""Shows welcome back message"""
	return "welcome back"
