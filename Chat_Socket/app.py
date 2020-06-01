from flask import Flask
from flask_socketio import SocketIO, join_room, emit, send, leave_room


ROOMS = set()
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!!'
socketio = SocketIO(app,cors_allowed_origins="*")

@socketio.on('connect')
def test_connect():
    print('connected')
    emit( {'data': 'Connected'})

@socketio.on('create')
def on_create(data):
    print(data)
    if (data['user1'], data['user2']) not in ROOMS:
        ROOMS.add((data['user1'], data['user2']))
        ROOMS.add((data['user2'], data['user1']))
    room = data['user1'] or data['user2']
    join_room(room)
    print(data)
    emit('join_room', {'room': room})


@socketio.on('join')
def on_join(data):
    x = (data['user1'], data['user2'])
    print(data)
    if x in ROOMS:
        join_room(data['room'])
        send("{} and {} has joined".format(data['user1'], data['user2']), room=data['room'])
    else:
        emit('Unable to join room. Room does not exist.', room=data['room'])


@socketio.on('message')
def handle_message(data):
    print(data,'message')
    send(data, room=data['room'])


@socketio.on('leave')
def on_leave(data):
    username = data['user1']
    room = data['room']
    ROOMS.remove((data['user1'], data['user2']))
    ROOMS.remove((data['user2'], data['user1']))
    leave_room(room)
    send(username + ' has left the room.', room=room)


@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')


if __name__ == '__main__':
    socketio.run(app, debug=True,port=5002)
