from flask import Flask, render_template, request, redirect, url_for, session
app = Flask(__name__)

@app.route('/')
@app.route('/menu')
def menu():
	return render_template('menu.html')

@app.route('/pop')
def pop():
	return render_template('pop.html')

@app.route('/rock')
def rock():
	return render_template('rock.html')

@app.route("/edm")
def edm():
	return render_template('edm.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/suggest')
def suggest():
	return render_template('suggest.html')



if __name__ == '__main__':
	app.run(debug=True)
