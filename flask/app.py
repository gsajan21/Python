from flask import Flask
from flask import render_template

app = Flask('__main__') # __main__

@app.route('/')
def home():
    greet = '<h1>Welcome to Takeo!<h1>'
    return greet
@app.route('/about')
def about():
    return '<h1>This is About Page!</h1>'

@app.route('/student/<studentName>')
def greetStudent(studentName):
    return f'<h1>Welcome {studentName} {__name__}!</h1>'

@app.route('/index')
def index():
    return render_template("main.html")

if __name__ == '__main__':
    app.run() # host/port/debug (by default --> host=localhost, port=5000, debug=false)