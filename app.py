from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

users = {}

@app.route('/')
def index():
    return render_template('index.html')

# Evento de login
@socketio.on('login')
def handle_login(data):
    username = data['user']
    login = data['login']
    users[login] = username
    emit('message', {'message': f'{username} entrou no chat.'}, broadcast=True)

# Evento de mensagens
@socketio.on('message')
def handle_message(data):
    username = data['user']
    message = data['message']
    emit('message', {'message': f'{username}: {message}'}, broadcast=True)

# Evento de envio de imagem
@socketio.on('image')
def handle_image(data):
    username = data['user']
    image = data['image']
    emit('image', {'image': image, 'user': username}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)
