from flask import Flask, render_template, request, url_for, redirect 

app = Flask(__name__) 

@app.route("/") 
def home(): 
		return render_template('home.html')

@app.route("/projects") 
def projects(): 
		return render_template('projects.html')

@app.route("/aboutus") 
def aboutus(): 
		return render_template('aboutus.html')

@app.route("/team") 
def team(): 
		return render_template('team.html')

@app.route("/examingo")
def examingo():
	return render_template('examingo.html')

@app.route("/chat")
def chat():
	return render_template('chat.html')

@app.route("/weather")
def weather():
	return render_template('weather.html')

@app.route("/taskmanager")
def taskmanager():
	return render_template('taskmanager.html')

@app.route("/chatbot")
def chatbot():
	return render_template('chatbot.html')

@app.route("/prashantresume")
def prashantresume():
	return render_template('prashantresume.html')

@app.route("/manavresume")
def manavresume():
	return render_template('manavresume.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
