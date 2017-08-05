from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

app.secret_key = 'mySecret'

@app.route('/')

def index():

	sumSessionCounter()

	return render_template('index.html')

@app.route('/add', methods=['POST'])

def sumSessionCounter():
	session['counter'] += 1
	return redirect('/')

@app.route('/process', methods=['POST'])

def reset():
	session['counter'] = 0	

	return redirect('/')
app.run(debug=True)