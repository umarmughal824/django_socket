from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import chat.routing
import doulix.routing


application = ProtocolTypeRouter({
    # (http -> django views is added by default)
    'websocket': AuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns + doulix.routing.websocket_urlpatterns
        )
    )
})
