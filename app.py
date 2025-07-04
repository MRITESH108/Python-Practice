from flask import Flask

'''
        It creates an instance of the Flask class , 
        which will be your WSGI (Web Server Gateway Interface) application.
'''
# WSGI Application

app=Flask(__name__)

@app.route("/")  # / means it's my home page
def hello():
    return "Hello, Welcome to Flask course.This is going to amazin journey."

@app.route("/index")
def index():
    return "This is the index page."


# entry point of every python code

if __name__ == '__main__':
    app.run(debug=True)