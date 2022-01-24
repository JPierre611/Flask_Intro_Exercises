from flask import Flask

app = Flask(__name__)

@app.route('/welcome')
def welcome_page():
	"""Shows Welcome message"""
	return "welcome"

@app.route('/welcome/home')
def welcome_home_page():
	"""Shows welcome home message"""
	return "welcome home"

@app.route('/welcome/back')
def welcome_back_page():
	"""Shows welcome back message"""
	return "welcome back"
