from channels import Channel, Group
from channels.sessions import channel_session
from channels.auth import http_session_user, channel_session_user, channel_session_user_from_http
import time


# Connected to websocket.connect
@channel_session_user_from_http
def dashboard_connect(message):
    # Work out room name from path (ignore slashes)
    graph_channel = message.content['path'].strip("/")
    # Save room in session and add us to the group
    message.channel_session['graph'] = graph_channel
    Group("chat-%s" % graph_channel).add(message.reply_channel)


# Connected to websocket.receive
@channel_session_user_from_http
def dashboard_message(message):
    Group("chat-%s" % message.channel_session['graph']).send({
        "text": message['text'],
    })


# Connected to websocket.disconnect
@channel_session_user_from_http
def dashboard_disconnect(message):
    Group("chat-%s" % message.channel_session['graph']).discard(message.reply_channel)
