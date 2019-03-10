from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__) #import name
app.secret_key = 'paz'


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


jogo1 = Jogo('Detroit: Become Human' , 'Ação', 'Playstation 4')
jogo2 = Jogo('The Witcher', 'Ação', 'Playstation 4')
jogo3 = Jogo('Uncharted', 'Aventura', 'Playstation 4 e Xbox One')
jogo4 = Jogo('Tomb Raider', 'Aventura', 'Playstation 4, Xbox One')
jogo5 = Jogo('Beyond Two Souls', 'Suspense', 'Playstation 4')
jogo6 = Jogo('BattleField', 'Ação', 'Playstation 4, Xbox One e PC')
lista = [jogo1, jogo2, jogo3, jogo4, jogo5, jogo6]

@app.route('/lista')
def index():
    return render_template('lista.html', titulo = 'Jogos', jogos = lista) #transformando o titulo em algo dinamico

@app.route('/cadastro')
def cadastro():
    return render_template('novo.html', titulo = 'Cadastre um novo jogo:' )

@app.route('/criar', methods = ['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return redirect('/lista')

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/autenticar', methods =['POST'])
def autenticar():
    if 'mestra' == request.form['senha']:
        session['usuario_logado'] = request.form['usuario']
        flash(request.form['usuario'] + ' logou com sucesso')
        return redirect('/lista')
    else:
        flash('Senha e/ou email Incorreto')
        return redirect('/')

app.run(debug = True)

