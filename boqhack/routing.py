from channels.routing import route, include
from chatroom.consumers import *
from dashboard.consumers import *

chat_routing = [
    route("websocket.connect", chat_connect),
    route("websocket.receive", chat_message),
    route("websocket.disconnect", chat_disconnect),
]

dashboard_routing = [
    route("websocket.connect", dashboard_connect),
    route("websocket.receive", dashboard_message),
    route("websocket.disconnect", dashboard_disconnect),
]

routing = [
    include(chat_routing, path=r"^/chat"),
    include(dashboard_routing, path=r"^/dashboard"),
]
