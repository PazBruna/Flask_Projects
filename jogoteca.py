from flask import Flask, render_template

app = Flask(__name__) #import name

@app.route('/inicio')
def ola():
    lista = ['Detroit', 'The Witcher', 'Uncharted', 'Tomb Raider', 'Beyond', 'Battlefield']
    return render_template('lista.html', titulo = 'Jogos', jogos = lista) #transformando o titulo em algo dinamico

app.run()

