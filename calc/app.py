from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def addition():
	"""Perform addition operation."""
	a = int(request.args['a'])
	b = int(request.args['b'])
	return str(add(a, b))

@app.route('/sub')
def subtraction():
	"""Perform subtraction operation."""
	a = int(request.args['a'])
	b = int(request.args['b'])
	return str(sub(a, b))

@app.route('/mult')
def multiplication():
	"""Perform multiplication operation."""
	a = int(request.args['a'])
	b = int(request.args['b'])
	return str(mult(a, b))

@app.route('/div')
def division():
	"""Perform division operation."""
	a = int(request.args['a'])
	b = int(request.args['b'])
	return str(div(a, b))