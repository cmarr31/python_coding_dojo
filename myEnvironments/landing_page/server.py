from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/ninjas')
def ninjas():
	return render_template("ninjas.html")

@app.route('/dojos', methods=['POST'])
def dojo():
	return render_template("dojos.html")
	print "Got post info."
	previous = request.form["previous"]
	new = request.form["new"]
	print request.form
	return redirect('/')

app.run(debug=True)