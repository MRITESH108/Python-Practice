from flask import Flask, render_template, request

app=Flask(__name__)


@app.route('/')
def welcome():
    return "kya haal hai mitron. Sb mst na ."

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/form',methods=['GET','POST'])
def form():
    if request.method == 'POST':
        name=request.form['name']
        return f'hello {name}'
    return render_template('form.html')

@app.route('/submit',methods=['GET','POST'])
def submit():
    if request.method == 'POST':
        name=request.form['name']
        return f'hello jiii {name}'
    return render_template('form.html')

if __name__=='__main__':
    app.run(debug=True)