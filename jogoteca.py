from flask import Flask, render_template

app = Flask(__name__) #import name

@app.route('/inicio')
def ola():
    return render_template('lista.html', titulo = 'Jogos') #transformando o titulo em algo dinamico

app.run()

