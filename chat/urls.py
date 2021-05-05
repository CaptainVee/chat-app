from django.urls import path
from .views import ThreadView, InboxView, user

urlpatterns = [
	path('', user, name='blog-home'),
    path("messages/", InboxView.as_view(), name='inbox'),
    path('messages/<str:username>/', ThreadView.as_view(), name='thread'),
]
