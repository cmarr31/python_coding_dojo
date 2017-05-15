from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/process', methods=['POST'])
def users_name():
	return render_template("process.html")
	first_last = request.form['first_last']
	print first_last
   	return redirect('/')




app.run(debug=True)