### Adapted from https://github.com/Samhita-alla/flask-chat-app-article ###

from flask import Flask
from flask_socketio import SocketIO

from flask import Flask, render_template
import sqlite3
from flask import g

DATABASE = '/var/ctp/lliu/git/data/temp_database.db'

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Buddha buddha lululand'
socketio = SocketIO(app)



def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('/var/ctp/lliu/git/data/schema.sql', mode='r') as f:
            try:
                db.cursor().executescript(f.read())
            except Exception as e:
        
                print (e)
        db.commit()


@app.route('/')
def sessions():
    #cur = get_db().cursor()
    #print (1)
    return render_template('session.html')


def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')

@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    socketio.emit('my response', json, callback=messageReceived)

print (2)


if __name__ == '__main__':
    print (1)
    init_db()
    socketio.run(app, debug=True,host='0.0.0.0', port=7799 )

