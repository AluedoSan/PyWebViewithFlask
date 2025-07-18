from flask import Flask, redirect, render_template, request, url_for, session, jsonify
import webview, os
import db

# Inicialização do app
server = Flask(__name__, static_folder='./static', template_folder='./templates')
server.config['DATABASE'] = os.path.join(server.root_path, '..', 'tutorial.db')

server.secret_key = 'Um@_(h@V&_f0rT&_AnD_$&gUr@'


@server.route("/")
def index():
    if 'user_id' not in session:
        return redirect(url_for('register'))
    print(session)
    return render_template("index.html")

@server.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Exemplo simples: validação fake
        email = request.form['email']
        senha = request.form['senha']
        
        # Aqui você chamaria db.get_user_by_email() para validar de verdade
        if email == 'teste@email.com' and senha == '123':
            session['user_id'] = 1  # Normalmente seria o ID real do usuário no banco
            return redirect(url_for('index'))
        else:
            return render_template('login.html', msg=True)

    return render_template('login.html')

@server.route("/register", methods=['GET' ,'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        
        db.criar_usuario(email, senha)
        return jsonify({"message": "Usuário cadastrado com sucesso!"})
    return render_template('register.html')

@server.route("/logout")
def logout():
    session.pop('user_id', None)
    return redirect(url_for('login'))

@server.route("/faturas", methods=['GET', 'POST'])
def faturas():
    if request.method == 'POST':
        nome = request.form['nome']
        total = request.form['total']
        descricao = request.form['descricao'] if request.form['descricao'] != "" else "None"
        db.cadastrar_banco(nome, total, descricao)
        return render_template('faturas.html', msg=True)
    bancos = db.listar_bancos()
    return render_template('faturas.html', msg=False, a = True, bancos=bancos)

@server.route("/faturas/<int:id>")
def banco_detalhes(id):
    banco = db.get_banco(id)
    bancos = db.listar_bancos()
    return render_template('faturas.html', msg=False,a = True,b = True, banco=banco, bancos=bancos)

if __name__ == '__main__':
    webview.create_window('Flask example', server)
    webview.start()
