from flask import Flask,render_template

app=Flask(__name__)


@app.route('/')
def welcome():
    return "kya haal hai mitron. Sb mst na ."

@app.route('/index')
def index():
    return render_template('index.html')



if __name__=='__main__':
    app.run(debug=True)