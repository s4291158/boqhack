from channels import Channel, Group
from channels.sessions import channel_session
from channels.auth import http_session_user, channel_session_user, channel_session_user_from_http


# Connected to websocket.connect
@channel_session_user_from_http
def chat_connect(message):
    # Work out room name from path (ignore slashes)
    room = message.content['path'].strip("/")
    print("room {0}".format(room))

    # Save room in session and add us to the group
    message.channel_session['room'] = room
    Group("chat-%s" % room).add(message.reply_channel)


# Connected to websocket.receive
@channel_session_user_from_http
def chat_message(message):
    print("what")
    Group("chat-%s" % message.channel_session['room']).send({
        "text": message['text'],
    })


# Connected to websocket.disconnect
@channel_session_user_from_http
def chat_disconnect(message):
    Group("chat-%s" % message.channel_session['room']).discard(message.reply_channel)