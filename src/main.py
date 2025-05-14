from flask import Flask, render_template, request, g
import webview, sqlite3, os

# Inicialização do app
server = Flask(__name__, static_folder='./static', template_folder='./templates')
server.config['DATABASE'] = os.path.join(server.root_path, '..', 'tutorial.db')


@server.route("/")
def hello_world():
    return render_template("index.html")

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(server.config['DATABASE'])
        g.db.row_factory = sqlite3.Row
    return g.db


@server.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

if __name__ == '__main__':
    webview.create_window('Flask example', server)
    webview.start()
