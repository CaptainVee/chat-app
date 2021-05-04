# from channels.auth import AuthMiddlewareStack
# from channels.routing import ProtocolTypeRouter, URLRouter
# import chat.routing

# application = ProtocolTypeRouter({
#     'websocket': AuthMiddlewareStack(
#         URLRouter(
#             chat.routing.websocket_urlpatterns
#         )
#     ),
# })






from django.conf.urls import url
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator, OriginValidator

from chat.consumers import ChatConsumer

application = ProtocolTypeRouter({

	'websocket': AllowedHostsOriginValidator(
		AuthMiddlewareStack(

			URLRouter(
				[
					url(r"messages/(?P<username>[\w.@+-]+)/", ChatConsumer),
				]
				)

			)

		)
	
	})