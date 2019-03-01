from flask import Flask, render_template, request

app = Flask(__name__) #import name

class Jogo:
    def __init__(self, nome, categoria, console):
        self._nome = nome
        self.categoria = categoria
        self.console = console

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def novo_nome(self, novo_nome):
        self._nome = novo_nome.title()


jogo1 = Jogo('Detroit' , 'Ação', 'Playstation 4')
jogo2 = Jogo('The Witcher', 'Ação', 'Playstation 4')
jogo3 = Jogo('Uncharted', 'Aventura', 'Playstation 4 e Xbox One')
jogo4 = Jogo('Tomb Raider', 'Aventura', 'Playstation 4, Xbox One')
jogo5 = Jogo('Beyond', 'Suspense', 'Playstation 4')
jogo6 = Jogo('Battlefield', 'Ação', 'Playstation 4, Xbox One e PC')
lista = [jogo1, jogo2, jogo3, jogo4, jogo5, jogo6]

@app.route('/')
def index():
    return render_template('lista.html', titulo = 'Jogos', jogos = lista) #transformando o titulo em algo dinamico

@app.route('/cadastro')
def cadastro():
    return render_template('novo.html', titulo = 'Cadastro Novo Jogo:' )

@app.route('/criar', methods = ['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return render_template('lista.html', titulo ='Jogos', jogos = lista)

app.run(debug = True)

