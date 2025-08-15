from flask import Flask,request, render_template

app =  Flask(__name__)

@app.route('/', methods = ['GET','POST']) 
def index():
    if request.method == 'POST':
        nome = request.form.get('nome') 
        idade = request.form.get('idade')
        return render_template('resultado.html', nome = nome, idade = idade)
    
    return render_template('index.html')

@app.route('/sobre')
def sobre():
    return '<h2>Projeto Flask iniciante </h2>'


if __name__ == '__main__':
    app.run(debug = True)